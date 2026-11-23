"""Table des règles par expressions régulières (Java, Go, JS/TS, C/C++,
configurations TLS et SSH, repli texte pour le Python illisible).

Chaque règle a un identifiant stable et une description courte. Les motifs
visent des appels d'API ou des directives précises, jamais un simple mot :
« rsa » dans un identifiant quelconque ne déclenche rien.
"""
from __future__ import annotations

import bisect
import re
from dataclasses import dataclass
from typing import Callable

from .familles import NOMS_JWT, Algo, courbe_canonique, resoudre, resoudre_jwt
from .modele import Detection, enregistrer
from .pem import resoudre_type_ssh

Liste = Callable[[str], list[tuple[Algo, dict]]]


@dataclass(frozen=True)
class Regle:
    id: str
    langages: frozenset[str]
    description: str
    motif: re.Pattern
    algo: str | None = None  # nom fixe quand le motif n'a pas de groupe « algo »
    resolveur: Callable[[str], list[Algo]] = resoudre
    liste: Liste | None = None  # traite le groupe « liste » (suites, groupes, versions, JWT)
    confiance: str = "elevee"
    fonctions: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    ec_vers: str | None = None  # famille à retenir pour une clé EC ambiguë
    extraire: tuple[tuple[str, re.Pattern], ...] = ()  # (taille|courbe|confiance, motif)
    fenetre: tuple[int, int] = (0, 0)  # lignes avant / après pour « extraire »
    hachage_signature: bool = False  # createSign('SHA256') : la clé n'est pas visible


REGLES: list[Regle] = []


def _r(id_: str, langages: str, description: str, motif: str, flags: int = 0, **kw) -> None:
    enregistrer(id_, langages, description)
    REGLES.append(Regle(id_, frozenset(langages.split(",")), description, re.compile(motif, flags), **kw))


def _a(famille: str, nom: str, primitive: str, **kw) -> Callable[[str], list[Algo]]:
    return lambda _n: [Algo(famille, nom, primitive, **kw)]


def _carte(table: dict[str, Callable[[], Algo] | str], resolveur=resoudre) -> Callable[[str], list[Algo]]:
    def f(nom: str) -> list[Algo]:
        v = table.get(nom)
        if v is None:
            return []
        return resolveur(v) if isinstance(v, str) else [v()]
    return f


def _A(famille: str, nom: str, primitive: str, **kw) -> Callable[[], Algo]:
    return lambda: Algo(famille, nom, primitive, **kw)


# ---------------------------------------------------------------------------
# Listes (suites TLS, groupes, versions, algorithmes JWT, algorithmes SSH)
# ---------------------------------------------------------------------------
def _jetons(chaine: str) -> list[str]:
    return [j for j in re.split(r"[\s,:;\[\]'\"()]+", chaine) if j]


def suites_faibles(chaine: str) -> list[Algo]:
    """Suites faibles réellement activées dans une liste OpenSSL/IANA (les « !x » et « -x » sont ignorés)."""
    vus: dict[str, Algo] = {}
    for j in _jetons(chaine):
        if j[0] in "!-":
            continue
        u = j.upper().replace("_", "-")
        if "RC4" in u:
            vus.setdefault("RC4", Algo("RC4", "RC4", "stream-cipher"))
        if re.search(r"DES-CBC3|3DES|DES-EDE3|DES-EDE", u):
            vus.setdefault("3DES", Algo("3DES", "3DES", "block-cipher"))
        elif re.search(r"(?:^|-)DES(?:-CBC)?(?:-|$)", u):
            vus.setdefault("DES", Algo("DES", "DES", "block-cipher"))
        if re.search(r"(?:^|-)MD5(?:-|$)", u):
            vus.setdefault("MD5", Algo("MD5", "MD5", "hash"))
    for a in vus.values():
        a.notes.append("suite_faible")
    return list(vus.values())


def _liste_suites(chaine: str) -> list[tuple[Algo, dict]]:
    chaine = chaine.strip().rstrip(";").strip("'\"")
    noms = [j for j in _jetons(chaine) if re.fullmatch(r"TLS_[A-Z0-9_]+", j)]
    res = [(Algo("TLS_SUITE", "TLS", "other", notes=["tls_config"]), {"suites": noms or [chaine]})]
    return res + [(a, {}) for a in suites_faibles(chaine)]


def _liste_groupes(chaine: str) -> list[tuple[Algo, dict]]:
    res = []
    for j in _jetons(chaine.rstrip(";")):
        for a in resoudre(j.lstrip("?*")):
            if "ec_ambigu" in a.notes:
                a.famille, a.nom, a.primitive, a.notes = "ECDH", f"ECDH-{a.courbe}", "key-agree", []
            if a.famille in ("HYBRID_KEM", "ML-KEM", "X25519_X448", "ECDH", "DH"):
                res.append((a, {}))
    return res


def _liste_versions(chaine: str, apache: bool = False) -> list[tuple[Algo, dict]]:
    jetons = _jetons(chaine)
    retires = {j[1:].upper() for j in jetons if j[0] in "-!"}
    actifs = [j.lstrip("+") for j in jetons if j[0] not in "-!"]
    if apache and any(j.lower() == "all" for j in actifs):  # « all » = TLS 1.0 à 1.3 (et SSLv3 si compilé)
        actifs += ["TLSv1", "TLSv1.1", "TLSv1.2", "TLSv1.3"]
    res, vus = [], set()
    for j in actifs:
        if j.upper() in retires:
            continue
        for a in resoudre(j):
            if a.famille in ("TLS_LEGACY", "TLS_SUITE") and a.nom not in vus:
                vus.add(a.nom)
                res.append((a, {"version_tls": a.nom}))
    return res


def _liste_jwt(chaine: str) -> list[tuple[Algo, dict]]:
    noms = re.findall(r"['\"]([^'\"]+)['\"]", chaine)
    return [(a, {}) for n in noms if NOMS_JWT.match(n) for a in resoudre_jwt(n)]


