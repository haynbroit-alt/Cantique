"""Matériel cryptographique stocké dans des fichiers : blocs PEM, certificats
DER, clés OpenSSH. Ne renvoie jamais le contenu d'une clé privée : seuls
l'algorithme, la taille ou la courbe sont lus, et les extraits sont masqués.

L'analyse des certificats utilise le paquet ``cryptography`` s'il est
installé ; sinon un lecteur DER minimal (bibliothèque standard) lit
l'algorithme de la clé publique. Si les deux échouent, l'élément est rangé
« à vérifier » (famille inconnue, confiance faible).
"""
from __future__ import annotations

import base64
import binascii
import hashlib
import re
import struct
from datetime import datetime, timezone

from .familles import Algo, resoudre

try:  # dépendance facultative
    from cryptography import x509 as _x509
    from cryptography.hazmat.primitives import serialization as _serialization

    _CRYPTOGRAPHY = True
except ImportError:  # pragma: no cover - dépend de l'environnement
    _CRYPTOGRAPHY = False

MOTIF_PEM = re.compile(r"-----BEGIN ([A-Z0-9 ]{3,40})-----(.*?)-----END \1-----", re.S)
MOTIF_SSH_PUB = re.compile(
    r"(?<![\w-])(ssh-rsa|ssh-dss|ssh-ed25519|ssh-ed448|ecdsa-sha2-nistp(?:256|384|521)|"
    r"sk-ssh-ed25519@openssh\.com|sk-ecdsa-sha2-nistp256@openssh\.com)\s+(AAAA[0-9A-Za-z+/]{20,}={0,2})"
)
_B64_LONG = re.compile(r"[A-Za-z0-9+/]{40,}={0,2}")
_HEX_LONG = re.compile(r"(?<![0-9A-Za-z])(?:0x)?[0-9A-Fa-f]{32,}(?![0-9A-Za-z])")


def masquer(texte: str, longueur_max: int = 160) -> str:
    """Masque les longues séquences base64 / hexadécimales (clés, secrets)."""
    t = _B64_LONG.sub("[masqué]", texte)
    t = _HEX_LONG.sub("[masqué]", t)
    t = t.strip()
    return t if len(t) <= longueur_max else t[: longueur_max - 1] + "…"


# ---------------------------------------------------------------------------
# Lecteur DER minimal
# ---------------------------------------------------------------------------
def _tlv(data: bytes, pos: int) -> tuple[int, bytes, int]:
    if pos + 2 > len(data):
        raise ValueError("DER tronqué")
    tag, lon = data[pos], data[pos + 1]
    pos += 2
    if lon & 0x80:
        n = lon & 0x7F
        if not 0 < n <= 4:
            raise ValueError("longueur DER invalide")
        lon = int.from_bytes(data[pos:pos + n], "big")
        pos += n
    fin = pos + lon
    if fin > len(data):
        raise ValueError("DER tronqué")
    return tag, data[pos:fin], fin


def _enfants(data: bytes) -> list[tuple[int, bytes]]:
    res, pos = [], 0
    while pos < len(data):
        tag, val, pos = _tlv(data, pos)
        res.append((tag, val))
    return res


def _seq(der: bytes) -> list[tuple[int, bytes]]:
    tag, val, _ = _tlv(der, 0)
    if tag != 0x30:
        raise ValueError("SEQUENCE attendue")
    return _enfants(val)


