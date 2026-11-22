# Préparation post-quantique : inventaire cryptographique

## pyjwt-2.10.1 (démonstration, bibliothèque libre)

| | |
|---|---|
| Client | pyjwt-2.10.1 (démonstration, bibliothèque libre) |
| Préparé par | Atelier PQC |
| Date | 2026-11-22 |
| Sources analysées | constats.json (code, 86 fichier(s)) |
| Référentiel réglementaire | regles.json, version 2026-11-22 (6 texte(s)) |
| Statut | Projet à relire, compléter et signer par le relecteur |

> Ce document est un produit d'information issu d'une analyse automatisée, relu par une personne. Il ne constitue ni un avis juridique, ni une certification, ni un audit de conformité.
>
> **Avertissement du référentiel** : Référentiel établi le 22 novembre 2026 à partir de notes de recherche datées et de sources primaires consultées le même jour. Ce n'est pas un avis juridique : l'applicabilité d'un texte à une organisation donnée doit être confirmée par un juriste ou par l'autorité compétente. Pour la plupart des entreprises privées situées hors du périmètre PCI DSS et hors des marchés publics (notamment fédéraux américains), aucune échéance de migration post-quantique contraignante n'existe à ce jour : les autres textes sont des recommandations, des projets ou des obligations qui visent des administrations. Conventions : « nature » décrit la portée du texte pour le public qu'il vise, pas pour le client ; « echeance » est la date à partir de laquelle, ou au plus tard à laquelle, l'effet s'applique ; quand le texte ne donne qu'une année, la date retenue est le 31 décembre de cette année, et quand il ne donne qu'un mois, le dernier jour de ce mois. « confiance » : elevee = vérifié dans le texte primaire le 22/11/2026 ; moyenne = partiellement vérifié (date ou libellé principal confirmé par une source officielle, le reste par des sources secondaires concordantes) ; faible = non vérifié dans une source primaire. Une exigence « faible » ne doit pas être citée à un client sans vérification préalable.

## 1. Synthèse

L'analyse a relevé **238 constats** répartis en **5 familles cryptographiques**, dont **35** dans du code ou des configurations classés « production ». 99 constats portent sur de la cryptographie à clé publique classique, vulnérable à un futur ordinateur quantique (algorithme de Shor) ; 0 portent sur des algorithmes ou protocoles déjà obsolètes aujourd'hui.

### Répartition par classe

| Classe | Constats | dont production | Familles |
|---|---:|---:|---|
| Vulnérable (algorithme de Shor) | 99 | 35 | RSA, ECDSA, EDDSA |
| Hachage robuste | 137 | 0 | SHA2 |
| Inventaire TLS | 2 | 0 | TLS_SUITE |

### Principaux risques

Classement par gravité de la classe, contexte (la production compte davantage que les tests) et confiance du constat.

1. **ECDSA** (Signatures ECDSA) : 50 occurrence(s), dont 15 en production ; signatures falsifiables une fois un ordinateur quantique disponible ; migration à coordonner avec la PKI. Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31), CABF-VALIDITE-200J-2026 (2026-03-15), et 8 autre(s), voir la section 3.
2. **EDDSA** (Signatures Ed25519 / Ed448) : 25 occurrence(s), dont 16 en production ; signatures falsifiables une fois un ordinateur quantique disponible ; migration à coordonner avec la PKI. Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31), EU-NIS2-PROPOSITION-PQC (—), et 5 autre(s), voir la section 3.
3. **RSA** (RSA (chiffrement, signature, échange de clés)) : 24 occurrence(s), dont 4 en production ; cryptographie à clé publique cassable par l'algorithme de Shor (chiffrement, échange de clés, signature). Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31), CABF-VALIDITE-200J-2026 (2026-03-15), et 8 autre(s), voir la section 3.

### Points TLS sondés

Aucun point TLS n'a été sondé. La sonde doit être lancée depuis le réseau du client ou du partenaire.

## 2. Inventaire

### 2.1 Par famille

| Famille | Classe | Occurrences | Production | Test / exemple / doc. | Confiance (é / m / f) | Algorithmes observés |
|---|---|---:|---:|---:|---|---|
| RSA | Vulnérable (algorithme de Shor) | 24 | 4 | 20 | 18 / 6 / 0 | RS256, RS384, RSA, RSA-1024, RSA-2048, RSA-PSS |
| ECDSA | Vulnérable (algorithme de Shor) | 50 | 15 | 35 | 10 / 8 / 32 | EC, EC-P-256, EC-P-384, EC-P-521, EC-secp256k1, ECDSA et 2 autre(s) |
| EDDSA | Vulnérable (algorithme de Shor) | 25 | 16 | 9 | 10 / 0 / 15 | Ed25519, Ed448, EdDSA |
| SHA2 | Hachage robuste | 137 | 0 | 137 | 3 / 134 / 0 | HS256, HS384, HS512 |
| TLS_SUITE | Inventaire TLS | 2 | 0 | 2 | 0 / 2 / 0 | TLS |

### 2.2 Par emplacement