def resoudre_ssh(nom: str) -> list[Algo]:
    t = nom.strip().lower()
    a = resoudre_type_ssh(t)
    if a:
        return [a]
    m = re.fullmatch(r"diffie-hellman-group(1|14|15|16|17|18)-(sha1|sha256|sha512)", t)
    if m:
        taille = {"1": 1024, "14": 2048, "15": 3072, "16": 4096, "17": 6144, "18": 8192}[m.group(1)]
        dh = [Algo("DH", f"DH-{taille}", "key-agree", taille=taille)]
        return dh + ([Algo("SHA1", "SHA-1", "hash")] if m.group(2) == "sha1" else [])
    if t.startswith("diffie-hellman-group-exchange-"):
        return [Algo("DH", "DH", "key-agree")] + ([Algo("SHA1", "SHA-1", "hash")] if t.endswith("sha1") else [])
    if t in ("curve25519-sha256", "curve25519-sha256@libssh.org"):
        return [Algo("X25519_X448", "X25519", "key-agree", courbe="X25519")]
    m = re.fullmatch(r"ecdh-sha2-nistp(256|384|521)", t)
    if m:
        return [Algo("ECDH", f"ECDH-P-{m.group(1)}", "key-agree", courbe=f"P-{m.group(1)}")]
    m = re.fullmatch(r"hmac-(sha1|sha2-256|sha2-512|md5)(?:-96)?(?:-etm@openssh\.com)?", t)
    if m:
        return resoudre("HMAC-" + {"sha2-256": "SHA256", "sha2-512": "SHA512"}.get(m.group(1), m.group(1)))
    return resoudre(t.replace("@openssh.com", ""))


def _liste_ssh(chaine: str) -> list[tuple[Algo, dict]]:
    return [(a, {}) for j in chaine.split(",") if j for a in resoudre_ssh(j)]


# ---------------------------------------------------------------------------
# Java / Kotlin
# ---------------------------------------------------------------------------
_JCA = {
    "KeyPairGenerator": ("keygen",), "KeyGenerator": ("keygen",), "Cipher": ("encrypt", "decrypt"),
    "Signature": ("sign", "verify"), "MessageDigest": ("digest",), "KeyAgreement": ("keyderive",),
    "Mac": ("tag",), "KEM": ("encapsulate", "decapsulate"), "SecretKeyFactory": ("keyderive",),
    "KeyFactory": ("other",),
}
_EXTRACTION_JCA = (
    ("taille", re.compile(r"\.(?:initialize|init)\(\s*(\d{3,5})\b")),
    ("taille", re.compile(r"RSAKeyGenParameterSpec\(\s*(\d{3,5})")),
    ("courbe", re.compile(r"(?:ECGenParameterSpec|NamedParameterSpec)\(\s*\"([^\"]+)\"")),
)
for _cls, _fn in _JCA.items():
    _r(f"java-jca-{_cls.lower()}", "java,kotlin", f"JCA : {_cls}.getInstance(\"…\") (algorithme lu, taille/courbe dans les lignes suivantes)",
       rf"\b{_cls}\.getInstance\(\s*\"(?P<algo>[^\"]+)\"", resolveur=lambda n: resoudre(n, jca=True),
       fonctions=_fn, extraire=_EXTRACTION_JCA if _cls in ("KeyPairGenerator", "KeyGenerator") else (), fenetre=(0, 8))


def _tls_generique(n: str) -> list[Algo]:
    return resoudre(n) or ([Algo("TLS_SUITE", "TLS", "other")] if n.upper() in ("TLS", "SSL", "DEFAULT") else [])


_r("java-sslcontext", "java,kotlin", "JSSE : SSLContext.getInstance(\"TLS…\")",
   r"\bSSLContext\.getInstance\(\s*\"(?P<algo>[^\"]+)\"", resolveur=_tls_generique)
_r("java-tls-protocole", "java,kotlin", "JSSE : chaîne de protocole \"SSLv3\" / \"TLSv1.x\" (setEnabledProtocols…)",
   r"\"(?P<algo>SSLv3|TLSv1(?:\.[0-3])?)\"", confiance="moyenne")

_BC = {
    "RSAKeyPairGenerator": "RSA", "RSAEngine": "RSA", "RSABlindedEngine": "RSA", "RSADigestSigner": "RSA",
    "OAEPEncoding": "RSA-OAEP", "PSSSigner": "RSA-PSS", "ECKeyPairGenerator": "EC", "ECDSASigner": "ECDSA",
    "ECDHBasicAgreement": "ECDH", "ECDHCBasicAgreement": "ECDH", "Ed25519Signer": "Ed25519",
    "Ed25519KeyPairGenerator": "Ed25519", "Ed448Signer": "Ed448", "Ed448KeyPairGenerator": "Ed448",
    "X25519Agreement": "X25519", "X25519KeyPairGenerator": "X25519", "X448Agreement": "X448",
    "DHBasicAgreement": "DH", "DHKeyPairGenerator": "DH", "DHParametersGenerator": "DH", "DSASigner": "DSA",
    "DSAKeyPairGenerator": "DSA", "AESEngine": "AES", "AESFastEngine": "AES", "AESLightEngine": "AES",
    "DESedeEngine": "3DES", "DESEngine": "DES", "RC4Engine": "RC4", "ChaCha20Poly1305": "ChaCha20-Poly1305",
    "ChaChaEngine": "ChaCha20", "ChaCha7539Engine": "ChaCha20", "MD5Digest": "MD5", "SHA1Digest": "SHA-1",
    "SHA224Digest": "SHA-224", "SHA256Digest": "SHA-256", "SHA384Digest": "SHA-384", "SHA512Digest": "SHA-512",
    "SHA3Digest": _A("SHA3", "SHA3", "hash"), "SHAKEDigest": _A("SHA3", "SHAKE", "xof"),
    "MLKEMKeyPairGenerator": "ML-KEM", "MLKEMGenerator": "ML-KEM", "MLKEMExtractor": "ML-KEM",
    "MLDSASigner": "ML-DSA", "MLDSAKeyPairGenerator": "ML-DSA", "SLHDSASigner": "SLH-DSA",
    "SLHDSAKeyPairGenerator": "SLH-DSA", "FalconSigner": "FN-DSA", "FalconKeyPairGenerator": "FN-DSA",
    "KyberKeyPairGenerator": "Kyber", "DilithiumSigner": "Dilithium", "SPHINCSPlusSigner": "SPHINCSPlus",
}
_BC_CLASSES = "|".join(sorted(_BC, key=len, reverse=True))
_r("java-bouncycastle-new", "java,kotlin", "Bouncy Castle : instanciation d'une classe d'algorithme (new RSAEngine()…)",
   rf"\bnew\s+(?P<algo>{_BC_CLASSES})\s*\(", resolveur=_carte(_BC))