def _oid(val: bytes) -> str:
    premier = val[0]
    parts = [min(premier // 40, 2), premier - 40 * min(premier // 40, 2)]
    n = 0
    for b in val[1:]:
        n = (n << 7) | (b & 0x7F)
        if not b & 0x80:
            parts.append(n)
            n = 0
    return ".".join(map(str, parts))


def _bits(entier: bytes) -> int:
    return int.from_bytes(entier, "big").bit_length()


_OID_COURBES = {
    "1.2.840.10045.3.1.7": "P-256", "1.3.132.0.34": "P-384", "1.3.132.0.35": "P-521",
    "1.3.132.0.33": "P-224", "1.3.132.0.10": "secp256k1", "1.3.36.3.3.2.8.1.1.7": "brainpoolP256r1",
    "1.3.36.3.3.2.8.1.1.11": "brainpoolP384r1", "1.3.36.3.3.2.8.1.1.13": "brainpoolP512r1",
}
_OID_CLES = {
    "1.2.840.113549.1.1.1": "RSA", "1.2.840.113549.1.1.10": "RSA-PSS", "1.2.840.10045.2.1": "EC",
    "1.3.101.112": "Ed25519", "1.3.101.113": "Ed448", "1.3.101.110": "X25519", "1.3.101.111": "X448",
    "1.2.840.10040.4.1": "DSA", "1.2.840.10046.2.1": "DH", "1.2.840.113549.1.3.1": "DH",
    "2.16.840.1.101.3.4.4.1": "ML-KEM-512", "2.16.840.1.101.3.4.4.2": "ML-KEM-768",
    "2.16.840.1.101.3.4.4.3": "ML-KEM-1024", "2.16.840.1.101.3.4.3.17": "ML-DSA-44",
    "2.16.840.1.101.3.4.3.18": "ML-DSA-65", "2.16.840.1.101.3.4.3.19": "ML-DSA-87",
}
_SLH = ["SHA2-128s", "SHA2-128f", "SHA2-192s", "SHA2-192f", "SHA2-256s", "SHA2-256f",
        "SHAKE-128s", "SHAKE-128f", "SHAKE-192s", "SHAKE-192f", "SHAKE-256s", "SHAKE-256f"]
_OID_CLES.update({f"2.16.840.1.101.3.4.3.{20 + i}": f"SLH-DSA-{p}" for i, p in enumerate(_SLH)})
_OID_SIGNATURES = {
    "1.2.840.113549.1.1.4": "MD5withRSA", "1.2.840.113549.1.1.5": "SHA1withRSA",
    "1.2.840.113549.1.1.11": "SHA256withRSA", "1.2.840.113549.1.1.12": "SHA384withRSA",
    "1.2.840.113549.1.1.13": "SHA512withRSA", "1.2.840.113549.1.1.14": "SHA224withRSA",
    "1.2.840.113549.1.1.10": "RSASSA-PSS", "1.2.840.10045.4.1": "SHA1withECDSA",
    "1.2.840.10045.4.3.1": "SHA224withECDSA", "1.2.840.10045.4.3.2": "SHA256withECDSA",
    "1.2.840.10045.4.3.3": "SHA384withECDSA", "1.2.840.10045.4.3.4": "SHA512withECDSA",
    "1.3.101.112": "Ed25519", "1.3.101.113": "Ed448", "1.2.840.10040.4.3": "SHA1withDSA",
    "2.16.840.1.101.3.4.3.2": "SHA256withDSA",
}
_OID_SIGNATURES.update({o: n for o, n in _OID_CLES.items() if n.startswith(("ML-DSA", "SLH-DSA"))})


def _algo_cle(nom: str, taille: int | None = None, courbe: str | None = None) -> Algo | None:
    algos = resoudre(nom)
    if not algos:
        return None
    a = algos[0]
    a.taille = taille or a.taille
    a.courbe = courbe or a.courbe
    if a.nom == "EC" and a.courbe:
        a.nom = f"EC-{a.courbe}"
    return a


def _algo_spki(spki: list[tuple[int, bytes]]) -> Algo | None:
    """spki : enfants de SubjectPublicKeyInfo."""
    algid = _enfants(spki[0][1])
    oid = _oid(algid[0][1])
    nom = _OID_CLES.get(oid)
    if not nom:
        return None
    taille = courbe = None
    if nom in ("RSA", "RSA-PSS"):
        cle = spki[1][1][1:]  # octet « bits inutilisés »
        taille = _bits(_seq(cle)[0][1])
    elif nom == "EC" and len(algid) > 1 and algid[1][0] == 0x06:
        courbe = _OID_COURBES.get(_oid(algid[1][1]))
    elif nom in ("DSA", "DH") and len(algid) > 1 and algid[1][0] == 0x30:
        taille = _bits(_enfants(algid[1][1])[0][1])
    return _algo_cle("RSA" if nom == "RSA-PSS" else nom, taille, courbe)


def _nom_x500(val: bytes) -> str:
    noms = {"2.5.4.3": "CN", "2.5.4.10": "O", "2.5.4.11": "OU", "2.5.4.6": "C"}
    parts = []
    for _, rdn in _enfants(val):
        for _, atv in _enfants(rdn):
            elems = _enfants(atv)
            cle = noms.get(_oid(elems[0][1]))
            if cle:
                v = elems[1][1]
                parts.append(f"{cle}={v.decode('utf-16-be' if elems[1][0] == 0x1E else 'utf-8', 'replace')}")
    return ",".join(parts)


def _date_der(tag: int, val: bytes) -> str:
    s = val.decode("ascii")
    fmt = "%y%m%d%H%M%SZ" if tag == 0x17 else "%Y%m%d%H%M%SZ"
    return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _certificat_der(der: bytes) -> dict:
    tbs = _enfants(_seq(der)[0][1])
    if tbs[0][0] == 0xA0:  # version explicite
        tbs = tbs[1:]
    sig_oid = _oid(_enfants(tbs[1][1])[0][1])
    validite = _enfants(tbs[3][1])
    return {
        "cle": _algo_spki(_enfants(tbs[5][1])),
        "signature": _OID_SIGNATURES.get(sig_oid, sig_oid),
        "emetteur": _nom_x500(tbs[2][1]),
        "sujet": _nom_x500(tbs[4][1]),
        "not_before": _date_der(*validite[0]),
        "not_after": _date_der(*validite[1]),
        "analyseur": "der-stdlib",
    }


def _certificat_cryptography(der: bytes) -> dict:
    cert = _x509.load_der_x509_certificate(der)
    try:
        spki = cert.public_key().public_bytes(
            encoding=_serialization.Encoding.DER, format=_serialization.PublicFormat.SubjectPublicKeyInfo)
        cle = _algo_spki(_seq(spki))
    except Exception:  # type de clé inconnu de cryptography : on retombe sur le DER brut
        cle = _certificat_der(der)["cle"]
    oid = cert.signature_algorithm_oid.dotted_string
    return {
        "cle": cle,
        "signature": _OID_SIGNATURES.get(oid, oid),
        "emetteur": cert.issuer.rfc4514_string(),
        "sujet": cert.subject.rfc4514_string(),
        "not_before": cert.not_valid_before_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "not_after": cert.not_valid_after_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "analyseur": "cryptography",
    }


def analyser_certificat(der: bytes, utiliser_cryptography: bool | None = None) -> dict | None:
    """Renvoie les informations d'un certificat X.509 DER, ou None si illisible."""
    if utiliser_cryptography is None:
        utiliser_cryptography = _CRYPTOGRAPHY
    try:
        infos = _certificat_cryptography(der) if utiliser_cryptography else _certificat_der(der)
    except Exception:
        try:
            infos = _certificat_der(der)
        except Exception:
            return None
    infos["empreinte_sha256"] = hashlib.sha256(der).hexdigest()
    return infos


# ---------------------------------------------------------------------------
# Clés privées / publiques
# ---------------------------------------------------------------------------
def _cle_pkcs8(der: bytes) -> Algo | None:
    elems = _seq(der)
    algid = _enfants(elems[1][1])
    nom = _OID_CLES.get(_oid(algid[0][1]))
    if not nom:
        return None
    taille = courbe = None
    if nom in ("RSA", "RSA-PSS"):
        taille = _bits(_seq(elems[2][1])[1][1])
    elif nom == "EC" and len(algid) > 1 and algid[1][0] == 0x06:
        courbe = _OID_COURBES.get(_oid(algid[1][1]))
    elif nom in ("DSA", "DH") and len(algid) > 1 and algid[1][0] == 0x30:
        taille = _bits(_enfants(algid[1][1])[0][1])
    return _algo_cle("RSA" if nom == "RSA-PSS" else nom, taille, courbe)


def _lire_chaine_ssh(data: bytes, pos: int) -> tuple[bytes, int]:
    (lon,) = struct.unpack(">I", data[pos:pos + 4])
    return data[pos + 4:pos + 4 + lon], pos + 4 + lon


def algo_cle_ssh(blob: bytes) -> Algo | None:
    """Blob de clé publique SSH (RFC 4253) -> Algo."""
    type_cle, pos = _lire_chaine_ssh(blob, 0)
    t = type_cle.decode("ascii", "replace")
    if t == "ssh-rsa":
        _e, pos = _lire_chaine_ssh(blob, pos)
        n, _ = _lire_chaine_ssh(blob, pos)
        return _algo_cle("RSA", _bits(n))
    return resoudre_type_ssh(t)


def resoudre_type_ssh(t: str) -> Algo | None:
    t = t.replace("-cert-v01@openssh.com", "")
    if t in ("ssh-rsa", "rsa-sha2-256", "rsa-sha2-512"):
        return Algo("RSA", "RSA", "signature")
    if t == "ssh-dss":
        return Algo("DSA", "DSA", "signature")
    if t in ("ssh-ed25519", "sk-ssh-ed25519@openssh.com"):
        return Algo("EDDSA", "Ed25519", "signature", courbe="Ed25519")
    if t == "ssh-ed448":
        return Algo("EDDSA", "Ed448", "signature", courbe="Ed448")
    m = re.fullmatch(r"(?:sk-)?ecdsa-sha2-nistp(256|384|521)(?:@openssh\.com)?", t)
    if m:
        c = f"P-{m.group(1)}"
        return Algo("ECDSA", f"ECDSA-{c}", "signature", courbe=c)
    return None


def _cle_openssh(der: bytes) -> Algo | None:
    magie = b"openssh-key-v1\x00"
    if not der.startswith(magie):
        return None
    pos = len(magie)
    for _ in range(3):  # ciphername, kdfname, kdfoptions
        _, pos = _lire_chaine_ssh(der, pos)
    pos += 4  # nombre de clés
    pub, _ = _lire_chaine_ssh(der, pos)
    return algo_cle_ssh(pub)


def analyser_bloc_pem(type_bloc: str, corps: str) -> dict:
    """Analyse un bloc PEM. Renvoie {"algos": [...], "notes": [...], "certificat": dict|None}.

    ``algos`` vide = famille inconnue (à vérifier manuellement).
    """
    res: dict = {"algos": [], "notes": [], "certificat": None}
    prive = "PRIVATE KEY" in type_bloc
    if prive:
        res["notes"].append("cle_privee")
    if "ENCRYPTED" in corps or type_bloc == "ENCRYPTED PRIVATE KEY":
        res["notes"].append("chiffree")
    corps = corps.replace("\\n", "\n").replace("\\r", "")
    lignes = [li.strip().strip('"\',') for li in corps.strip().splitlines() if li.strip() and ":" not in li]
    try:
        der = base64.b64decode("".join(lignes), validate=False)
    except (binascii.Error, ValueError):
        der = b""

    def ajouter(a: Algo | None) -> None:
        if a:
            res["algos"].append(a)

    try:
        if type_bloc in ("CERTIFICATE", "TRUSTED CERTIFICATE", "X509 CERTIFICATE"):
            res["notes"].append("certificat")
            infos = analyser_certificat(der)
            if infos:
                res["certificat"] = infos
                ajouter(infos["cle"])
        elif type_bloc == "RSA PRIVATE KEY":
            taille = None if "chiffree" in res["notes"] else _bits(_seq(der)[1][1])
            ajouter(_algo_cle("RSA", taille))
        elif type_bloc == "RSA PUBLIC KEY":
            res["notes"].append("cle_publique")
            ajouter(_algo_cle("RSA", _bits(_seq(der)[0][1])))
        elif type_bloc == "EC PRIVATE KEY":
            courbe = None
            if "chiffree" not in res["notes"]:
                for tag, val in _seq(der):
                    if tag == 0xA0:
                        courbe = _OID_COURBES.get(_oid(_enfants(val)[0][1]))
            ajouter(_algo_cle("EC", None, courbe))
        elif type_bloc == "DSA PRIVATE KEY":
            ajouter(_algo_cle("DSA", None if "chiffree" in res["notes"] else _bits(_seq(der)[1][1])))
        elif type_bloc == "PRIVATE KEY":
            ajouter(_cle_pkcs8(der))
        elif type_bloc == "PUBLIC KEY":
            res["notes"].append("cle_publique")
            ajouter(_algo_spki(_seq(der)))
        elif type_bloc in ("CERTIFICATE REQUEST", "NEW CERTIFICATE REQUEST"):
            res["notes"].append("csr")
            info = _enfants(_seq(der)[0][1])
            ajouter(_algo_spki(_enfants(info[2][1])))
        elif type_bloc == "OPENSSH PRIVATE KEY":
            ajouter(_cle_openssh(der))
        elif type_bloc == "DH PARAMETERS":
            ajouter(_algo_cle("DH", _bits(_seq(der)[0][1])))
        elif type_bloc == "EC PARAMETERS":
            ajouter(_algo_cle("EC", None, _OID_COURBES.get(_oid(_tlv(der, 0)[1]))))
    except (ValueError, IndexError, struct.error, UnicodeDecodeError):
        pass  # contenu illisible : famille inconnue
    return res
