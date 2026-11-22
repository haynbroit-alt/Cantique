"""Familles cryptographiques du contrat (referentiel/SCHEMA.md) et normalisation
des noms d'algorithmes rencontrés dans le code, les configurations et TLS.

Tout ce qui est déterministe et partagé entre le scanner, le CBOM et le rapport
vit ici : table des familles, libellés FR/EN, résolution d'un nom d'algorithme
("SHA256withRSA", "aes-256-gcm", "X25519MLKEM768"...) vers une famille.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# Table de SCHEMA.md, dans le même ordre. Ne pas ajouter d'identifiant ici sans
# modifier le contrat.
FAMILLES: dict[str, str] = {
    "RSA": "vulnerable_shor",
    "ECDSA": "vulnerable_shor",
    "ECDH": "vulnerable_shor",
    "EDDSA": "vulnerable_shor",
    "X25519_X448": "vulnerable_shor",
    "DH": "vulnerable_shor",
    "DSA": "vulnerable_shor",
    "ML-KEM": "pqc",
    "ML-DSA": "pqc",
    "SLH-DSA": "pqc",
    "FN-DSA": "pqc",
    "HYBRID_KEM": "hybride",
    "AES": "symetrique",
    "CHACHA20": "symetrique",
    "3DES": "obsolete_classique",
    "DES": "obsolete_classique",
    "RC4": "obsolete_classique",
    "MD5": "obsolete_classique",
    "SHA1": "obsolete_classique",
    "SHA2": "hachage_ok",
    "SHA3": "hachage_ok",
    "TLS_LEGACY": "obsolete_classique",
    "TLS_SUITE": "inventaire",
}

FAMILLES_LIBELLES: dict[str, tuple[str, str]] = {
    "RSA": ("RSA (chiffrement, signature, échange de clés)", "RSA (encryption, signature, key exchange)"),
    "ECDSA": ("Signatures ECDSA", "ECDSA signatures"),
    "ECDH": ("Échange de clés ECDH (courbes NIST, Brainpool)", "ECDH key exchange (NIST, Brainpool curves)"),
    "EDDSA": ("Signatures Ed25519 / Ed448", "Ed25519 / Ed448 signatures"),
    "X25519_X448": ("Échange de clés X25519 / X448", "X25519 / X448 key exchange"),
    "DH": ("Diffie-Hellman à corps fini", "Finite-field Diffie-Hellman"),
    "DSA": ("DSA", "DSA"),
    "ML-KEM": ("ML-KEM (FIPS 203), Kyber", "ML-KEM (FIPS 203), Kyber"),
    "ML-DSA": ("ML-DSA (FIPS 204), Dilithium", "ML-DSA (FIPS 204), Dilithium"),
    "SLH-DSA": ("SLH-DSA (FIPS 205), SPHINCS+", "SLH-DSA (FIPS 205), SPHINCS+"),
    "FN-DSA": ("FN-DSA (FIPS 206 en projet), Falcon", "FN-DSA (draft FIPS 206), Falcon"),
    "HYBRID_KEM": ("Échange hybride classique + post-quantique", "Hybrid classical + post-quantum key exchange"),
    "AES": ("AES", "AES"),
    "CHACHA20": ("ChaCha20, ChaCha20-Poly1305", "ChaCha20, ChaCha20-Poly1305"),
    "3DES": ("Triple DES", "Triple DES"),
    "DES": ("DES", "DES"),
    "RC4": ("RC4", "RC4"),
    "MD5": ("MD5", "MD5"),
    "SHA1": ("SHA-1", "SHA-1"),
    "SHA2": ("SHA-2 (SHA-224 à SHA-512)", "SHA-2 (SHA-224 to SHA-512)"),
    "SHA3": ("SHA-3, SHAKE", "SHA-3, SHAKE"),
    "TLS_LEGACY": ("Protocoles SSL 3.0, TLS 1.0, TLS 1.1", "SSL 3.0, TLS 1.0, TLS 1.1 protocols"),
    "TLS_SUITE": ("Suites et protocoles TLS observés", "Observed TLS suites and protocols"),
}

CLASSES_LIBELLES: dict[str, tuple[str, str]] = {
    "vulnerable_shor": ("Vulnérable (algorithme de Shor)", "Vulnerable (Shor's algorithm)"),
    "obsolete_classique": ("Obsolète dès aujourd'hui", "Already obsolete today"),
    "hybride": ("Hybride classique + post-quantique", "Hybrid classical + post-quantum"),
    "pqc": ("Post-quantique normalisé", "Standardised post-quantum"),
    "symetrique": ("Symétrique (taille de clé à vérifier)", "Symmetric (check key size)"),
    "hachage_ok": ("Hachage robuste", "Robust hashing"),
    "inventaire": ("Inventaire TLS", "TLS inventory"),
}
ORDRE_CLASSES = list(CLASSES_LIBELLES)

# Familles dont la menace principale est « collecter maintenant, déchiffrer plus tard ».
ECHANGE_CLES = {"ECDH", "X25519_X448", "DH"}
SIGNATURES = {"ECDSA", "EDDSA", "DSA"}

FONCTIONS_LIBELLES: dict[str, tuple[str, str]] = {
    "keygen": ("génération de clé", "key generation"),
    "generate": ("génération", "generation"),
    "sign": ("signature", "signing"),
    "verify": ("vérification de signature", "signature verification"),
    "encrypt": ("chiffrement", "encryption"),
    "decrypt": ("déchiffrement", "decryption"),
    "digest": ("empreinte", "hashing"),
    "tag": ("MAC", "MAC"),
    "keyderive": ("accord / dérivation de clé", "key agreement / derivation"),
    "encapsulate": ("encapsulation", "encapsulation"),
    "decapsulate": ("décapsulation", "decapsulation"),
    "other": ("autre usage", "other use"),
}

NOTES_LIBELLES: dict[str, tuple[str, str]] = {
    "import": ("import du module, usage non confirmé", "module import, use not confirmed"),
    "commentaire": ("ligne commentée", "commented-out line"),
    "ec_ambigu": ("clé EC : ECDSA ou ECDH selon l'usage", "EC key: ECDSA or ECDH depending on use"),
    "non_securitaire": ("déclaré usedforsecurity=False", "declared usedforsecurity=False"),
    "kyber": ("nom antérieur à la norme (Kyber)", "pre-standard name (Kyber)"),
    "dilithium": ("nom antérieur à la norme (Dilithium)", "pre-standard name (Dilithium)"),
    "non_nist": ("hybride non normalisé par le NIST (sntrup761)", "hybrid not standardised by NIST (sntrup761)"),
    "chaine": ("nom d'algorithme dans une chaîne", "algorithm name in a string literal"),
    "cle_privee": ("clé privée présente dans les fichiers analysés", "private key present in the scanned files"),
    "cle_publique": ("clé publique", "public key"),
    "certificat": ("certificat X.509", "X.509 certificate"),
    "csr": ("demande de certificat (CSR)", "certificate signing request (CSR)"),
    "chiffree": ("clé chiffrée, paramètres non lus", "encrypted key, parameters not read"),
    "sig_cle_inconnue": ("type de clé non visible statiquement", "key type not statically visible"),
    "tls_defaut": ("paramètres TLS par défaut de la bibliothèque", "library default TLS settings"),
    "tls_config": ("configuration TLS", "TLS configuration"),
    "ssh_config": ("configuration SSH", "SSH configuration"),
    "suite_faible": ("suite faible activée dans une liste de suites", "weak suite enabled in a cipher list"),
    "tls_negocie": ("négociation par défaut", "default negotiation"),
    "tls_accepte": ("accepté par le serveur", "accepted by the server"),
    "tls_cert_feuille": ("certificat feuille du serveur", "server leaf certificate"),
    "tls_cert_signature": ("signature du certificat feuille", "leaf certificate signature"),
    "tls_classique_seul": ("échange de clés classique uniquement", "classical key exchange only"),
    "tls_cert_non_verifie": ("certificat non vérifié", "certificate not verified"),
    "ssh_cle_publique": ("clé publique SSH", "SSH public key"),
}


def classe_de(famille: str) -> str:
    return FAMILLES[famille]


@dataclass
class Algo:
    """Algorithme résolu : une famille du contrat plus ses paramètres visibles."""

    famille: str
    nom: str
    primitive: str = "unknown"  # énumération CycloneDX 1.6
    taille: int | None = None
    courbe: str | None = None
    mode: str | None = None
    remplissage: str | None = None
    notes: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.famille not in FAMILLES:
            raise ValueError(f"famille hors contrat : {self.famille}")


# ---------------------------------------------------------------------------
# Courbes et hachages
# ---------------------------------------------------------------------------
_COURBES = {
    "P-256": ("P256", "P-256", "SECP256R1", "PRIME256V1", "NISTP256", "CURVEP256", "X9-62-PRIME256V1"),
    "P-384": ("P384", "P-384", "SECP384R1", "NISTP384", "CURVEP384"),
    "P-521": ("P521", "P-521", "SECP521R1", "NISTP521", "CURVEP521"),
    "P-224": ("P224", "P-224", "SECP224R1", "NISTP224"),
    "secp256k1": ("SECP256K1", "P-256K", "P256K"),
    "brainpoolP256r1": ("BRAINPOOLP256R1",),
    "brainpoolP384r1": ("BRAINPOOLP384R1",),
    "brainpoolP512r1": ("BRAINPOOLP512R1",),
}
_COURBE_PAR_ALIAS = {alias: canon for canon, alias_ in _COURBES.items() for alias in alias_}


def courbe_canonique(nom: str | None) -> str | None:
    if not nom:
        return None
    return _COURBE_PAR_ALIAS.get(re.sub(r"[\s_]+", "-", nom.strip()).upper())


def _hachage(k: str) -> Algo | None:
    """k : nom déjà mis en majuscules, « _ » remplacés par « - »."""
    if k == "MD5":
        return Algo("MD5", "MD5", "hash")
    if k in ("SHA1", "SHA-1"):
        return Algo("SHA1", "SHA-1", "hash")
    m = re.fullmatch(r"SHA-?(224|256|384|512)(?:[/-](224|256))?", k)
    if m:
        nom = f"SHA-{m.group(1)}" + (f"/{m.group(2)}" if m.group(2) else "")
        return Algo("SHA2", nom, "hash")
    m = re.fullmatch(r"SHA3-?(224|256|384|512)", k)
    if m:
        return Algo("SHA3", f"SHA3-{m.group(1)}", "hash")
    m = re.fullmatch(r"SHAKE-?(128|256)", k)
    if m:
        return Algo("SHA3", f"SHAKE{m.group(1)}", "xof")
    return None


# ---------------------------------------------------------------------------
# Résolution d'un nom d'algorithme
# ---------------------------------------------------------------------------
_HYBRIDES = [
    (re.compile(r"X25519MLKEM768"), "X25519MLKEM768", []),
    (re.compile(r"(?:SECP256R1|P256)MLKEM768"), "SecP256r1MLKEM768", []),
    (re.compile(r"(?:SECP384R1|P384)MLKEM1024"), "SecP384r1MLKEM1024", []),
    (re.compile(r"X25519KYBER768(?:DRAFT00)?"), "X25519Kyber768Draft00", ["kyber"]),
    (re.compile(r"MLKEM768X25519SHA256"), "mlkem768x25519-sha256", []),
    (re.compile(r"SNTRUP761X25519SHA512(?:@OPENSSH\.COM)?"), "sntrup761x25519-sha512", ["non_nist"]),
]

_TAILLES_MODP = {"1": 768, "2": 1024, "5": 1536, "14": 2048, "15": 3072, "16": 4096, "17": 6144, "18": 8192}
_MODES = {"GCM": "gcm", "CBC": "cbc", "ECB": "ecb", "CCM": "ccm", "CFB": "cfb", "OFB": "ofb", "CTR": "ctr"}
_SIG_CLES = {"RSA": "RSA", "RSAPSS": "RSA", "RSA/PSS": "RSA", "RSAANDMGF1": "RSA", "RSAENCRYPTION": "RSA",
             "ECDSA": "ECDSA", "PLAIN-ECDSA": "ECDSA", "CVC-ECDSA": "ECDSA", "DSA": "DSA"}
_H = r"MD5|SHA-?1|SHA-?224|SHA-?256|SHA-?384|SHA-?512|SHA3-?(?:224|256|384|512)"


def _signature(cle: str, hachage: str) -> list[Algo]:
    h = _hachage(hachage)
    fam = _SIG_CLES[cle]
    pss = cle in ("RSAPSS", "RSA/PSS", "RSAANDMGF1")
    nom_h = h.nom.replace("SHA-", "SHA") if h else hachage
    remplissage = "other" if pss else ("pkcs1v15" if fam == "RSA" else None)
    algos = [Algo(fam, f"{nom_h}with{'RSA/PSS' if pss else fam}", "signature", remplissage=remplissage)]
    if h and h.famille in ("MD5", "SHA1"):
        algos.append(h)
    return algos


def resoudre(nom: str, *, jca: bool = False) -> list[Algo]:
    """Résout un nom d'algorithme en une liste (souvent un seul élément) d'Algo.

    Retourne [] si le nom n'est pas reconnu : on préfère ne rien signaler
    plutôt que de deviner. ``jca`` active les alias propres à Java (« SHA »).
    """
    brut = nom.strip()
    k = re.sub(r"[\s_]+", "-", brut).upper()
    if not k or len(k) > 80:
        return []
    compact = k.replace("-", "")

    for motif, canon, notes in _HYBRIDES:
        if motif.fullmatch(compact):
            return [Algo("HYBRID_KEM", canon, "kem", notes=list(notes))]

    # --- post-quantique -----------------------------------------------------
    m = re.fullmatch(r"(ML-?KEM|KYBER)-?(512|768|1024)?", k)
    if m:
        n = m.group(2)
        return [Algo("ML-KEM", f"ML-KEM-{n}" if n else "ML-KEM", "kem",
                     notes=["kyber"] if m.group(1) == "KYBER" else [])]
    m = re.fullmatch(r"(ML-?DSA|DILITHIUM)-?(44|65|87|2|3|5)?", k)
    if m:
        n = {"2": "44", "3": "65", "5": "87"}.get(m.group(2) or "", m.group(2))
        return [Algo("ML-DSA", f"ML-DSA-{n}" if n else "ML-DSA", "signature",
                     notes=["dilithium"] if m.group(1) == "DILITHIUM" else [])]
    m = re.fullmatch(r"(?:SLH-?DSA|SPHINCS\+?|SPHINCSPLUS)(?:-(SHA2|SHAKE)-?(128|192|256)([SF]))?", k)
    if m:
        if m.group(1):
            return [Algo("SLH-DSA", f"SLH-DSA-{m.group(1)}-{m.group(2)}{m.group(3).lower()}", "signature")]
        return [Algo("SLH-DSA", "SLH-DSA", "signature")]
    m = re.fullmatch(r"(?:FN-?DSA|FALCON)-?(512|1024)?", k)
    if m:
        return [Algo("FN-DSA", f"FN-DSA-{m.group(1)}" if m.group(1) else "FN-DSA", "signature")]

    # --- signatures composées (JCA, OpenSSL, Go, Node) ------------------------
    m = re.fullmatch(rf"({_H})WITH(RSA/PSS|RSAANDMGF1|RSAENCRYPTION|RSA|PLAIN-ECDSA|CVC-ECDSA|ECDSA|DSA)", k)
    if m:
        return _signature(m.group(2), m.group(1))
    m = re.fullmatch(rf"(RSA|ECDSA|DSA)-(?:WITH-)?({_H})", k)
    if m:
        return _signature(m.group(1), m.group(2))
    m = re.fullmatch(rf"({_H})-(RSAPSS|RSA|ECDSA|DSA)", k)
    if m:
        return _signature(m.group(2), m.group(1))

    # --- RSA ------------------------------------------------------------------
    if k in ("RSA", "RSAENCRYPTION", "RSAES-PKCS1-V1-5", "RSA1-5"):
        return [Algo("RSA", "RSA", "pke", remplissage="pkcs1v15" if k in ("RSA1-5", "RSAES-PKCS1-V1-5") else None)]
    if re.fullmatch(r"RSA-OAEP(?:-(?:256|384|512))?|RSAES-OAEP", k):
        return [Algo("RSA", "RSA-OAEP", "pke", remplissage="oaep")]
    if k in ("RSA-PSS", "RSASSA-PSS"):
        return [Algo("RSA", "RSA-PSS", "signature", remplissage="other")]
    if k == "RSASSA-PKCS1-V1-5":
        return [Algo("RSA", "RSASSA-PKCS1-v1_5", "signature", remplissage="pkcs1v15")]
    m = re.fullmatch(r"RSA/(?:ECB|NONE)/([A-Z0-9-]+)", k)
    if m:
        pad = m.group(1)
        if pad.startswith("OAEP"):
            return [Algo("RSA", "RSA-OAEP", "pke", remplissage="oaep")]
        return [Algo("RSA", "RSA", "pke", remplissage="pkcs1v15" if pad.startswith("PKCS1") else "raw")]

    # --- courbes elliptiques ----------------------------------------------------
    if k in ("EC", "ECC"):
        return [Algo("ECDSA", "EC", "signature", notes=["ec_ambigu"])]
    if k == "ECDSA":
        return [Algo("ECDSA", "ECDSA", "signature")]
    if re.fullmatch(r"ECDHE?|ECDH-ES(?:\+A(?:128|192|256)KW)?|ECMQV", k):
        return [Algo("ECDH", "ECDH", "key-agree")]
    if k == "ECIES":
        return [Algo("ECDH", "ECIES", "pke")]
    c = courbe_canonique(k)
    if c:
        return [Algo("ECDSA", f"EC-{c}", "signature", courbe=c, notes=["ec_ambigu"])]
    if k in ("ED25519", "ED448", "EDDSA"):
        nom_e = {"ED25519": "Ed25519", "ED448": "Ed448", "EDDSA": "EdDSA"}[k]
        return [Algo("EDDSA", nom_e, "signature", courbe=nom_e if k != "EDDSA" else None)]
    if k in ("X25519", "X448", "XDH", "CURVE25519"):
        nom_x = {"X25519": "X25519", "CURVE25519": "X25519", "X448": "X448", "XDH": "XDH"}[k]
        return [Algo("X25519_X448", nom_x, "key-agree", courbe=nom_x if nom_x != "XDH" else None)]

    # --- corps finis --------------------------------------------------------------
    if k in ("DH", "DHE", "DIFFIEHELLMAN", "DIFFIE-HELLMAN", "DHX"):
        return [Algo("DH", "DH", "key-agree")]
    m = re.fullmatch(r"FFDHE(2048|3072|4096|6144|8192)", k)
    if m:
        return [Algo("DH", f"DH-{m.group(1)}", "key-agree", taille=int(m.group(1)))]
    m = re.fullmatch(r"MODP-?(1|2|5|14|15|16|17|18)", k)
    if m:
        t = _TAILLES_MODP[m.group(1)]
        return [Algo("DH", f"DH-{t}", "key-agree", taille=t)]
    if k == "DSA":
        return [Algo("DSA", "DSA", "signature")]

    # --- symétrique -------------------------------------------------------------
    if re.fullmatch(r"(?:ID-)?AES(?:-?(?:128|192|256))?(?:[-/][A-Z0-9/-]*)?|AESWRAP(?:PAD)?", k):
        t = re.search(r"AES-?(128|192|256)", k)
        reste = k[3:] if not k.startswith("ID-") else k[6:]
        md = re.search(r"(GCM|CBC|ECB|CCM|CFB|OFB|CTR|XTS|KW|WRAP|SIV|OCB)", reste)
        mode_brut = md.group(1) if md else None
        mode = _MODES.get(mode_brut or "", "other" if mode_brut else None)
        nom_a = "AES" + (f"-{t.group(1)}" if t else "") + (f"-{mode_brut}" if mode_brut else "")
        prim = "ae" if mode_brut in ("GCM", "CCM", "SIV", "OCB") else "block-cipher"
        return [Algo("AES", nom_a, prim, taille=int(t.group(1)) if t else None, mode=mode)]
    if re.fullmatch(r"X?CHACHA20-?POLY1305(?:@OPENSSH\.COM)?", k):
        return [Algo("CHACHA20", "ChaCha20-Poly1305", "ae", taille=256)]
    if k == "CHACHA20":
        return [Algo("CHACHA20", "ChaCha20", "stream-cipher", taille=256)]
    if re.fullmatch(r"DESEDE3?(?:/.*)?|TRIPLEDES|3DES(?:-[A-Z]+)?|DES-EDE3?(?:-(?:CBC|ECB|CFB|OFB))?|DES3|TDEA", k):
        return [Algo("3DES", "3DES", "block-cipher")]
    if re.fullmatch(r"DES(?:/.*)?|DES-(?:CBC|ECB|CFB|OFB)", k):
        return [Algo("DES", "DES", "block-cipher")]
    if re.fullmatch(r"RC4(?:-[A-Z0-9-]+)?|ARCFOUR(?:128|256)?|ARC4", k):
        return [Algo("RC4", "RC4", "stream-cipher")]

    # --- hachage, MAC, KDF --------------------------------------------------------
    h = _hachage(k) or (_hachage("SHA1") if jca and k == "SHA" else None)
    if h:
        return [h]
    m = re.fullmatch(r"HMAC-?(.+)", k)
    if m:
        h = _hachage(m.group(1)) or (_hachage("SHA1") if m.group(1) == "SHA" else None)
        if h:
            return [Algo(h.famille, f"HMAC-{h.nom}", "mac")]
        return []
    m = re.fullmatch(r"PBKDF2(?:WITH)?HMAC-?(.+)", compact)
    if m:
        h = _hachage(m.group(1))
        if h:
            return [Algo(h.famille, f"PBKDF2-HMAC-{h.nom}", "kdf")]
        return []

    # --- protocoles -----------------------------------------------------------------
    if re.fullmatch(r"SSLV?3(?:\.0)?", k):
        return [Algo("TLS_LEGACY", "SSL 3.0", "other")]
    if re.fullmatch(r"TLSV?1(?:[.-]0)?|TLSV?10", k):
        return [Algo("TLS_LEGACY", "TLS 1.0", "other")]
    if re.fullmatch(r"TLSV?1[.-]1|TLSV?11", k):
        return [Algo("TLS_LEGACY", "TLS 1.1", "other")]
    m = re.fullmatch(r"TLSV?1[.-]([23])|TLSV?1([23])", k)
    if m:
        return [Algo("TLS_SUITE", f"TLS 1.{m.group(1) or m.group(2)}", "other")]
    if re.fullmatch(r"TLS-[A-Z0-9-]+-WITH-[A-Z0-9-]+|TLS-(?:AES-128-GCM-SHA256|AES-256-GCM-SHA384|CHACHA20-POLY1305-SHA256|AES-128-CCM(?:-8)?-SHA256)", k):
        return [Algo("TLS_SUITE", brut.replace("-", "_").upper(), "other")]
    return []


# ---------------------------------------------------------------------------
# Algorithmes JOSE / JWT
# ---------------------------------------------------------------------------
def resoudre_jwt(nom: str) -> list[Algo]:
    n = nom.strip()
    m = re.fullmatch(r"RS(256|384|512)", n)
    if m:
        return [Algo("RSA", n, "signature", remplissage="pkcs1v15")]
    m = re.fullmatch(r"PS(256|384|512)", n)
    if m:
        return [Algo("RSA", n, "signature", remplissage="other")]
    courbes = {"ES256": "P-256", "ES384": "P-384", "ES512": "P-521", "ES256K": "secp256k1"}
    if n in courbes:
        return [Algo("ECDSA", n, "signature", courbe=courbes[n])]
    if n in ("EdDSA", "Ed25519", "Ed448"):
        return [Algo("EDDSA", n, "signature", courbe=n if n != "EdDSA" else None)]
    if re.fullmatch(r"HS(256|384|512)", n):
        return [Algo("SHA2", n, "mac")]
    if n in ("RSA-OAEP", "RSA-OAEP-256", "RSA1_5"):
        return [Algo("RSA", n, "pke", remplissage="oaep" if "OAEP" in n else "pkcs1v15")]
    if re.fullmatch(r"ECDH-ES(?:\+A(?:128|192|256)KW)?", n):
        return [Algo("ECDH", n, "key-agree")]
    m = re.fullmatch(r"ML-DSA-(44|65|87)", n)
    if m:
        return [Algo("ML-DSA", n, "signature")]
    return []


NOMS_JWT = re.compile(r"^(?:RS|PS|ES|HS)(?:256|384|512)$|^ES256K$|^EdDSA$|^Ed(?:25519|448)$|^RSA-OAEP(?:-256)?$|^RSA1_5$|^ECDH-ES(?:\+A(?:128|192|256)KW)?$|^ML-DSA-(?:44|65|87)$")


# ---------------------------------------------------------------------------
# Niveaux de sécurité (CycloneDX) et OID
# ---------------------------------------------------------------------------
_CLASSIQUE_TAILLE = {1024: 80, 2048: 112, 3072: 128, 7680: 192, 15360: 256}  # NIST SP 800-57
_CLASSIQUE_COURBE = {"P-224": 112, "P-256": 128, "secp256k1": 128, "brainpoolP256r1": 128, "Ed25519": 128,
                     "X25519": 128, "P-384": 192, "brainpoolP384r1": 192, "P-521": 256, "brainpoolP512r1": 256,
                     "Ed448": 224, "X448": 224}


def niveau_classique(a: Algo) -> int | None:
    if a.famille in ("RSA", "DH", "DSA") and a.taille in _CLASSIQUE_TAILLE:
        return _CLASSIQUE_TAILLE[a.taille]
    if a.courbe in _CLASSIQUE_COURBE:
        return _CLASSIQUE_COURBE[a.courbe]
    if a.famille == "AES" and a.taille in (128, 192, 256):
        return a.taille
    if a.famille == "3DES":
        return 112
    return None


def niveau_quantique(a: Algo) -> int | None:
    """Catégorie NIST de sécurité post-quantique (0 = aucune), quand elle se déduit."""
    classe = FAMILLES[a.famille]
    if classe == "vulnerable_shor" or a.famille in ("MD5", "SHA1", "DES", "3DES", "RC4"):
        return 0
    chiffres = re.findall(r"\d+", a.nom)
    if a.famille == "ML-KEM":
        return {"512": 1, "768": 3, "1024": 5}.get(chiffres[-1] if chiffres else "")
    if a.famille == "ML-DSA":
        return {"44": 2, "65": 3, "87": 5}.get(chiffres[-1] if chiffres else "")
    if a.famille == "SLH-DSA":
        m = re.search(r"-(128|192|256)[sf]$", a.nom)
        return {"128": 1, "192": 3, "256": 5}.get(m.group(1)) if m else None
    if a.famille == "FN-DSA":
        return {"512": 1, "1024": 5}.get(chiffres[-1] if chiffres else "")
    if a.famille == "HYBRID_KEM":
        if "MLKEM768" in a.nom.upper():
            return 3
        if "MLKEM1024" in a.nom.upper():
            return 5
        return None
    if a.famille == "AES":
        return {128: 1, 192: 3, 256: 5}.get(a.taille or 0)
    if a.famille == "CHACHA20":
        return 5
    if a.primitive == "hash" and a.nom in ("SHA-256", "SHA3-256"):
        return 2
    if a.primitive == "hash" and a.nom in ("SHA-384", "SHA3-384"):
        return 4
    return None


OID_PAR_NOM = {
    "MD5": "1.2.840.113549.2.5", "SHA-1": "1.3.14.3.2.26",
    "SHA-224": "2.16.840.1.101.3.4.2.4", "SHA-256": "2.16.840.1.101.3.4.2.1",
    "SHA-384": "2.16.840.1.101.3.4.2.2", "SHA-512": "2.16.840.1.101.3.4.2.3",
    "SHA3-224": "2.16.840.1.101.3.4.2.7", "SHA3-256": "2.16.840.1.101.3.4.2.8",
    "SHA3-384": "2.16.840.1.101.3.4.2.9", "SHA3-512": "2.16.840.1.101.3.4.2.10",
    "Ed25519": "1.3.101.112", "Ed448": "1.3.101.113", "X25519": "1.3.101.110", "X448": "1.3.101.111",
    "ML-KEM-512": "2.16.840.1.101.3.4.4.1", "ML-KEM-768": "2.16.840.1.101.3.4.4.2",
    "ML-KEM-1024": "2.16.840.1.101.3.4.4.3", "ML-DSA-44": "2.16.840.1.101.3.4.3.17",
    "ML-DSA-65": "2.16.840.1.101.3.4.3.18", "ML-DSA-87": "2.16.840.1.101.3.4.3.19",
    "AES-128-CBC": "2.16.840.1.101.3.4.1.2", "AES-256-CBC": "2.16.840.1.101.3.4.1.42",
    "AES-128-GCM": "2.16.840.1.101.3.4.1.6", "AES-256-GCM": "2.16.840.1.101.3.4.1.46",
}


def oid_de(a: Algo) -> str | None:
    if a.nom in OID_PAR_NOM:
        return OID_PAR_NOM[a.nom]
    if a.famille == "RSA" and re.fullmatch(r"RSA(-\d+)?", a.nom):
        return "1.2.840.113549.1.1.1"
    return None


def nom_avec_taille(a: Algo) -> str:
    """Ajoute taille/courbe au nom quand elles sont connues (« RSA » -> « RSA-2048 »)."""
    nom = a.nom
    if a.taille and a.famille in ("RSA", "DH", "DSA") and nom in ("RSA", "DH", "DSA", "RSA-OAEP", "RSA-PSS"):
        return f"{nom}-{a.taille}"
    if a.courbe and a.famille in ("ECDSA", "ECDH") and nom in ("EC", "ECDSA", "ECDH"):
        return f"{nom}-{a.courbe}"
    if a.taille and a.famille == "AES" and nom.startswith("AES") and not re.search(r"\d{3}", nom):
        return nom.replace("AES", f"AES-{a.taille}", 1)
    return nom