| Emplacement | Famille | Détail | Contexte | Confiance | Règle | Extrait |
|---|---|---|---|---|---|---|
| `docs/usage.rst:23` | RSA | RSA-2048 ; clé privée présente dans les fichiers analysés | documentation | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `docs/usage.rst:24` | RSA | RSA-2048 ; clé publique | documentation | élevée | `pem-cle-publique` | `-----BEGIN PUBLIC KEY-----` |
| `docs/usage.rst:36` | RSA | RSA ; clé privée présente dans les fichiers analysés ; clé chiffrée, paramètres non lus | documentation | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `docs/usage.rst:56` | RSA | RSA-2048 ; clé privée présente dans les fichiers analysés | documentation | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `docs/usage.rst:57` | RSA | RSA-2048 ; clé publique | documentation | élevée | `pem-cle-publique` | `-----BEGIN PUBLIC KEY-----` |
| `docs/usage.rst:70` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | documentation | élevée | `pem-cle-privee` | `-----BEGIN PRIVATE KEY----- [contenu masqué]` |
| `docs/usage.rst:71` | EDDSA | Ed25519 ; clé publique | documentation | élevée | `pem-cle-publique` | `-----BEGIN PUBLIC KEY-----` |
| `docs/usage.rst:84` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | documentation | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `docs/usage.rst:85` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; clé publique | documentation | élevée | `pem-cle-publique` | `-----BEGIN PUBLIC KEY-----` |
| `jwt/algorithms.py:101` | EDDSA | EdDSA ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"EdDSA",` |
| `jwt/algorithms.py:132` | EDDSA | EdDSA ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"EdDSA": OKPAlgorithm(),` |
| `jwt/algorithms.py:477` | RSA | RSA | production | élevée | `py-cryptography-rsa` | `return key.sign(msg, padding.PKCS1v15(), self.hash_alg())` |
| `jwt/algorithms.py:481` | RSA | RSA | production | élevée | `py-cryptography-rsa` | `key.verify(sig, msg, padding.PKCS1v15(), self.hash_alg())` |
| `jwt/algorithms.py:530` | ECDSA | ECDSA, signature / vérification de signature | production | élevée | `py-cryptography-ec` | `der_sig = key.sign(msg, ECDSA(self.hash_alg()))` |
| `jwt/algorithms.py:546` | ECDSA | ECDSA, signature / vérification de signature | production | élevée | `py-cryptography-ec` | `public_key.verify(der_sig, msg, ECDSA(self.hash_alg()))` |
| `jwt/algorithms.py:573` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "P-256"` |
| `jwt/algorithms.py:575` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "P-384"` |
| `jwt/algorithms.py:577` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "P-521"` |
| `jwt/algorithms.py:579` | ECDSA | EC-secp256k1 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "secp256k1"` |
| `jwt/algorithms.py:631` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if curve == "P-256":` |
| `jwt/algorithms.py:638` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `elif curve == "P-384":` |
| `jwt/algorithms.py:645` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `elif curve == "P-521":` |
| `jwt/algorithms.py:652` | ECDSA | EC-secp256k1 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `elif curve == "secp256k1":` |
| `jwt/algorithms.py:689` | RSA | RSA-PSS, signature / vérification de signature | production | élevée | `py-cryptography-rsa` | `padding.PSS(` |
| `jwt/algorithms.py:701` | RSA | RSA-PSS, signature / vérification de signature | production | élevée | `py-cryptography-rsa` | `padding.PSS(` |
| `jwt/algorithms.py:802` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "Ed25519" if isinstance(key, Ed25519PublicKey) else "Ed448"` |
| `jwt/algorithms.py:802` | EDDSA | Ed448 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "Ed25519" if isinstance(key, Ed25519PublicKey) else "Ed448"` |
| `jwt/algorithms.py:827` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "Ed25519" if isinstance(key, Ed25519PrivateKey) else "Ed448"` |
| `jwt/algorithms.py:827` | EDDSA | Ed448 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `crv = "Ed25519" if isinstance(key, Ed25519PrivateKey) else "Ed448"` |
| `jwt/algorithms.py:858` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if curve != "Ed25519" and curve != "Ed448":` |
| `jwt/algorithms.py:858` | EDDSA | Ed448 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if curve != "Ed25519" and curve != "Ed448":` |
| `jwt/algorithms.py:867` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if curve == "Ed25519":` |
| `jwt/algorithms.py:868` | EDDSA | Ed25519 | production | élevée | `py-cryptography-eddsa` | `return Ed25519PublicKey.from_public_bytes(x)` |
| `jwt/algorithms.py:869` | EDDSA | Ed448 | production | élevée | `py-cryptography-eddsa` | `return Ed448PublicKey.from_public_bytes(x)` |
| `jwt/algorithms.py:871` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if curve == "Ed25519":` |
| `jwt/algorithms.py:872` | EDDSA | Ed25519 | production | élevée | `py-cryptography-eddsa` | `return Ed25519PrivateKey.from_private_bytes(d)` |
| `jwt/algorithms.py:873` | EDDSA | Ed448 | production | élevée | `py-cryptography-eddsa` | `return Ed448PrivateKey.from_private_bytes(d)` |
| `jwt/api_jwk.py:34` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if crv == "P-256" or not crv:` |
| `jwt/api_jwk.py:36` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `elif crv == "P-384":` |
| `jwt/api_jwk.py:38` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `elif crv == "P-521":` |
| `jwt/api_jwk.py:40` | ECDSA | EC-secp256k1 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `elif crv == "secp256k1":` |
| `jwt/api_jwk.py:51` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if crv == "Ed25519":` |
| `jwt/api_jwk.py:52` | EDDSA | EdDSA ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `algorithm = "EdDSA"` |
| `jwt/utils.py:7` | ECDSA | EC ; clé EC : ECDSA ou ECDH selon l'usage ; import du module, usage non confirmé | production | moyenne | `py-import-module` | `from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurve` |
| `tests/keys/__init__.py:8` | ECDSA | EC ; clé EC : ECDSA ou ECDH selon l'usage ; import du module, usage non confirmé | test | moyenne | `py-import-module` | `from cryptography.hazmat.primitives.asymmetric import ec` |
| `tests/keys/testkey2_rsa.pub.pem:1` | RSA | RSA-2048 ; clé publique | test | élevée | `pem-cle-publique` | `-----BEGIN PUBLIC KEY-----` |
| `tests/keys/testkey_ec.priv:1` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN PRIVATE KEY----- [contenu masqué]` |
| `tests/keys/testkey_ec.pub:1` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; clé publique | test | élevée | `pem-cle-publique` | `-----BEGIN PUBLIC KEY-----` |
| `tests/keys/testkey_ec_secp192r1.priv:1` | ECDSA | EC ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN PRIVATE KEY----- [contenu masqué]` |
| `tests/keys/testkey_ec_ssh.pub:1` | ECDSA | ECDSA-P-256, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ecdsa-sha2-nistp256 [clé masquée]` |
| `tests/keys/testkey_ed25519:1` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN PRIVATE KEY----- [contenu masqué]` |
| `tests/keys/testkey_ed25519.pub:1` | EDDSA | Ed25519, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-ed25519 [clé masquée]` |
| `tests/keys/testkey_pkcs1.pub.pem:1` | RSA | RSA-1024 ; clé publique | test | élevée | `pem-cle-publique` | `-----BEGIN RSA PUBLIC KEY-----` |
| `tests/keys/testkey_rsa.cer:1` | RSA | RSA-2048, vérification de signature ; certificat X.509 ; OU=Test Certificate,O=PyJWT,L=Austin,ST=Texas,C=US, expire le 2018-03-17 | test | élevée | `pem-certificat` | `-----BEGIN CERTIFICATE-----` |
| `tests/keys/testkey_rsa.priv:1` | RSA | RSA-2048 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `tests/keys/testkey_rsa.pub:1` | RSA | RSA-2048, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-rsa [clé masquée]` |
| `tests/test_advisory.py:9` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN PRIVATE KEY----- [contenu masqué]` |
| `tests/test_advisory.py:14` | EDDSA | Ed25519, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-ed25519 [clé masquée]` |
| `tests/test_advisory.py:17` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_advisory.py:23` | ECDSA | ECDSA-P-256, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ecdsa-sha2-nistp256 [clé masquée]` |
| `tests/test_algorithms.py:27` | RSA | RSA ; import du module, usage non confirmé | test | moyenne | `py-import-module` | `from cryptography.hazmat.primitives.asymmetric.rsa import (` |
| `tests/test_algorithms.py:172` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-256": ECAlgorithm.SHA256,` |
| `tests/test_algorithms.py:173` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-384": ECAlgorithm.SHA384,` |
| `tests/test_algorithms.py:174` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-521": ECAlgorithm.SHA512,` |
| `tests/test_algorithms.py:175` | ECDSA | EC-secp256k1 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"secp256k1": ECAlgorithm.SHA256,` |
| `tests/test_algorithms.py:194` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-256": {` |
| `tests/test_algorithms.py:198` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-384": {` |
| `tests/test_algorithms.py:202` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-521": {` |
| `tests/test_algorithms.py:206` | ECDSA | EC-secp256k1 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"secp256k1": {` |
| `tests/test_algorithms.py:237` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `for curve in ("P-256", "P-384", "P-521", "secp256k1"):` |
| `tests/test_algorithms.py:237` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `for curve in ("P-256", "P-384", "P-521", "secp256k1"):` |
| `tests/test_algorithms.py:237` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `for curve in ("P-256", "P-384", "P-521", "secp256k1"):` |
| `tests/test_algorithms.py:237` | ECDSA | EC-secp256k1 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `for curve in ("P-256", "P-384", "P-521", "secp256k1"):` |
| `tests/test_algorithms.py:289` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"crv": "P-256",` |
| `tests/test_algorithms.py:311` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"crv": "P-256",` |
| `tests/test_algorithms.py:330` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-256": ECAlgorithm.SHA256,` |
| `tests/test_algorithms.py:331` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-384": ECAlgorithm.SHA384,` |
| `tests/test_algorithms.py:332` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"P-521": ECAlgorithm.SHA512,` |
| `tests/test_algorithms.py:333` | ECDSA | EC-secp256k1 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"secp256k1": ECAlgorithm.SHA256,` |
| `tests/test_algorithms.py:936` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `v["crv"] = "P-256"` |
| `tests/test_algorithms.py:942` | EDDSA | Ed448 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `v["crv"] = "Ed448"` |
| `tests/test_algorithms.py:1046` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `v["crv"] = "P-256"` |
| `tests/test_algorithms.py:1052` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `v["crv"] = "Ed25519"` |
| `tests/test_api_jwk.py:80` | RSA | RS256, signature / vérification de signature | test | élevée | `py-jwt-algorithme` | `jwk = PyJWK.from_dict(key_data, algorithm="RS256")` |
| `tests/test_api_jwk.py:169` | EDDSA | EdDSA ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert jwk.algorithm_name == "EdDSA"` |
| `tests/test_api_jwk.py:217` | RSA | RS256, signature / vérification de signature | test | élevée | `py-jwt-algorithme` | `PyJWK({"kty": "dummy"}, algorithm="RS256")` |
| `tests/test_api_jwk.py:223` | RSA | RS256, signature / vérification de signature | test | élevée | `py-jwt-algorithme` | `PyJWK({"kty": "dummy"}, algorithm="RS256")` |
| `tests/test_api_jws.py:70` | SHA2 | HS256, signature / vérification de signature | test | élevée | `py-jwt-algorithme` | `jws = PyJWS(algorithms=["HS256"])` |
| `tests/test_api_jws.py:92` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws_message = jws.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jws.py:93` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(jws_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:101` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws_token = jws.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jws.py:102` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(jws_token, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:105` | SHA2 | HS384, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(jws_token, secret, algorithms=["HS384"])` |
| `tests/test_api_jws.py:115` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(unicode_jws, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:122` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:132` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:142` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:156` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:163` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jws.decode_complete(msg, "secret", algorithms=["HS256"])` |
| `tests/test_api_jws.py:165` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"header": {"alg": "HS256", "typ": "JWT"},` |
| `tests/test_api_jws.py:174` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.encode(payload, "secret", algorithm="HS256")` |
| `tests/test_api_jws.py:195` | ECDSA | ES256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `msg = jws.encode(payload, priv_key, headers={"alg": "ES256"})` |
| `tests/test_api_jws.py:196` | ECDSA | ES256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `assert b"hello world" == jws.decode(msg, pub_key, algorithms=["ES256"])` |
| `tests/test_api_jws.py:205` | ECDSA | ES256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `msg = jws.encode(payload, priv_key, algorithm="HS256", headers={"alg": "ES256"})` |
| `tests/test_api_jws.py:205` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `msg = jws.encode(payload, priv_key, algorithm="HS256", headers={"alg": "ES256"})` |
| `tests/test_api_jws.py:206` | ECDSA | ES256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `assert b"hello world" == jws.decode(msg, pub_key, algorithms=["ES256"])` |
| `tests/test_api_jws.py:212` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"alg": "HS256",` |
| `tests/test_api_jws.py:217` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jws.decode_complete(msg, key=jwk, algorithms=["HS256"])` |
| `tests/test_api_jws.py:219` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"header": {"alg": "HS256", "typ": "JWT"},` |
| `tests/test_api_jws.py:247` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(jws_message, bad_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:251` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(jws_message, bad_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:262` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:274` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jws.decode_complete(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:277` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"header": {"alg": "HS256", "typ": "JWT"},` |
| `tests/test_api_jws.py:289` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"alg": "HS256",` |
| `tests/test_api_jws.py:299` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(example_jws, jwk, algorithms=["HS256"])` |
| `tests/test_api_jws.py:307` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"alg": "HS256",` |
| `tests/test_api_jws.py:325` | SHA2 | HS512, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"alg": "HS512",` |
| `tests/test_api_jws.py:352` | ECDSA | ES256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(example_jws, example_pubkey, algorithms=["ES256"])` |
| `tests/test_api_jws.py:378` | RSA | RS384, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(example_jws, example_pubkey, algorithms=["RS384"])` |
| `tests/test_api_jws.py:392` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `example_jws, key=example_secret, algorithms=["HS256"]` |
| `tests/test_api_jws.py:440` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jws.py:451` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(jws_message, algorithms=["HS256"])` |
| `tests/test_api_jws.py:458` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(jws_message, algorithms=["HS256"])` |
| `tests/test_api_jws.py:466` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, "secret", algorithms=["HS256"])` |
| `tests/test_api_jws.py:475` | RSA | RS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.encode(payload, "secret", algorithm="RS256")` |
| `tests/test_api_jws.py:481` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(jws_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:489` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(jws_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:497` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jws.decode(jws_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:521` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:534` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:547` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:560` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:578` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithm="HS256",` |
| `tests/test_api_jws.py:822` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `payload, secret, algorithm="HS256", is_payload_detached=True` |
| `tests/test_api_jws.py:825` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(jws_message, secret, algorithms=["HS256"], detached_payload=payload)` |
| `tests/test_api_jws.py:863` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jws.decode(example_jws, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jws.py:873` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `payload, secret, algorithm="HS256", is_payload_detached=True` |
| `tests/test_api_jws.py:880` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jws.py:890` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `payload, secret, algorithm="HS256", is_payload_detached=True` |
| `tests/test_api_jws.py:897` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:47` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jwt.decode(example_jwt, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:59` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode_complete(example_jwt, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:62` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"header": {"alg": "HS256", "typ": "JWT"},` |
| `tests/test_api_jwt.py:80` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `example_jwt, key=example_secret, algorithms=["HS256"]` |
| `tests/test_api_jwt.py:94` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(example_jwt, example_secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:107` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(example_jwt, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:121` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(example_jwt, secret, audience=1, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:139` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:158` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:170` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `lambda t=t: jwt.encode(t, "secret", algorithms=["HS256"]),` |
| `tests/test_api_jwt.py:190` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `payload, "secret", algorithm="HS256", headers={"typ": "secevent+jwt"}` |
| `tests/test_api_jwt.py:208` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(example_jwt, "secret", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:221` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(example_jwt, "secret", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:229` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:235` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `data = jwt.decode(jwt_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:247` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(example_jwt, "secret", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:256` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode(example_jwt, "secret", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:269` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt_message, secret, leeway=1, algorithms=["HS256"]` |
| `tests/test_api_jwt.py:297` | ECDSA | ES256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jwt.decode(example_jwt, example_pubkey, algorithms=["ES256"])` |
| `tests/test_api_jwt.py:321` | RSA | RS384, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded_payload = jwt.decode(example_jwt, example_pubkey, algorithms=["RS384"])` |
| `tests/test_api_jwt.py:331` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:339` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:349` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:361` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:373` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt_message, secret, leeway=leeway, algorithms=["HS256"]` |
| `tests/test_api_jwt.py:380` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, leeway=leeway, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:388` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, leeway=13, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:391` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, leeway=1, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:396` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", audience="urn:me", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:405` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:412` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:422` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:428` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", audience="urn:me", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:436` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", audience="urn-me", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:442` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", audience=b"urn:me", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:453` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", audience="urn:me", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:463` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", issuer=issuer, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:475` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", issuer=issuer, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:482` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", audience="urn:me", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:491` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", audience="urn:me", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:499` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", issuer=issuer, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:505` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", issuer=issuer, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:515` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", issuer=issuer, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:525` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, "secret", issuer=issuer, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:534` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:547` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:562` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:579` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:596` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:611` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:624` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:637` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:650` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.encode(data, "secret", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:653` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `payload = jwt.decode(token, "secret", algorithms=["HS256"])` |
| `tests/test_api_jwt.py:665` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:673` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:718` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, verify=False, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:732` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, options=options, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:740` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(jwt_message, secret, algorithms=["HS256"], foo="bar")` |
| `tests/test_api_jwt.py:749` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode_complete(jwt_message, secret, algorithms=["HS256"], foo="bar")` |
| `tests/test_api_jwt.py:764` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:774` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:788` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:800` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:816` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:829` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `algorithms=["HS256"],` |
| `tests/test_api_jwt.py:839` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:840` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode(token, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:846` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode({}, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:848` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode(token, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:854` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode({}, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:858` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token, secret, algorithms=["HS256"], options={"require": ["sub"]}` |
| `tests/test_api_jwt.py:866` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:869` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:876` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:878` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode(token, secret, algorithms=["HS256"], subject="user123")` |
| `tests/test_api_jwt.py:887` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:890` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, secret, algorithms=["HS256"], subject="user456")` |
| `tests/test_api_jwt.py:899` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:901` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode(token, secret, algorithms=["HS256"], subject=None)` |
| `tests/test_api_jwt.py:911` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:912` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode(token, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:919` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:923` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token, secret, algorithms=["HS256"], options={"require": ["jti"]}` |
| `tests/test_api_jwt.py:930` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode({}, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:932` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `decoded = jwt.decode(token, secret, algorithms=["HS256"])` |
| `tests/test_api_jwt.py:942` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `token = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_api_jwt.py:945` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `jwt.decode(token, secret, algorithms=["HS256"])` |
| `tests/test_compressed_jwt.py:27` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `example_jwt, example_secret, algorithms=["HS256"]` |
| `tests/test_compressed_jwt.py:31` | SHA2 | HS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"header": {"alg": "HS256", "typ": "JWT"},` |
| `tests/test_jwks_client.py:20` | RSA | RS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"alg": "RS256",` |
| `tests/test_jwks_client.py:37` | RSA | RS256, signature / vérification de signature | test | moyenne | `py-jwt-algorithme` | `"alg": "RS256",` |
| `tests/test_jwks_client.py:207` | RSA | RS256, signature / vérification de signature | test | élevée | `py-jwt-algorithme` | `algorithms=["RS256"],` |
| `tests/test_jwks_client.py:342` | TLS_SUITE | TLS ; paramètres TLS par défaut de la bibliothèque | test | moyenne | `py-ssl-contexte` | `jwks_client = PyJWKClient(url, ssl_context=ssl.create_default_context())` |
| `tests/test_jwks_client.py:351` | TLS_SUITE | TLS ; paramètres TLS par défaut de la bibliothèque | test | moyenne | `py-ssl-contexte` | `url, ssl_context=ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)` |
| `tests/test_jwt.py:16` | SHA2 | HS256, signature / vérification de signature | test | élevée | `py-jwt-algorithme` | `jwt_message = jwt.encode(payload, secret, algorithm="HS256")` |
| `tests/test_jwt.py:17` | SHA2 | HS256, signature / vérification de signature | test | élevée | `py-jwt-algorithme` | `decoded_payload = jwt.decode(jwt_message, secret, algorithms=["HS256"])` |

## 3. Correspondance réglementaire

Les exigences ci-dessous proviennent exclusivement du référentiel fourni (regles.json, version 2026-11-22). Leur applicabilité au client dépend de son secteur, de sa juridiction et de ses contrats ; le relecteur doit la confirmer.

### 3.1 Familles observées et exigences

| Famille | Exigences du référentiel (échéance, effet) |
|---|---|
| RSA | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; CABF-VALIDITE-200J-2026 (2026-03-15, autre) ; CABF-VALIDITE-100J-2027 (2027-03-15, autre) ; CABF-VALIDITE-47J-2029 (2029-03-15, autre) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| ECDSA | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; CABF-VALIDITE-200J-2026 (2026-03-15, autre) ; CABF-VALIDITE-100J-2027 (2027-03-15, autre) ; CABF-VALIDITE-47J-2029 (2029-03-15, autre) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| EDDSA | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| SHA2 | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) |
| TLS_SUITE | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; CABF-VALIDITE-200J-2026 (2026-03-15, autre) ; CABF-VALIDITE-100J-2027 (2027-03-15, autre) ; CABF-VALIDITE-47J-2029 (2029-03-15, autre) |

### 3.2 Détail des exigences citées

#### PCI-DSS-12.3.3-INVENTAIRE-SUITES (PCI DSS v4.0.1 — Payment Card Industry Data Security Standard)

- Émetteur, juridiction, nature : PCI Security Standards Council, INT, contraignant
- Public visé : Entités qui stockent, traitent ou transmettent des données de titulaires de carte, et prestataires pouvant affecter leur sécurité. L'obligation est contractuelle (réseaux de cartes, acquéreurs), pas légale.
- Résumé : Les suites et protocoles cryptographiques utilisés sont documentés et revus au moins tous les 12 mois : inventaire à jour (usage et emplacement), veille sur leur viabilité, stratégie documentée face aux vulnérabilités attendues. Obligatoire depuis le 31 mars 2025. Aucune échéance de migration PQC. Libellé principal vérifié sur un document hébergé par le PCI SSC ; les alinéas « veille » et « stratégie » proviennent de sources secondaires concordantes (texte de la norme, sous licence, non consulté).
- Échéance : 2025-03-31
- Effet : inventaire obligatoire
- Confiance du référentiel : moyenne
- Familles observées concernées : RSA, ECDSA, EDDSA, SHA2, TLS_SUITE
- Source : <https://www.pcisecuritystandards.org/day-1_t2_7_pci-dss-v4-0_final/> (source datée du 2024-08-20)

#### PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (PCI DSS v4.0.1 — Payment Card Industry Data Security Standard)

- Émetteur, juridiction, nature : PCI Security Standards Council, INT, contraignant
- Public visé : Entités qui stockent, traitent ou transmettent des données de titulaires de carte, et prestataires pouvant affecter leur sécurité. L'obligation est contractuelle (réseaux de cartes, acquéreurs), pas légale.
- Résumé : Inventaire des clés et certificats de confiance utilisés pour protéger le PAN en transmission, exigence applicable depuis le 31 mars 2025. Non vérifié dans le texte de la norme : seule une source secondaire a été lue.
- Échéance : 2025-03-31
- Effet : inventaire obligatoire
- Confiance du référentiel : faible (à vérifier dans la source primaire)
- Familles observées concernées : RSA, ECDSA, EDDSA, TLS_SUITE
- Source : <https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/> (source datée du 2024-08-20)

#### CABF-VALIDITE-200J-2026 (CA/Browser Forum — Baseline Requirements, scrutin SC-081v3 (durées de validité des certificats TLS))

- Émetteur, juridiction, nature : CA/Browser Forum, INT, contraignant indirectement (marchés publics, contrats)
- Public visé : Autorités de certification publiques (obligation directe). Tout détenteur de certificats TLS publics en subit l'effet. Ce ne sont pas des exigences PQC.
- Résumé : Durée de validité maximale de 200 jours pour les certificats TLS publics émis à partir du 15 mars 2026 (en vigueur) ; réutilisation des validations de domaine limitée à 200 jours. Vérifié dans les Baseline Requirements v2.3.1.
- Échéance : 2026-03-15
- Effet : autre
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, TLS_SUITE
- Source : <https://github.com/cabforum/servercert/blob/main/docs/BR.md> (source datée du 2025-04-11)

#### EU-ROADMAP-2026-PLANS-NATIONAUX (A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography (NIS Cooperation Group, v1.1))

- Émetteur, juridiction, nature : NIS Cooperation Group (groupe de travail PQC), avec la Commission européenne, EU, recommandation
- Public visé : États membres de l'UE. Le texte ne crée aucune obligation directe pour les entreprises ; il découle d'une recommandation de la Commission et n'a pas, à notre lecture, d'effet juridique contraignant.
- Résumé : D'ici le 31 décembre 2026 : premières étapes mises en œuvre par tous les États membres, feuilles de route nationales initiales établies, planification et pilotes lancés pour les usages à risque élevé et moyen.
- Échéance : 2026-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, EDDSA
- Source : <https://ec.europa.eu/newsroom/dae/redirection/document/117507> (source datée du 2025-06-23)

#### CABF-VALIDITE-100J-2027 (CA/Browser Forum — Baseline Requirements, scrutin SC-081v3 (durées de validité des certificats TLS))

- Émetteur, juridiction, nature : CA/Browser Forum, INT, contraignant indirectement (marchés publics, contrats)
- Public visé : Autorités de certification publiques (obligation directe). Tout détenteur de certificats TLS publics en subit l'effet. Ce ne sont pas des exigences PQC.
- Résumé : Durée de validité maximale de 100 jours pour les certificats émis à partir du 15 mars 2027 ; réutilisation des validations de domaine limitée à 100 jours.
- Échéance : 2027-03-15
- Effet : autre
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, TLS_SUITE
- Source : <https://github.com/cabforum/servercert/blob/main/docs/BR.md> (source datée du 2025-04-11)

#### CABF-VALIDITE-47J-2029 (CA/Browser Forum — Baseline Requirements, scrutin SC-081v3 (durées de validité des certificats TLS))

- Émetteur, juridiction, nature : CA/Browser Forum, INT, contraignant indirectement (marchés publics, contrats)
- Public visé : Autorités de certification publiques (obligation directe). Tout détenteur de certificats TLS publics en subit l'effet. Ce ne sont pas des exigences PQC.
- Résumé : Durée de validité maximale de 47 jours pour les certificats émis à partir du 15 mars 2029 ; réutilisation des validations de domaine limitée à 10 jours.
- Échéance : 2029-03-15
- Effet : autre
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, TLS_SUITE
- Source : <https://github.com/cabforum/servercert/blob/main/docs/BR.md> (source datée du 2025-04-11)

#### EU-ROADMAP-2030-HAUT-RISQUE (A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography (NIS Cooperation Group, v1.1))

- Émetteur, juridiction, nature : NIS Cooperation Group (groupe de travail PQC), avec la Commission européenne, EU, recommandation
- Public visé : États membres de l'UE. Le texte ne crée aucune obligation directe pour les entreprises ; il découle d'une recommandation de la Commission et n'a pas, à notre lecture, d'effet juridique contraignant.
- Résumé : D'ici le 31 décembre 2030 : transition achevée pour les usages à haut risque (notamment les données devant rester confidentielles au moins 10 ans), mises à jour résistantes au quantique activées par défaut. Après 2030, aucun mécanisme à clé publique vulnérable ne devrait être utilisé seul pour ces usages.
- Échéance : 2030-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, EDDSA
- Source : <https://ec.europa.eu/newsroom/dae/redirection/document/117507> (source datée du 2025-06-23)

#### FR-ANSSI-CALENDRIER (ANSSI — positions sur la transition post-quantique)

- Émetteur, juridiction, nature : ANSSI, FR, recommandation
- Public visé : Administrations, opérateurs et fournisseurs de produits évalués par l'ANSSI (périmètre exact non vérifié).
- Résumé : Selon le même site : déploiement à partir de 2026, usages à haut risque d'ici 2030, transition complète d'ici 2035, en cohérence avec la feuille de route européenne que l'ANSSI diffuse. Non vérifié dans un texte de l'ANSSI.
- Échéance : 2030-12-31
- Effet : recommandé
- Confiance du référentiel : faible (à vérifier dans la source primaire)
- Familles observées concernées : RSA, ECDSA, EDDSA
- Source : <https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/> (source datée du 2026-04-05)

#### EU-ROADMAP-2035 (A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography (NIS Cooperation Group, v1.1))

- Émetteur, juridiction, nature : NIS Cooperation Group (groupe de travail PQC), avec la Commission européenne, EU, recommandation
- Public visé : États membres de l'UE. Le texte ne crée aucune obligation directe pour les entreprises ; il découle d'une recommandation de la Commission et n'a pas, à notre lecture, d'effet juridique contraignant.
- Résumé : D'ici le 31 décembre 2035 : transition achevée pour les usages à risque moyen et, autant que possible, pour les usages à faible risque ; les États visent « autant de systèmes que possible ».
- Échéance : 2035-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, EDDSA
- Source : <https://ec.europa.eu/newsroom/dae/redirection/document/117507> (source datée du 2025-06-23)

#### G7-CEG-CIBLE-2035 (G7 Cyber Expert Group — Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector)

- Émetteur, juridiction, nature : G7 Cyber Expert Group, INT, recommandation
- Public visé : Établissements financiers et autorités financières des pays du G7. Le texte se déclare non prescriptif.
- Résumé : Feuille de route en six phases, explicitement non contraignante : la déclaration « ne fixe ni orientations ni attentes réglementaires ». Elle cite 2035 comme cible générale et 2030-2032 pour les systèmes les plus critiques. Document daté « janvier 2026 » (le 12 janvier selon les notes).
- Échéance : 2035-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, EDDSA
- Source : <https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf> (source datée du 2026-01-12)

#### EU-NIS2-PROPOSITION-PQC (Proposition de modification de la directive NIS2 — COM(2026) 13, procédure 2026/0012(COD))

- Émetteur, juridiction, nature : Commission européenne, EU, projet
- Public visé : États membres (stratégies nationales de cybersécurité). Aucune obligation PQC pour les entreprises, même une fois adoptée.
- Résumé : La proposition obligerait les États membres à adopter, dans leur stratégie nationale de cybersécurité, des politiques de migration vers la PQC. Ce n'est qu'une proposition, encore en commission (ITRE) au Parlement, avec une première lecture indicative le 8 mars 2027, puis une transposition. Le numéro d'article (7(2)(k)) et l'alignement sur 2030/2035 viennent de sources secondaires. Date de la proposition : 14 janv. 2026 selon l'Observatoire législatif, 20 janv. 2026 selon d'autres sources.
- Échéance : non précisée
- Effet : autre
- Confiance du référentiel : moyenne
- Familles observées concernées : RSA, ECDSA, EDDSA
- Source : <https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1884097> (source datée du 2026-01-14)

## 4. Feuille de route de migration

Priorités déduites de l'inventaire. Les échéances citées sont celles du référentiel fourni ; les actions sont des recommandations de méthode, à adapter par le relecteur.

### Horizon 1 : maintenant à fin 2027

1. **Valider l'inventaire.** Relire les 197 constats à confiance faible ou moyenne, confirmer le contexte (production ou test) de chaque emplacement et compléter le questionnaire sur les HSM, KMS, VPN, la PKI et les dépendances fournisseurs, que l'analyse statique ne voit pas.
2. Aucun algorithme déjà obsolète n'a été relevé en production.
3. **Sonder les points TLS exposés** depuis le réseau du client, puis activer l'échange hybride X25519MLKEM768 là où il manque.
4. **Documenter l'inventaire des suites et protocoles et le revoir au moins une fois par an** ; exigences d'inventaire du référentiel : PCI-DSS-12.3.3-INVENTAIRE-SUITES, PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS.
5. **Rendre la cryptographie agile** : regrouper le choix des algorithmes dans une configuration centrale plutôt que dans le code (3 fichier(s) en production fixent un algorithme à clé publique), et vérifier que les bibliothèques et modules certifiés utilisés prendront en charge ML-KEM et ML-DSA.

Échéances du référentiel dans cet horizon :
- CABF-VALIDITE-100J-2027 (2027-03-15, autre) : <https://github.com/cabforum/servercert/blob/main/docs/BR.md>
- CABF-VALIDITE-200J-2026 (2026-03-15, autre) : <https://github.com/cabforum/servercert/blob/main/docs/BR.md>
- EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) : <https://ec.europa.eu/newsroom/dae/redirection/document/117507>
- PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) : <https://www.pcisecuritystandards.org/day-1_t2_7_pci-dss-v4-0_final/>
- PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) : <https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/>

### Horizon 2 : 2028 à 2030

1. **Remplacer d'abord l'échange de clés et le chiffrement à clé publique** (ECDH, X25519/X448, DH, RSA en chiffrement) par ML-KEM ou un mode hybride : 0 occurrence(s) dans 0 fichier(s) ou point(s) ; 11 occurrence(s) RSA dont l'usage (chiffrement ou signature) reste à préciser.
2. **Remplacer ensuite les signatures** (RSA, ECDSA, EdDSA, DSA) par ML-DSA ou SLH-DSA, en coordination avec la PKI, les autorités de certification et les HSM : 88 occurrence(s) dans 19 fichier(s) ou point(s).
3. Cet ordre suit la logique de dépréciation des algorithmes à clé publique décrite dans NIST IR 8547 : vérifier les dates exactes dans le référentiel (section 3).

Échéances du référentiel dans cet horizon :
- CABF-VALIDITE-47J-2029 (2029-03-15, autre) : <https://github.com/cabforum/servercert/blob/main/docs/BR.md>
- EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) : <https://ec.europa.eu/newsroom/dae/redirection/document/117507>
- FR-ANSSI-CALENDRIER (2030-12-31, recommandé) : <https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/>

### Horizon 3 : 2031 à 2035

1. **Terminer la migration avant les dates d'interdiction** : traiter les résidus, y compris le code de test et d'exemple (64 occurrence(s) vulnérables hors production), les dépendances fournisseurs et les équipements à longue durée de vie.
2. Réévaluer les modes hybrides et les tailles de clés symétriques au regard des exigences alors en vigueur ; refaire l'inventaire pour confirmer qu'il ne reste aucun algorithme vulnérable.

Échéances du référentiel dans cet horizon :
- EU-ROADMAP-2035 (2035-12-31, recommandé) : <https://ec.europa.eu/newsroom/dae/redirection/document/117507>
- G7-CEG-CIBLE-2035 (2035-12-31, recommandé) : <https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf>

## 5. Limites de l'analyse

- **Analyse statique uniquement.** Le code et les fichiers de configuration sont lus sans être exécutés ; un algorithme choisi à l'exécution, chargé dynamiquement ou fourni par une dépendance binaire peut échapper à l'analyse.
- **Faux positifs et faux négatifs.** Les règles visent des appels d'API et des directives précises, mais un constat peut concerner du code mort, et une forme d'écriture non prévue peut passer inaperçue. La confiance indiquée pour chaque constat (élevée, moyenne, faible) guide la relecture ; elle ne remplace pas la vérification.
- **Aucune visibilité sur l'exécution, les HSM, les KMS, la PKI interne, les VPN ni les micrologiciels.** Ces éléments relèvent du questionnaire et de l'accès privilégié du partenaire.
- **Sondes TLS.** Elles mesurent ce que voit le poste d'où elles sont lancées. Un proxy ou un équipement d'inspection TLS sur le chemin fausse la mesure : il faut les lancer depuis un réseau sans interception.
- **Ni certification, ni audit de conformité, ni avis juridique.** Ce rapport aide à préparer une démarche de conformité ; il ne l'atteste pas.
- **Le relecteur humain reste responsable** du tri des constats, de l'applicabilité des exigences au client et des recommandations finales.
- **Aucune cryptographie maison.** Ce rapport ne recommande jamais d'implémenter soi-même un algorithme : la migration doit s'appuyer sur des bibliothèques et modules cryptographiques reconnus et, lorsque c'est exigé, certifiés.
- **Référentiel daté.** Les exigences citées sont celles du fichier regles.json fourni (version 2026-11-22) ; les textes évoluent et doivent être revérifiés à la source avant toute décision.

## 6. Liste de contrôle du relecteur

- [ ] Vérifier un échantillon d'au moins dix constats à confiance élevée en ouvrant le fichier à la ligne indiquée.
- [ ] Trier chaque constat à confiance faible ou moyenne : confirmer, requalifier ou écarter, et le noter.
- [ ] Confirmer le contexte (production, test, exemple, documentation) des emplacements ambigus.
- [ ] Vérifier qu'aucun extrait du rapport ne contient de secret ; les clés privées trouvées doivent être signalées au client.
- [ ] Pour chaque point TLS, vérifier que la sonde a été lancée depuis un réseau sans proxy d'interception.
- [ ] Vérifier la version et la date du référentiel, puis ouvrir chaque source citée pour confirmer l'exigence et l'échéance.
- [ ] Confirmer avec le client quelles exigences lui sont réellement applicables (secteur, juridiction, contrats).
- [ ] Compléter le questionnaire HSM, KMS, VPN, PKI et dépendances fournisseurs.
- [ ] Adapter la feuille de route au contexte du client, puis dater et signer le rapport.

## Annexe : méthode

Constats produits par pqc-inventaire 0.1.0 (107 règles).

constats.json : 86 fichier(s) analysé(s) ; ignorés : 0 binaire(s), 0 trop volumineux, 0 exclu(s).

**Classes utilisées**

- Vulnérable (algorithme de Shor) (`vulnerable_shor`) : cryptographie à clé publique classique, cassable par un ordinateur quantique (algorithme de Shor)
- Obsolète dès aujourd'hui (`obsolete_classique`) : algorithme ou protocole déjà faible avec des moyens classiques
- Hybride classique + post-quantique (`hybride`) : échange de clés combinant un algorithme classique et un algorithme post-quantique
- Post-quantique normalisé (`pqc`) : algorithme post-quantique normalisé par le NIST (FIPS 203, 204, 205 ; FIPS 206 en projet)
- Symétrique (taille de clé à vérifier) (`symetrique`) : chiffrement symétrique ; l'impact quantique dépend de la taille de clé
- Hachage robuste (`hachage_ok`) : fonction de hachage robuste
- Inventaire TLS (`inventaire`) : suite ou protocole TLS relevé pour l'inventaire

---

Document produit par l'Atelier PQC avec pqc-inventaire 0.1.0.