_r("java-bouncycastle-import", "java,kotlin", "Bouncy Castle : import d'une classe d'algorithme",
   rf"^\s*import\s+org\.bouncycastle\.[\w.]*?\.(?P<algo>{_BC_CLASSES})\s*;", re.M, resolveur=_carte(_BC),
   confiance="moyenne", notes=("import",))
_BC_PQC = {"mlkem": "ML-KEM", "kyber": "Kyber", "crystals.kyber": "Kyber", "mldsa": "ML-DSA", "dilithium": "Dilithium",
           "crystals.dilithium": "Dilithium", "slhdsa": "SLH-DSA", "sphincsplus": "SPHINCSPlus", "falcon": "FN-DSA"}
_r("java-bouncycastle-pqc-paquet", "java,kotlin", "Bouncy Castle : paquet post-quantique importé (org.bouncycastle.pqc.*)",
   r"^\s*import\s+org\.bouncycastle\.pqc\.(?:crypto|jcajce\.provider|jcajce\.spec|jcajce\.interfaces)\.(?P<algo>crystals\.kyber|crystals\.dilithium|mlkem|mldsa|slhdsa|sphincsplus|falcon|kyber|dilithium)\b",
   re.M, resolveur=_carte(_BC_PQC), confiance="moyenne", notes=("import",))
_r("java-bouncycastle-pqc-spec", "java,kotlin", "Bouncy Castle / JCA : jeu de paramètres PQC (MLKEMParameterSpec.ml_kem_768…)",
   r"\b(?:MLKEM|MLDSA|Kyber|Dilithium)ParameterSpec\.(?P<algo>ml_kem_(?:512|768|1024)|ml_dsa_(?:44|65|87)|kyber(?:512|768|1024)|dilithium[235])\b")
_AUTH0 = {"RSA256": "RS256", "RSA384": "RS384", "RSA512": "RS512", "ECDSA256": "ES256", "ECDSA384": "ES384",
          "ECDSA512": "ES512", "HMAC256": "HS256", "HMAC384": "HS384", "HMAC512": "HS512"}
_r("java-jwt-algorithme", "java,kotlin", "jjwt / Nimbus / auth0 : constante d'algorithme JWT (SignatureAlgorithm.RS256…)",
   r"\b(?:SignatureAlgorithm|JWSAlgorithm|JWEAlgorithm|Jwts\.SIG|Jwts\.KEY)\.(?P<algo>[RPE]S(?:256|384|512)|HS(?:256|384|512)|ES256K|EdDSA|Ed25519|RSA_OAEP_256|RSA_OAEP|RSA1_5)\b",
   resolveur=lambda n: resoudre_jwt(n.replace("RSA_OAEP_256", "RSA-OAEP-256").replace("RSA_OAEP", "RSA-OAEP")),
   fonctions=("sign", "verify"))
_r("java-auth0-jwt", "java,kotlin", "auth0 java-jwt : Algorithm.RSA256(…), ECDSA256(…), HMAC256(…)",
   r"\bAlgorithm\.(?P<algo>RSA(?:256|384|512)|ECDSA(?:256|384|512)|HMAC(?:256|384|512))\s*\(",
   resolveur=_carte(_AUTH0, resoudre_jwt), fonctions=("sign", "verify"))

# ---------------------------------------------------------------------------
# Go
# ---------------------------------------------------------------------------
_GO_IMPORTS = {
    "crypto/rsa": "RSA", "crypto/ecdsa": "ECDSA", "crypto/ed25519": "Ed25519", "crypto/ecdh": "ECDH",
    "crypto/elliptic": "EC", "crypto/mlkem": "ML-KEM", "crypto/md5": "MD5", "crypto/sha1": "SHA-1",
    "crypto/des": "DES", "crypto/rc4": "RC4", "crypto/dsa": "DSA", "crypto/aes": "AES", "crypto/sha256": "SHA-256",
    "crypto/sha512": "SHA-512", "crypto/sha3": _A("SHA3", "SHA3", "hash"),
    "golang.org/x/crypto/chacha20poly1305": "ChaCha20-Poly1305", "golang.org/x/crypto/curve25519": "X25519",
    "golang.org/x/crypto/sha3": _A("SHA3", "SHA3", "hash"), "golang.org/x/crypto/ed25519": "Ed25519",
}
_r("go-import-crypto", "go", "Go : import d'un paquet d'algorithme (crypto/rsa, crypto/md5, crypto/mlkem…)",
   r"\"(?P<algo>crypto/(?:rsa|ecdsa|ed25519|ecdh|elliptic|mlkem|md5|sha1|des|rc4|dsa|aes|sha256|sha512|sha3)|golang\.org/x/crypto/(?:chacha20poly1305|curve25519|sha3|ed25519))\"",
   resolveur=_carte(_GO_IMPORTS), confiance="moyenne", notes=("import",))
