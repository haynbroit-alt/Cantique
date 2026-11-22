"""Analyse des fichiers Python par l'arbre syntaxique (module ``ast``).

L'AST apporte trois gains de précision sur les expressions régulières :
les commentaires et docstrings sont ignorés, les noms sont résolus à partir
des imports (``rsa`` est-il bien ``cryptography...asymmetric.rsa`` ?), et
les tailles de clé passées par mot-clé, par position ou via une constante
de module (``KEY_SIZE = 2048``) sont lues.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass

from .familles import NOMS_JWT, Algo, courbe_canonique, resoudre, resoudre_jwt
from .modele import Detection, enregistrer
from .regles_scan import suites_faibles

L = "python"
R_CRY_RSA = enregistrer("py-cryptography-rsa", L, "cryptography : génération de clé RSA, remplissage OAEP/PSS/PKCS#1 v1.5")
R_CRY_EC = enregistrer("py-cryptography-ec", L, "cryptography : clé EC (courbe lue), ECDSA, ECDH")
R_CRY_ED = enregistrer("py-cryptography-eddsa", L, "cryptography : Ed25519 / Ed448")
R_CRY_X = enregistrer("py-cryptography-xdh", L, "cryptography : X25519 / X448")
R_CRY_DH = enregistrer("py-cryptography-dh", L, "cryptography : Diffie-Hellman à corps fini (taille lue)")
R_CRY_DSA = enregistrer("py-cryptography-dsa", L, "cryptography : DSA (taille lue)")
R_CRY_PQC = enregistrer("py-cryptography-pqc", L, "cryptography : ML-KEM / ML-DSA")
R_CRY_HASH = enregistrer("py-cryptography-hash", L, "cryptography : fonctions de hachage (hashes.*)")
R_CRY_SYM = enregistrer("py-cryptography-symetrique", L, "cryptography : AES, 3DES, RC4, ChaCha20, AEAD, mode lu dans Cipher()")
R_PCD_CLE = enregistrer("py-pycryptodome-cle", L, "PyCryptodome : clés RSA / ECC / DSA (taille ou courbe lue)")
R_PCD_SYM = enregistrer("py-pycryptodome-chiffrement", L, "PyCryptodome : AES (mode lu), DES, DES3, ARC4, ChaCha20, PKCS1_OAEP")
R_PCD_HASH = enregistrer("py-pycryptodome-hash", L, "PyCryptodome : Crypto.Hash.*")
R_PCD_SIG = enregistrer("py-pycryptodome-signature", L, "PyCryptodome : pkcs1_15, pss, DSS, eddsa")
R_HASHLIB = enregistrer("py-hashlib", L, "hashlib : md5, sha1, sha2, sha3, new(), pbkdf2_hmac()")
R_HMAC = enregistrer("py-hmac", L, "hmac : algorithme lu dans digestmod")
R_SSL_PROTO = enregistrer("py-ssl-protocole", L, "ssl : constantes de version (PROTOCOL_TLSv1, TLSVersion.TLSv1_1...)")
R_SSL_CTX = enregistrer("py-ssl-contexte", L, "ssl : contexte TLS (create_default_context, SSLContext, wrap_socket)")
R_SSL_SUITES = enregistrer("py-ssl-suites", L, "ssl : liste de suites passée à set_ciphers()")
R_SSL_COURBE = enregistrer("py-ssl-courbe", L, "ssl : courbe ECDH passée à set_ecdh_curve()")
R_PARAMIKO = enregistrer("py-paramiko-cle", L, "paramiko : RSAKey, ECDSAKey, Ed25519Key, DSSKey")
R_JWT = enregistrer("py-jwt-algorithme", L, "PyJWT / python-jose / authlib : algorithm=, algorithms=, ALGORITHMS.*, {'alg': ...}")
R_IMPORT = enregistrer("py-import-module", L, "import d'un module propre à un algorithme (ex. Crypto.Cipher.DES), usage non confirmé")
R_CHAINE = enregistrer("py-chaine-algorithme", L, "chaîne littérale égale à un nom d'algorithme OpenSSL/JCA (hors docstrings)")

C = "cryptography.hazmat.primitives"
A = C + ".asymmetric"


@dataclass(frozen=True)
class _Spec:
    regle: str
    algo: str  # nom pour resoudre() ; "@dernier" / "@module" = composant du nom qualifié
    fonctions: tuple[str, ...] = ()
    taille: tuple = ()  # (mot-clé, position)
    courbe: tuple = ()
    mode: tuple = ()
    note: str | None = None
    jca: bool = False


_EXACTS: dict[str, _Spec] = {}
_PREFIXES: list[tuple[str, _Spec]] = []


def _exact(noms: list[str], spec: _Spec) -> None:
    for n in noms:
        _EXACTS[n] = spec


def _prefixe(noms: list[str], spec: _Spec) -> None:
    _PREFIXES.extend((n, spec) for n in noms)


_exact([f"{A}.rsa.generate_private_key"], _Spec(R_CRY_RSA, "RSA", ("keygen",), taille=("key_size", 1)))
_exact([f"{A}.padding.OAEP"], _Spec(R_CRY_RSA, "RSA-OAEP", ("encrypt", "decrypt")))
_exact([f"{A}.padding.PSS"], _Spec(R_CRY_RSA, "RSA-PSS", ("sign", "verify")))
_exact([f"{A}.padding.PKCS1v15"], _Spec(R_CRY_RSA, "RSAES-PKCS1-v1_5", ("other",)))
_exact([f"{A}.ec.generate_private_key"], _Spec(R_CRY_EC, "EC", ("keygen",), courbe=("curve", 0)))
_exact([f"{A}.ec.derive_private_key"], _Spec(R_CRY_EC, "EC", ("keygen",), courbe=("curve", 1)))
_exact([f"{A}.ec.ECDSA"], _Spec(R_CRY_EC, "ECDSA", ("sign", "verify")))
_exact([f"{A}.ec.ECDH"], _Spec(R_CRY_EC, "ECDH", ("keyderive",)))
_prefixe([f"{A}.ed25519"], _Spec(R_CRY_ED, "Ed25519"))
_prefixe([f"{A}.ed448"], _Spec(R_CRY_ED, "Ed448"))
_prefixe([f"{A}.x25519"], _Spec(R_CRY_X, "X25519", ("keyderive",)))
_prefixe([f"{A}.x448"], _Spec(R_CRY_X, "X448", ("keyderive",)))
_prefixe([f"{A}.dh.generate_parameters"], _Spec(R_CRY_DH, "DH", ("keygen",), taille=("key_size", 1)))
_prefixe([f"{A}.dh"], _Spec(R_CRY_DH, "DH", ("keyderive",)))
_prefixe([f"{A}.dsa"], _Spec(R_CRY_DSA, "DSA", ("sign",), taille=("key_size", 0)))
for _n in ("512", "768", "1024"):
    _prefixe([f"{A}.mlkem.MLKEM{_n}PrivateKey", f"{A}.mlkem.MLKEM{_n}PublicKey"],
             _Spec(R_CRY_PQC, f"ML-KEM-{_n}", ("encapsulate", "decapsulate")))
for _n in ("44", "65", "87"):
    _prefixe([f"{A}.mldsa.MLDSA{_n}PrivateKey", f"{A}.mldsa.MLDSA{_n}PublicKey"],
             _Spec(R_CRY_PQC, f"ML-DSA-{_n}", ("sign", "verify")))
_prefixe([f"{C}.hashes"], _Spec(R_CRY_HASH, "@dernier", ("digest",)))
_prefixe([f"{C}.ciphers.algorithms", "cryptography.hazmat.decrepit.ciphers.algorithms"],
         _Spec(R_CRY_SYM, "@dernier", ("encrypt", "decrypt")))
_prefixe([f"{C}.ciphers.aead"], _Spec(R_CRY_SYM, "@aead", ("encrypt", "decrypt"), taille=("bit_length",)))

P = "Crypto"
_prefixe([f"{P}.PublicKey.RSA"], _Spec(R_PCD_CLE, "RSA", taille=("bits", 0)))
_prefixe([f"{P}.PublicKey.ECC"], _Spec(R_PCD_CLE, "EC", courbe=("curve",)))
_prefixe([f"{P}.PublicKey.DSA"], _Spec(R_PCD_CLE, "DSA", taille=("bits", 0)))
_exact([f"{P}.Cipher.AES.new"], _Spec(R_PCD_SYM, "AES", ("encrypt", "decrypt"), mode=("mode", 1)))
_exact([f"{P}.Cipher.DES.new"], _Spec(R_PCD_SYM, "DES", ("encrypt", "decrypt")))
_exact([f"{P}.Cipher.DES3.new"], _Spec(R_PCD_SYM, "3DES", ("encrypt", "decrypt")))
_exact([f"{P}.Cipher.ARC4.new"], _Spec(R_PCD_SYM, "RC4", ("encrypt", "decrypt")))
_exact([f"{P}.Cipher.ChaCha20.new"], _Spec(R_PCD_SYM, "ChaCha20", ("encrypt", "decrypt")))
_exact([f"{P}.Cipher.ChaCha20_Poly1305.new"], _Spec(R_PCD_SYM, "ChaCha20-Poly1305", ("encrypt", "decrypt")))
_exact([f"{P}.Cipher.PKCS1_OAEP.new"], _Spec(R_PCD_SYM, "RSA-OAEP", ("encrypt", "decrypt")))
_exact([f"{P}.Cipher.PKCS1_v1_5.new"], _Spec(R_PCD_SYM, "RSAES-PKCS1-v1_5", ("encrypt", "decrypt")))
_prefixe([f"{P}.Hash"], _Spec(R_PCD_HASH, "@module", ("digest",), jca=True))
_exact([f"{P}.Signature.pkcs1_15.new"], _Spec(R_PCD_SIG, "RSASSA-PKCS1-v1_5", ("sign", "verify")))
_exact([f"{P}.Signature.pss.new"], _Spec(R_PCD_SIG, "RSA-PSS", ("sign", "verify")))
_exact([f"{P}.Signature.DSS.new"], _Spec(R_PCD_SIG, "ECDSA", ("sign", "verify"), note="dss_ambigu"))
_exact([f"{P}.Signature.eddsa.new"], _Spec(R_PCD_SIG, "EdDSA", ("sign", "verify")))

_exact([f"hashlib.{h}" for h in ("md5", "sha1", "sha224", "sha256", "sha384", "sha512", "sha3_224", "sha3_256",
                                 "sha3_384", "sha3_512", "shake_128", "shake_256")],
       _Spec(R_HASHLIB, "@dernier", ("digest",)))
_exact(["hashlib.new"], _Spec(R_HASHLIB, "@arg0", ("digest",)))
_exact(["hashlib.pbkdf2_hmac"], _Spec(R_HASHLIB, "@pbkdf2", ("keyderive",)))
_exact(["hmac.new", "hmac.digest", "hmac.HMAC"], _Spec(R_HMAC, "@hmac", ("tag",)))

_exact(["ssl.create_default_context", "ssl.SSLContext", "ssl.wrap_socket", "ssl._create_unverified_context"],
       _Spec(R_SSL_CTX, "@tls", note="tls_defaut"))

for _cls, _algo in (("RSAKey", "RSA"), ("ECDSAKey", "ECDSA"), ("Ed25519Key", "Ed25519"), ("DSSKey", "DSA")):
    _prefixe([f"paramiko.{_cls}", f"paramiko.{_cls.lower()}.{_cls}"], _Spec(R_PARAMIKO, _algo, taille=("bits", 0)))

_AEAD = {"AESGCM": "AES-GCM", "AESCCM": "AES-CCM", "AESSIV": "AES-SIV", "AESOCB3": "AES-OCB",
         "AESGCMSIV": "AES-GCM-SIV", "ChaCha20Poly1305": "ChaCha20-Poly1305"}
_IMPORTS = {
    f"{P}.Cipher.DES": "DES", f"{P}.Cipher.DES3": "3DES", f"{P}.Cipher.ARC4": "RC4", f"{P}.Cipher.AES": "AES",
    f"{P}.PublicKey.RSA": "RSA", f"{P}.PublicKey.ECC": "EC", f"{P}.PublicKey.DSA": "DSA",
    f"{P}.Hash.MD5": "MD5", f"{P}.Hash.SHA1": "SHA1", f"{P}.Hash.SHA": "SHA1",
    f"{A}.rsa": "RSA", f"{A}.ec": "EC", f"{A}.ed25519": "Ed25519", f"{A}.ed448": "Ed448", f"{A}.x25519": "X25519",
    f"{A}.x448": "X448", f"{A}.dh": "DH", f"{A}.dsa": "DSA", f"{A}.mlkem": "ML-KEM", f"{A}.mldsa": "ML-DSA",
    "paramiko.dsskey": "DSA",
}
_ALEA = {"os.urandom", "secrets.token_bytes", f"{P}.Random.get_random_bytes"}
_CHAINES_MINUSCULES = re.compile(
    r"aes-(?:128|192|256)-(?:cbc|gcm|ecb|ctr|cfb|ofb|ccm|xts)|aes(?:128|192|256)|des-ede3(?:-cbc)?|des-(?:cbc|ecb)"
    r"|rc4|chacha20(?:-poly1305)?|md5|sha1|sha(?:224|256|384|512)|sha3-(?:224|256|384|512)|shake(?:128|256)"
    r"|prime256v1|secp(?:256k1|256r1|384r1|521r1)|x25519|x448|ed25519|ed448|ecdsa|mlkem(?:512|768|1024)"
    r"|ml-kem-(?:512|768|1024)|ml-dsa-(?:44|65|87)|ffdhe(?:2048|3072|4096|6144|8192)|x25519mlkem768"
)


_CHAINES_SURES = {"ECDSA", "ECDH", "ECDHE", "EdDSA", "AES", "DESede", "TripleDES", "ARCFOUR"}


def chaine_est_algo(s: str) -> list[Algo]:
    """Une chaîne littérale isolée ne compte que sous une forme non ambiguë.

    Exclut volontairement « RSA », « DES », « DSA », « EC », « DH » seuls : en
    français ou dans un contexte européen ce sont aussi des mots courants
    (revenu de solidarité active, article « des », Digital Services Act...).
    """
    s = s.strip()
    if not re.fullmatch(r"[A-Za-z0-9_./+-]{3,40}", s):
        return []
    if not (re.search(r"\d", s) or "/" in s or s in _CHAINES_SURES or _CHAINES_MINUSCULES.fullmatch(s)):
        return []
    return resoudre(s)


class _Visiteur(ast.NodeVisitor):
    def __init__(self) -> None:
        self.imports: dict[str, str] = {}
        self.constantes: dict[str, object] = {}
        self.tailles_cles: dict[str, int] = {}
        self.consommes: set[int] = set()
        self.docstrings: set[int] = set()
        self.detections: list[Detection] = []

    # -- résolution ------------------------------------------------------------
    def qualifie(self, node: ast.AST) -> str | None:
        parts: list[str] = []
        while isinstance(node, ast.Attribute):
            parts.append(node.attr)
            node = node.value
        if isinstance(node, ast.Name) and node.id in self.imports:
            parts.append(self.imports[node.id])
            return ".".join(reversed(parts))
        return None

    def valeur(self, node: ast.AST | None) -> object:
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            return self.constantes.get(node.id)
        return None

    def argument(self, call: ast.Call, cle: str | None, pos: int | None) -> ast.AST | None:
        for kw in call.keywords:
            if kw.arg == cle:
                return kw.value
        if pos is not None and pos < len(call.args):
            return call.args[pos]
        return None

    def _ajouter(self, node: ast.AST, regle: str, algos: list[Algo], confiance: str = "elevee",
                 fonctions: tuple[str, ...] = (), notes: tuple[str, ...] = (), extra: dict | None = None) -> None:
        for a in algos:
            a.notes.extend(n for n in notes if n not in a.notes)
            self.detections.append(Detection(node.lineno, regle, a, confiance, fonctions, [], dict(extra or {})))

    # -- visites ----------------------------------------------------------------
    def visit_Module(self, node: ast.Module) -> None:
        niveau_module = {id(n) for n in node.body}
        for n in ast.walk(node):
            if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and n.body:
                premier = n.body[0]
                if isinstance(premier, ast.Expr) and isinstance(premier.value, ast.Constant):
                    self.docstrings.add(id(premier.value))
            if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
                if isinstance(n.value, ast.Constant) and id(n) in niveau_module:
                    self.constantes[n.targets[0].id] = n.value.value
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            nom = alias.name.replace("Cryptodome", "Crypto", 1)
            if alias.asname:
                self.imports[alias.asname] = nom
            else:
                self.imports[alias.name.split(".")[0]] = nom.split(".")[0]
            self._import(node, nom)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.level or not node.module:
            return
        module = node.module.replace("Cryptodome", "Crypto", 1)
        for alias in node.names:
            complet = f"{module}.{alias.name}"
            self.imports[alias.asname or alias.name] = complet
            self._import(node, complet)

    def _import(self, node: ast.AST, complet: str) -> None:
        for candidat in (complet, complet.rsplit(".", 1)[0]):
            if candidat in _IMPORTS:
                self._ajouter(node, R_IMPORT, resoudre(_IMPORTS[candidat]), "moyenne", notes=("import",))
                return

    def visit_Assign(self, node: ast.Assign) -> None:
        if isinstance(node.value, ast.Call) and self.qualifie(node.value.func) in _ALEA:
            n = self.valeur(node.value.args[0]) if node.value.args else None
            if isinstance(n, int):
                for cible in node.targets:
                    if isinstance(cible, ast.Name):
                        self.tailles_cles[cible.id] = n * 8
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        q = self.qualifie(node)
        if q and (q.startswith("ssl.PROTOCOL_") or q.startswith("ssl.TLSVersion.")):
            version = q.rsplit(".", 1)[1].removeprefix("PROTOCOL_")
            algos = resoudre(version)
            if algos and algos[0].famille in ("TLS_LEGACY", "TLS_SUITE"):
                self._ajouter(node, R_SSL_PROTO, algos, extra={"version_tls": algos[0].nom})
        elif NOMS_JWT.match(node.attr) and isinstance(node.value, ast.Name) and node.value.id == "ALGORITHMS":
            self._ajouter(node, R_JWT, resoudre_jwt(node.attr), "moyenne", ("sign", "verify"))
        self.generic_visit(node)

    def visit_Dict(self, node: ast.Dict) -> None:
        for k, v in zip(node.keys, node.values):
            if isinstance(k, ast.Constant) and k.value == "alg" and isinstance(v, ast.Constant) \
                    and isinstance(v.value, str) and NOMS_JWT.match(v.value):
                self.consommes.add(id(v))
                self._ajouter(v, R_JWT, resoudre_jwt(v.value), "moyenne", ("sign", "verify"))
        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant) -> None:
        if isinstance(node.value, str) and id(node) not in self.consommes and id(node) not in self.docstrings:
            algos = chaine_est_algo(node.value)
            if algos:
                self._ajouter(node, R_CHAINE, algos, "faible", notes=("chaine",))

    def visit_Call(self, node: ast.Call) -> None:
        q = self.qualifie(node.func)
        if q:
            q = q.replace("Cryptodome.", "Crypto.", 1)
            spec = _EXACTS.get(q) or next((s for p, s in _PREFIXES if q == p or q.startswith(p + ".")), None)
            if q == f"{C}.ciphers.Cipher":
                self._cipher(node)
            elif spec:
                self._appel(node, q, spec)
        self._jwt(node, q)
        if isinstance(node.func, ast.Attribute) and node.args:
            texte = self.valeur(node.args[0])
            if node.func.attr == "set_ciphers" and isinstance(texte, str):
                self.consommes.add(id(node.args[0]))
                self._ajouter(node, R_SSL_SUITES, [Algo("TLS_SUITE", "TLS", "other")],
                              extra={"suites": [texte]}, notes=("tls_config",))
                self._ajouter(node, R_SSL_SUITES, suites_faibles(texte), notes=("suite_faible",))
            elif node.func.attr == "set_ecdh_curve" and isinstance(texte, str):
                self.consommes.add(id(node.args[0]))
                c = courbe_canonique(texte)
                self._ajouter(node, R_SSL_COURBE, [Algo("ECDH", f"ECDH-{c}" if c else "ECDH", "key-agree", courbe=c)],
                              fonctions=("keyderive",))
        self.generic_visit(node)

    # -- traitements spécifiques -----------------------------------------------------
    def _jwt(self, node: ast.Call, q: str | None) -> None:
        for kw in node.keywords:
            if kw.arg not in ("algorithm", "algorithms"):
                continue
            elems = kw.value.elts if isinstance(kw.value, (ast.List, ast.Tuple, ast.Set)) else [kw.value]
            connu = bool(q) and q.split(".")[0] in ("jwt", "jose", "authlib", "jwcrypto")
            for e in elems:
                nom = e.value if isinstance(e, ast.Constant) else (e.attr if isinstance(e, ast.Attribute) else None)
                if isinstance(nom, str) and NOMS_JWT.match(nom):
                    self.consommes.add(id(e))
                    self._ajouter(e, R_JWT, resoudre_jwt(nom), "elevee" if connu else "moyenne", ("sign", "verify"))

    def _cipher(self, node: ast.Call) -> None:
        algo_n = self.argument(node, "algorithm", 0)
        mode_n = self.argument(node, "mode", 1)
        if not isinstance(algo_n, ast.Call):
            return
        qa = self.qualifie(algo_n.func) or ""
        algos = resoudre(qa.rsplit(".", 1)[-1])
        if not algos:
            return
        a = algos[0]
        if isinstance(mode_n, ast.Call):
            mode = (self.qualifie(mode_n.func) or "").rsplit(".", 1)[-1]
            if a.famille == "AES" and mode:
                a = (resoudre(f"AES-{mode}") or [a])[0]
        a.taille = a.taille or self._taille_alea(algo_n.args[0] if algo_n.args else None)
        self.consommes.add(id(algo_n))
        self._ajouter(node, R_CRY_SYM, [a], fonctions=("encrypt", "decrypt"))

    def _taille_alea(self, node: ast.AST | None) -> int | None:
        if isinstance(node, ast.Name):
            return self.tailles_cles.get(node.id)
        if isinstance(node, ast.Call) and self.qualifie(node.func) in _ALEA and node.args:
            n = self.valeur(node.args[0])
            return n * 8 if isinstance(n, int) else None
        return None

    def _appel(self, node: ast.Call, q: str, spec: _Spec) -> None:
        if id(node) in self.consommes:
            return
        parts = q.split(".")
        nom = spec.algo
        notes: list[str] = [spec.note] if spec.note else []
        confiance = "elevee"
        if nom == "@dernier":
            nom = parts[-1]
            if nom.endswith("Key") or nom in ("Hash", "HashAlgorithm", "BLAKE2b", "BLAKE2s"):
                return
        elif nom == "@module":
            nom = parts[2] if len(parts) > 3 else parts[-1]
        elif nom == "@aead":
            nom = _AEAD.get(parts[-1] if parts[-1] in _AEAD else parts[-2], "")
        elif nom in ("@arg0", "@pbkdf2", "@hmac"):
            if nom == "@hmac":
                arg = self.argument(node, "digest" if parts[-1] == "digest" else "digestmod", 2)
            else:
                arg = self.argument(node, "name" if nom == "@arg0" else "hash_name", 0)
            v = self.valeur(arg)
            if not isinstance(v, str) and arg is not None:
                v = (self.qualifie(arg) or "").rsplit(".", 1)[-1] or None
            if not isinstance(v, str):
                return
            if arg is not None:
                self.consommes.add(id(arg))
            nom = {"@arg0": v, "@pbkdf2": f"PBKDF2WithHmac{v}", "@hmac": f"HMAC-{v}"}[nom]
        elif nom == "@tls":
            self._ajouter(node, spec.regle, [Algo("TLS_SUITE", "TLS", "other")], "moyenne", notes=tuple(notes))
            return
        algos = resoudre(nom, jca=spec.jca)
        if not algos:
            return
        a = algos[0]
        fonctions = spec.fonctions or (("keygen",) if parts[-1].startswith("generate") else ())
        if spec.taille:
            v = self.valeur(self.argument(node, *(spec.taille + (None,))[:2]))
            if isinstance(v, int) and 64 <= v <= 65536:
                if a.famille == "ECDSA" and a.nom == "ECDSA":  # paramiko : bits=256 -> P-256
                    a.courbe = {256: "P-256", 384: "P-384", 521: "P-521"}.get(v)
                else:
                    a.taille = v
        if spec.courbe:
            c_node = self.argument(node, *(spec.courbe + (None,))[:2])
            c = self.valeur(c_node)
            if not isinstance(c, str) and c_node is not None:
                cible = c_node.func if isinstance(c_node, ast.Call) else c_node
                c = (self.qualifie(cible) or "").rsplit(".", 1)[-1]
            a.courbe = courbe_canonique(c) if isinstance(c, str) else None
            if c_node is not None:
                self.consommes.add(id(c_node))
                if isinstance(c_node, ast.Call):
                    self.consommes.add(id(c_node.func))
        if spec.mode:
            m_node = self.argument(node, *spec.mode)
            m = (self.qualifie(m_node) or "").rsplit(".", 1)[-1] if m_node is not None else ""
            if m.startswith("MODE_"):
                a = (resoudre(f"AES-{m[5:]}") or [a])[0]
        if a.famille == "AES" and not a.taille:
            a.taille = self._taille_alea(node.args[0] if node.args else None)
        if a.famille in ("MD5", "SHA1") and any(
                kw.arg == "usedforsecurity" and isinstance(kw.value, ast.Constant) and kw.value.value is False
                for kw in node.keywords):
            notes.append("non_securitaire")
            confiance = "moyenne"
        for arg in list(node.args) + [kw.value for kw in node.keywords]:
            if isinstance(arg, ast.Constant):
                self.consommes.add(id(arg))
        self._ajouter(node, spec.regle, [a] + algos[1:], confiance, fonctions, tuple(notes))


def analyser_python(source: str) -> list[Detection] | None:
    """Renvoie les détections, ou None si le fichier n'est pas du Python 3 valide."""
    try:
        arbre = ast.parse(source)
    except (SyntaxError, ValueError):
        return None
    v = _Visiteur()
    v.visit(arbre)
    return v.detections