_r("go-rsa-generatekey", "go", "Go : rsa.GenerateKey(rand, bits) (taille lue)",
   r"\brsa\.GenerateKey\(\s*[\w.]+\s*,\s*(?P<taille>\d{3,5})?", algo="RSA", fonctions=("keygen",))
_GO_RSA = {"EncryptOAEP": "RSA-OAEP", "DecryptOAEP": "RSA-OAEP", "EncryptPKCS1v15": "RSAES-PKCS1-v1_5",
           "DecryptPKCS1v15": "RSAES-PKCS1-v1_5", "SignPKCS1v15": "RSASSA-PKCS1-v1_5",
           "VerifyPKCS1v15": "RSASSA-PKCS1-v1_5", "SignPSS": "RSA-PSS", "VerifyPSS": "RSA-PSS"}
_r("go-rsa-operation", "go", "Go : rsa.EncryptOAEP / SignPKCS1v15 / SignPSS…",
   rf"\brsa\.(?P<algo>{'|'.join(_GO_RSA)})\(", resolveur=_carte(_GO_RSA))
_r("go-ecdsa", "go", "Go : ecdsa.GenerateKey(elliptic.Pxxx()), ecdsa.Sign/Verify",
   r"\becdsa\.(?:GenerateKey\(\s*elliptic\.(?P<courbe>P224|P256|P384|P521)\(\)|(?:SignASN1|Sign|VerifyASN1|Verify)\b)",
   algo="ECDSA", fonctions=("sign", "verify"))
_r("go-ed25519", "go", "Go : ed25519.GenerateKey / Sign / Verify",
   r"\bed25519\.(?:GenerateKey|Sign|Verify|NewKeyFromSeed)\(", algo="Ed25519", fonctions=("sign", "verify"))
_r("go-ecdh", "go", "Go : ecdh.X25519() / ecdh.P256()…",
   r"\becdh\.(?P<algo>X25519|P256|P384|P521)\(\)", ec_vers="ECDH", fonctions=("keyderive",))
_r("go-elliptic", "go", "Go : courbe elliptic.P256()… (usage ECDSA ou ECDH selon le contexte)",
   r"\belliptic\.(?P<algo>P224|P256|P384|P521)\(\)", confiance="moyenne")
_r("go-mlkem", "go", "Go : crypto/mlkem GenerateKey768/1024, NewEncapsulationKey…",
   r"\bmlkem\.(?:GenerateKey|NewDecapsulationKey|NewEncapsulationKey)(?P<algo>768|1024)\(",
   resolveur=lambda n: resoudre(f"ML-KEM-{n}"), fonctions=("encapsulate", "decapsulate"))
_GO_HASH = {"md5": "MD5", "sha1": "SHA-1", "sha256": "SHA-256", "sha512": "SHA-512"}


def _go_hachage(n: str) -> list[Algo]:
    paquet, fn = n.split(".")
    for motif, nom in (("224", "SHA-224"), ("384", "SHA-384"), ("512_256", "SHA-512/256"), ("512_224", "SHA-512/224")):
        if paquet in ("sha256", "sha512") and motif in fn:
            return resoudre(nom)
    return resoudre(_GO_HASH[paquet])


_r("go-hachage", "go", "Go : md5/sha1/sha256/sha512 .New() / .Sum…()",
   r"\b(?P<algo>(?:md5|sha1|sha256|sha512)\.(?:New\w*|Sum\w*))\(", resolveur=_go_hachage, fonctions=("digest",))
_r("go-des", "go", "Go : des.NewCipher / des.NewTripleDESCipher",
   r"\bdes\.(?P<algo>NewTripleDESCipher|NewCipher)\(",
   resolveur=_carte({"NewTripleDESCipher": "3DES", "NewCipher": "DES"}), fonctions=("encrypt", "decrypt"))
_r("go-rc4", "go", "Go : rc4.NewCipher", r"\brc4\.NewCipher\(", algo="RC4", fonctions=("encrypt", "decrypt"))
_r("go-aes", "go", "Go : aes.NewCipher (taille de clé connue à l'exécution)", r"\baes\.NewCipher\(", algo="AES",
   fonctions=("encrypt", "decrypt"))
_r("go-chacha20poly1305", "go", "Go : chacha20poly1305.New / NewX", r"\bchacha20poly1305\.NewX?\(",
   algo="ChaCha20-Poly1305", fonctions=("encrypt", "decrypt"))
_r("go-tls-groupe", "go", "Go crypto/tls : groupe d'échange de clés (tls.X25519MLKEM768, tls.X25519, tls.CurveP256…)",
   r"\btls\.(?P<algo>X25519MLKEM768|X25519|CurveP256|CurveP384|CurveP521)\b", ec_vers="ECDH", fonctions=("keyderive",))
_GO_TLS_VERSIONS = {"VersionSSL30": "SSLv3", "VersionTLS10": "TLSv1.0", "VersionTLS11": "TLSv1.1",
                    "VersionTLS12": "TLSv1.2", "VersionTLS13": "TLSv1.3"}
_r("go-tls-version", "go", "Go crypto/tls : tls.VersionTLS10 / VersionTLS11 / VersionSSL30…",
   r"\btls\.(?P<algo>VersionSSL30|VersionTLS1[0-3])\b", resolveur=_carte(_GO_TLS_VERSIONS))
_r("go-tls-suite", "go", "Go crypto/tls : constante de suite tls.TLS_…",
   r"\btls\.(?P<algo>TLS_[A-Z0-9_]+_WITH_[A-Z0-9_]+|TLS_AES_(?:128|256)_GCM_SHA(?:256|384)|TLS_CHACHA20_POLY1305_SHA256)\b")
_r("go-jwt", "go", "golang-jwt : jwt.SigningMethodRS256…",
   r"\bjwt\.SigningMethod(?P<algo>[RPE]S(?:256|384|512)|HS(?:256|384|512)|EdDSA)\b", resolveur=resoudre_jwt,
   fonctions=("sign", "verify"))

# ---------------------------------------------------------------------------
# JavaScript / TypeScript
# ---------------------------------------------------------------------------
JS = "javascript,typescript"
_EXTRACTION_JS = (
    ("taille", re.compile(r"\bmodulusLength\s*:\s*(\d{3,5})")),
    ("courbe", re.compile(r"\bnamedCurve\s*:\s*['\"]([^'\"]+)['\"]")),
    ("taille", re.compile(r"\blength\s*:\s*(128|192|256)\b")),
)
_r("js-generatekeypair", JS, "node:crypto : generateKeyPair(Sync)('rsa'|'ec'|'ed25519'…) (taille/courbe lues)",
   r"\bgenerateKeyPair(?:Sync)?\(\s*['\"](?P<algo>rsa|rsa-pss|dsa|ec|ed25519|ed448|x25519|x448|dh)['\"]",
   fonctions=("keygen",), extraire=_EXTRACTION_JS, fenetre=(0, 8))
_r("js-createsign", JS, "node:crypto : createSign / createVerify('RSA-SHA256'…)",
   r"\bcreate(?:Sign|Verify)\(\s*['\"](?P<algo>[^'\"]+)['\"]", fonctions=("sign", "verify"), hachage_signature=True)
_r("js-createhash", JS, "node:crypto : createHash('md5'…)",
   r"\bcreateHash\(\s*['\"](?P<algo>[^'\"]+)['\"]", fonctions=("digest",))
_r("js-createhmac", JS, "node:crypto : createHmac('sha256'…)",
   r"\bcreateHmac\(\s*['\"](?P<algo>[^'\"]+)['\"]", resolveur=lambda n: resoudre("HMAC-" + n), fonctions=("tag",))
_r("js-createcipheriv", JS, "node:crypto : createCipheriv / createDecipheriv('aes-256-gcm'…)",
   r"\bcreate(?:Dec|C)ipher(?:iv)?\(\s*['\"](?P<algo>[^'\"]+)['\"]", fonctions=("encrypt", "decrypt"))
_r("js-createecdh", JS, "node:crypto : createECDH('prime256v1'…)",
   r"\bcreateECDH\(\s*['\"](?P<algo>[^'\"]+)['\"]", ec_vers="ECDH", fonctions=("keyderive",))
_r("js-diffiehellman", JS, "node:crypto : createDiffieHellman(bits) / getDiffieHellman('modp14')",
   r"\b(?:createDiffieHellman(?:Group)?|getDiffieHellman)\(\s*(?:['\"](?P<algo>[^'\"]+)['\"]|(?P<taille>\d{3,5}))?",
   algo="DH", fonctions=("keyderive",))
_r("js-webcrypto-algorithme", JS, "WebCrypto : { name: 'RSA-OAEP' | 'ECDSA' | 'AES-GCM'… } (élevée si subtle.* à proximité)",
   r"\bname\s*:\s*['\"](?P<algo>RSA-OAEP|RSA-PSS|RSASSA-PKCS1-v1_5|ECDSA|ECDH|Ed25519|Ed448|X25519|X448|AES-GCM|AES-CBC|AES-CTR|AES-KW|ML-KEM-(?:512|768|1024)|ML-DSA-(?:44|65|87))['\"]",
   confiance="moyenne",
   extraire=_EXTRACTION_JS + (("confiance", re.compile(r"\bsubtle\.")),), fenetre=(3, 4))
_r("js-webcrypto-digest", JS, "WebCrypto : subtle.digest('SHA-256'…)",
   r"\bsubtle\.digest\(\s*['\"](?P<algo>SHA-1|SHA-256|SHA-384|SHA-512)['\"]", fonctions=("digest",))
_r("js-jwt-options", JS, "jsonwebtoken / jose : algorithm(s): ['RS256'…], alg: 'ES256'",
   r"\b(?:algorithms?|alg)\s*:\s*(?P<liste>\[[^\]]*\]|['\"][^'\"]+['\"])", liste=_liste_jwt, fonctions=("sign", "verify"))
_r("js-tls-version", JS, "node:tls : minVersion / maxVersion / secureProtocol",
   r"\b(?:minVersion|maxVersion|secureProtocol)\s*:\s*['\"](?P<algo>TLSv1(?:\.[0-3])?|SSLv3_method|TLSv1(?:_[123])?_method)['\"]",
   resolveur=lambda n: resoudre(n.removesuffix("_method")))
_r("js-tls-ciphers", JS, "node:tls : ciphers: '…' (inventaire + suites faibles)",
   r"\bciphers\s*:\s*['\"](?P<liste>[^'\"]+)['\"]", liste=_liste_suites)
_r("js-tls-ecdhcurve", JS, "node:tls : ecdhCurve: 'X25519MLKEM768:X25519…'",
   r"\becdhCurve\s*:\s*['\"](?P<liste>[^'\"]+)['\"]", liste=_liste_groupes, fonctions=("keyderive",))

# ---------------------------------------------------------------------------
# C / C++ (OpenSSL)
# ---------------------------------------------------------------------------
C = "c,cpp"
_r("c-evp-pkey-id", C, "OpenSSL : identifiant EVP_PKEY_RSA / EC / ED25519 / X25519 / DH / DSA / ML_KEM…",
   r"\bEVP_PKEY_(?P<algo>RSA_PSS|RSA|EC|ED25519|ED448|X25519|X448|DHX|DH|DSA|ML_KEM_(?:512|768|1024)|ML_DSA_(?:44|65|87))\b",
   confiance="moyenne")
_r("c-evp-pkey-par-nom", C, "OpenSSL 3 : EVP_PKEY_CTX_new_from_name(ctx, \"RSA\"|\"ML-KEM-768\"…)",
   r"\bEVP_PKEY_CTX_new_from_name\(\s*[^,()]*,\s*\"(?P<algo>[^\"]+)\"")
_r("c-evp-pkey-q-keygen", C, "OpenSSL 3 : EVP_PKEY_Q_keygen(…, \"RSA\", 2048) / (…, \"EC\", \"P-256\")",
   r"\bEVP_PKEY_Q_keygen\(\s*[^,()]*,\s*[^,()]*,\s*\"(?P<algo>[^\"]+)\"(?:\s*,\s*(?:\(size_t\)\s*)?(?P<taille>\d{3,5})|\s*,\s*\"(?P<courbe>[^\"]+)\")?",
   fonctions=("keygen",))
_r("c-evp-rsa-bits", C, "OpenSSL : EVP_PKEY_CTX_set_rsa_keygen_bits(ctx, bits)",
   r"\bEVP_PKEY_CTX_set_rsa_keygen_bits\(\s*[^,()]+,\s*(?P<taille>\d{3,5})", algo="RSA", fonctions=("keygen",))
_r("c-evp-ec-courbe", C, "OpenSSL : EVP_PKEY_CTX_set_ec_paramgen_curve_nid(ctx, NID_…)",
   r"\bEVP_PKEY_CTX_set_ec_paramgen_curve_nid\(\s*[^,()]+,\s*NID_(?P<courbe>\w+)", algo="EC", fonctions=("keygen",))
_r("c-evp-chiffre-hachage", C, "OpenSSL : EVP_aes_256_gcm(), EVP_des_ede3_cbc(), EVP_rc4(), EVP_md5(), EVP_sha1()…",
   r"\bEVP_(?P<algo>aes_(?:128|192|256)_(?:cbc|gcm|ecb|ctr|cfb\d*|ofb|ccm|xts|wrap)|des_ede3(?:_cbc|_ecb)?|des_ede(?:_cbc)?|des_(?:cbc|ecb)|rc4(?:_40|_hmac_md5)?|chacha20(?:_poly1305)?|md5|sha1|sha224|sha256|sha384|sha512(?:_224|_256)?|sha3_(?:224|256|384|512)|shake(?:128|256))\s*\(\s*\)")
_r("c-evp-fetch", C, "OpenSSL 3 : EVP_CIPHER_fetch / EVP_MD_fetch / EVP_KEM_fetch…(ctx, \"nom\")",
   r"\bEVP_(?:CIPHER|MD|MAC|KDF|SIGNATURE|KEM|KEYMGMT|KEYEXCH)_fetch\(\s*[^,()]*,\s*\"(?P<algo>[^\"]+)\"")
_r("c-rsa-api", C, "OpenSSL (API historique) : RSA_generate_key(_ex), RSA_public_encrypt, RSA_sign…",
   r"\b(?:RSA_generate_key(?:_ex)?|RSA_new|RSA_public_encrypt|RSA_private_decrypt|RSA_private_encrypt|RSA_public_decrypt|RSA_sign|RSA_verify|PEM_read_bio_RSAPrivateKey|d2i_RSAPrivateKey)\s*\(",
   algo="RSA", extraire=(("taille", re.compile(r"RSA_generate_key_ex\(\s*[^,()]+,\s*(\d{3,5})|RSA_generate_key\(\s*(\d{3,5})")),))
_r("c-ec-key", C, "OpenSSL (API historique) : EC_KEY_new_by_curve_name(NID_…), EC_KEY_generate_key",
   r"\b(?:EC_KEY_new_by_curve_name\(\s*NID_(?P<courbe>\w+)\s*\)|EC_KEY_generate_key\s*\()", algo="EC",
   fonctions=("keygen",))
_r("c-ecdsa-api", C, "OpenSSL (API historique) : ECDSA_sign / ECDSA_do_sign / ECDSA_verify",
   r"\bECDSA_(?:do_)?(?:sign|verify)\s*\(", algo="ECDSA", fonctions=("sign", "verify"))
_r("c-ecdh-api", C, "OpenSSL (API historique) : ECDH_compute_key", r"\bECDH_compute_key\s*\(", algo="ECDH",
   fonctions=("keyderive",))
_r("c-dh-api", C, "OpenSSL (API historique) : DH_new, DH_generate_parameters_ex (taille lue), DH_compute_key",
   r"\b(?:DH_new|DH_generate_key|DH_compute_key|DH_generate_parameters_ex|DH_get_2048_256|DH_get_1024_160)\s*\(",
   algo="DH", fonctions=("keyderive",),
   extraire=(("taille", re.compile(r"DH_generate_parameters_ex\(\s*[^,()]+,\s*(\d{3,5})")),))
_r("c-dsa-api", C, "OpenSSL (API historique) : DSA_new, DSA_generate_parameters_ex (taille lue), DSA_sign",
   r"\b(?:DSA_new|DSA_generate_parameters_ex|DSA_generate_key|DSA_sign|DSA_do_sign)\s*\(", algo="DSA",
   fonctions=("sign",), extraire=(("taille", re.compile(r"DSA_generate_parameters_ex\(\s*[^,()]+,\s*(\d{3,5})")),))
_r("c-hachage-api", C, "OpenSSL (API historique) : MD5(), SHA1(), SHA256_Init()…",
   r"\b(?P<algo>MD5|SHA1|SHA224|SHA256|SHA384|SHA512)(?:_Init|_Update|_Final)?\s*\(", confiance="moyenne",
   fonctions=("digest",))
_C_SYM = {"DES_ede3_cbc_encrypt": "3DES", "DES_ecb3_encrypt": "3DES", "RC4_set_key": "RC4", "RC4": "RC4"}
_r("c-chiffrement-api", C, "OpenSSL (API historique) : DES_*, RC4(), AES_set_encrypt_key (taille lue)",
   r"\b(?P<algo>DES_ede3_cbc_encrypt|DES_ecb3_encrypt|DES_set_key(?:_checked|_unchecked)?|DES_ecb_encrypt|DES_cbc_encrypt|DES_ncbc_encrypt|RC4_set_key|RC4|AES_set_encrypt_key|AES_set_decrypt_key|AES_encrypt|AES_cbc_encrypt)\s*\(",
   resolveur=lambda n: resoudre(_C_SYM.get(n, n.split("_")[0])), fonctions=("encrypt", "decrypt"),
   extraire=(("taille", re.compile(r"AES_set_(?:en|de)crypt_key\(\s*[^,()]+,\s*(128|192|256)")),))
_r("c-ssl-groupes", C, "OpenSSL : SSL_CTX_set1_groups_list(ctx, \"X25519MLKEM768:X25519…\")",
   r"\bSSL(?:_CTX)?_set1_(?:groups|curves)_list\(\s*[^,()]+,\s*\"(?P<liste>[^\"]+)\"", liste=_liste_groupes,
   fonctions=("keyderive",))
_r("c-ssl-suites", C, "OpenSSL : SSL_CTX_set_cipher_list / set_ciphersuites (inventaire + suites faibles)",
   r"\bSSL(?:_CTX)?_set_(?:cipher_list|ciphersuites)\(\s*[^,()]+,\s*\"(?P<liste>[^\"]+)\"", liste=_liste_suites)
_r("c-ssl-methode", C, "OpenSSL : TLSv1_method() / SSLv3_method() / TLSv1_1_method()…",
   r"\b(?P<algo>SSLv3|TLSv1_1|TLSv1_2|TLSv1)_(?:client_|server_)?method\s*\(")
_C_VERSIONS = {"SSL3_VERSION": "SSLv3", "TLS1_VERSION": "TLSv1", "TLS1_1_VERSION": "TLSv1.1",
               "TLS1_2_VERSION": "TLSv1.2", "TLS1_3_VERSION": "TLSv1.3"}
_r("c-ssl-version", C, "OpenSSL : SSL_CTX_set_min/max_proto_version(ctx, TLS1_VERSION…)",
   r"\bSSL(?:_CTX)?_set_(?:min|max)_proto_version\(\s*[^,()]+,\s*(?P<algo>SSL3_VERSION|TLS1_VERSION|TLS1_[123]_VERSION)",
   resolveur=_carte(_C_VERSIONS))

# ---------------------------------------------------------------------------
# Fichiers de configuration (nginx, Apache, HAProxy, OpenSSL, Spring, PostgreSQL…)
# ---------------------------------------------------------------------------
_CLE = r"^[ \t]*(?:[\w-]+\.)*"
_r("cfg-tls-protocoles", "config", "Configuration : directive de protocoles TLS (ssl_protocols, SSLProtocol, MinProtocol…)",
   _CLE + r"(?:ssl_protocols|ssl-protocols|ssl-min-ver|ssl-max-ver|minprotocol|maxprotocol|tls_min_version|tls-min-version|min_tls_version|min-tls-version|ssl_min_protocol_version|enabled-protocols|enabled_protocols|enabledprotocols|sslenabledprotocols|protocols)\b[ \t]*[=:]?[ \t]*(?P<liste>[^\n#]+)",
   re.I | re.M, liste=_liste_versions, notes=("tls_config",))
_r("cfg-apache-sslprotocol", "config", "Apache : SSLProtocol (« all » développé, « -TLSv1 » retiré)",
   r"^[ \t]*SSLProtocol[ \t]+(?P<liste>[^\n#]+)", re.I | re.M, liste=lambda c: _liste_versions(c, apache=True),
   notes=("tls_config",))
_r("cfg-tls-suites", "config", "Configuration : liste de suites TLS (ssl_ciphers, SSLCipherSuite, CipherString…)",
   _CLE + r"(?:ssl_ciphers|sslciphersuite|ciphersuites|cipherstring|ssl-default-bind-ciphers|ssl-default-bind-ciphersuites|ssl-default-server-ciphers|cipher_suites|ciphersuite|ssl_cipher|tls_ciphers|ssl-ciphers|ciphers)\b[ \t]*[=:]?[ \t]*(?P<liste>[^\n#]+)",
   re.I | re.M, liste=_liste_suites)
_r("cfg-tls-groupes", "config", "Configuration : groupes / courbes d'échange de clés (ssl_ecdh_curve, Groups, Curves…)",
   _CLE + r"(?:ssl_ecdh_curve|sslopensslconfcmd[ \t]+(?:curves|groups)|ssl_conf_command[ \t]+groups|groups|curves|ecdhcurve|ecdh-curve|named[-_]?groups|supported[-_]?groups|curve_preferences|curvepreferences)\b[ \t]*[=:]?[ \t]*(?P<liste>[^\n#]+)",
   re.I | re.M, liste=_liste_groupes, notes=("tls_config",), fonctions=("keyderive",))

_r("ssh-kex", "ssh-config", "OpenSSH : KexAlgorithms (hybrides mlkem768x25519 / sntrup761x25519, DH, ECDH)",
   r"^[ \t]*KexAlgorithms[ \t]+[+^]?(?P<liste>[^\s#]+)", re.I | re.M, liste=_liste_ssh, notes=("ssh_config",),
   fonctions=("keyderive",))
_r("ssh-cles-hote", "ssh-config", "OpenSSH : HostKeyAlgorithms / PubkeyAcceptedAlgorithms / CASignatureAlgorithms",
   r"^[ \t]*(?:HostKeyAlgorithms|PubkeyAcceptedAlgorithms|PubkeyAcceptedKeyTypes|CASignatureAlgorithms|HostbasedAcceptedAlgorithms)[ \t]+[+^]?(?P<liste>[^\s#]+)",
   re.I | re.M, liste=_liste_ssh, notes=("ssh_config",), fonctions=("sign", "verify"))
_r("ssh-chiffrements", "ssh-config", "OpenSSH : Ciphers / MACs",
   r"^[ \t]*(?:Ciphers|MACs)[ \t]+[+^]?(?P<liste>[^\s#]+)", re.I | re.M, liste=_liste_ssh, notes=("ssh_config",))
_r("ssh-hostkey-fichier", "ssh-config", "OpenSSH : HostKey …/ssh_host_<type>_key",
   r"^[ \t]*HostKey[ \t]+\S*ssh_host_(?P<algo>rsa|ecdsa|ed25519|dsa)_key", re.I | re.M,
   resolveur=_carte({"rsa": "RSA", "ecdsa": "ECDSA", "ed25519": "Ed25519", "dsa": "DSA"}), confiance="moyenne",
   notes=("ssh_config",))

# ---------------------------------------------------------------------------
# Repli pour le Python que ast ne sait pas lire (Python 2, gabarits…)
# ---------------------------------------------------------------------------
PT = "python-texte"
_r("pyt-hashlib", PT, "Python (repli texte) : hashlib.md5( / sha1( / sha256(…",
   r"\bhashlib\.(?P<algo>md5|sha1|sha224|sha256|sha384|sha512|sha3_(?:224|256|384|512))\(", fonctions=("digest",))
_r("pyt-cle-asymetrique", PT, "Python (repli texte) : rsa.generate_private_key( / RSA.generate( (taille lue)",
   r"\b(?:rsa\.generate_private_key|RSA\.generate)\(", algo="RSA", fonctions=("keygen",),
   extraire=(("taille", re.compile(r"key_size\s*=\s*(\d{3,5})|RSA\.generate\(\s*(\d{3,5})")),))
_r("pyt-chiffrement", PT, "Python (repli texte) : AES.new( / DES.new( / DES3.new( / ARC4.new(",
   r"\b(?P<algo>DES3|DES|ARC4|AES)\.new\(", resolveur=lambda n: resoudre({"DES3": "3DES"}.get(n, n)),
   fonctions=("encrypt", "decrypt"))
_r("pyt-jwt", PT, "Python (repli texte) : algorithm(s)=['RS256'…]",
   r"\balgorithms?\s*=\s*(?P<liste>\[[^\]]*\]|['\"][^'\"]+['\"])", liste=_liste_jwt, fonctions=("sign", "verify"))

# ---------------------------------------------------------------------------
# Application des règles
# ---------------------------------------------------------------------------
_COMMENTAIRES = {"java": ("//", "/*", "*"), "kotlin": ("//", "/*", "*"), "go": ("//", "/*", "*"),
                 "javascript": ("//", "/*", "*"), "typescript": ("//", "/*", "*"), "c": ("//", "/*", "*"),
                 "cpp": ("//", "/*", "*"), "python-texte": ("#",), "config": ("#", ";", "//"),
                 "ssh-config": ("#",)}
_CONFIG = {"config", "ssh-config"}


def _en_commentaire(ligne: str, colonne: int, langage: str) -> bool:
    debut = ligne.lstrip()
    if debut.startswith(_COMMENTAIRES.get(langage, ())):
        return True
    if langage not in _CONFIG and langage != "python-texte":
        return bool(re.search(r"(?<![:\"'\\])//", ligne[:colonne]))
    return False


def _extraire(regle: Regle, lignes: list[str], idx: int) -> dict:
    avant, apres = regle.fenetre
    zone = lignes[max(0, idx - avant): idx + apres + 1]
    res: dict = {}
    for champ, motif in regle.extraire:
        if champ in res:
            continue
        for li in zone:
            m = motif.search(li)
            if m:
                res[champ] = next(g for g in m.groups() if g) if m.groups() else True
                break
    return res


def _completer(a: Algo, taille: str | None, courbe: str | None, ec_vers: str | None) -> Algo:
    if taille and a.taille is None and a.famille in ("RSA", "DH", "DSA", "AES"):
        a.taille = int(taille)
    if courbe and not a.courbe:
        c = courbe_canonique(courbe) or courbe_canonique(courbe.removeprefix("NID_"))
        if c:
            a.courbe = c
            if a.nom == "EC":
                a.nom = f"EC-{c}"
    if ec_vers and "ec_ambigu" in a.notes:
        a.famille = ec_vers
        a.primitive = "key-agree" if ec_vers == "ECDH" else "signature"
        a.notes.remove("ec_ambigu")
        a.nom = f"{ec_vers}-{a.courbe}" if a.courbe else ec_vers
    return a


def appliquer_regles(texte: str, langage: str) -> list[Detection]:
    regles = [r for r in REGLES if langage in r.langages]
    if not regles:
        return []
    lignes = texte.splitlines()
    debuts = [0]
    for li in lignes:
        debuts.append(debuts[-1] + len(li) + 1)
    res: list[Detection] = []
    for regle in regles:
        for m in regle.motif.finditer(texte):
            idx = bisect.bisect_right(debuts, m.start()) - 1
            ligne = lignes[idx] if idx < len(lignes) else ""
            commentaire = _en_commentaire(ligne, m.start() - debuts[idx], langage)
            if commentaire and langage in _CONFIG:
                continue
            groupes = m.groupdict()
            extrait = _extraire(regle, lignes, idx) if regle.extraire else {}
            confiance = "elevee" if extrait.get("confiance") else regle.confiance
            if regle.liste and groupes.get("liste"):
                paires = regle.liste(groupes["liste"])
            else:
                nom = groupes.get("algo") or regle.algo
                paires = [(a, {}) for a in regle.resolveur(nom)] if nom else []
            for a, extra in paires:
                notes = list(regle.notes)
                conf = confiance
                if regle.hachage_signature and a.famille in ("MD5", "SHA1", "SHA2", "SHA3"):
                    notes.append("sig_cle_inconnue")
                    conf = "moyenne"
                if commentaire:
                    notes.append("commentaire")
                    conf = "faible"
                a = _completer(a, groupes.get("taille") or extrait.get("taille"),
                               groupes.get("courbe") or extrait.get("courbe"), regle.ec_vers)
                a.notes.extend(n for n in notes if n not in a.notes)
                res.append(Detection(idx + 1, regle.id, a, conf, regle.fonctions, [], extra))
    return res
