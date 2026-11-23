# Préparation post-quantique : inventaire cryptographique

## paramiko-3.5.1 (démonstration, bibliothèque libre)

| | |
|---|---|
| Client | paramiko-3.5.1 (démonstration, bibliothèque libre) |
| Préparé par | Atelier PQC |
| Date | 2026-11-22 |
| Sources analysées | constats.json (code, 227 fichier(s)) |
| Référentiel réglementaire | regles.json, version 2026-11-22 (6 texte(s)) |
| Statut | Projet à relire, compléter et signer par le relecteur |

> Ce document est un produit d'information issu d'une analyse automatisée, relu par une personne. Il ne constitue ni un avis juridique, ni une certification, ni un audit de conformité.
>
> **Avertissement du référentiel** : Référentiel établi le 22 novembre 2026 à partir de notes de recherche datées et de sources primaires consultées le même jour. Ce n'est pas un avis juridique : l'applicabilité d'un texte à une organisation donnée doit être confirmée par un juriste ou par l'autorité compétente. Pour la plupart des entreprises privées situées hors du périmètre PCI DSS et hors des marchés publics (notamment fédéraux américains), aucune échéance de migration post-quantique contraignante n'existe à ce jour : les autres textes sont des recommandations, des projets ou des obligations qui visent des administrations. Conventions : « nature » décrit la portée du texte pour le public qu'il vise, pas pour le client ; « echeance » est la date à partir de laquelle, ou au plus tard à laquelle, l'effet s'applique ; quand le texte ne donne qu'une année, la date retenue est le 31 décembre de cette année, et quand il ne donne qu'un mois, le dernier jour de ce mois. « confiance » : elevee = vérifié dans le texte primaire le 22/11/2026 ; moyenne = partiellement vérifié (date ou libellé principal confirmé par une source officielle, le reste par des sources secondaires concordantes) ; faible = non vérifié dans une source primaire. Une exigence « faible » ne doit pas être citée à un client sans vérification préalable.

## 1. Synthèse

L'analyse a relevé **277 constats** répartis en **11 familles cryptographiques**, dont **73** dans du code ou des configurations classés « production ». 211 constats portent sur de la cryptographie à clé publique classique, vulnérable à un futur ordinateur quantique (algorithme de Shor) ; 30 portent sur des algorithmes ou protocoles déjà obsolètes aujourd'hui.

### Répartition par classe

| Classe | Constats | dont production | Familles |
|---|---:|---:|---|
| Vulnérable (algorithme de Shor) | 211 | 35 | RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA |
| Obsolète dès aujourd'hui | 30 | 20 | 3DES, MD5, SHA1 |
| Symétrique (taille de clé à vérifier) | 35 | 17 | AES |
| Hachage robuste | 1 | 1 | SHA2 |

### Principaux risques

Classement par gravité de la classe, contexte (la production compte davantage que les tests) et confiance du constat.

1. **RSA** (RSA (chiffrement, signature, échange de clés)) : 81 occurrence(s), dont 3 en production ; cryptographie à clé publique cassable par l'algorithme de Shor (chiffrement, échange de clés, signature). Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31), CABF-VALIDITE-200J-2026 (2026-03-15), et 8 autre(s), voir la section 3.
2. **DSA** (DSA) : 36 occurrence(s), dont 15 en production ; signatures falsifiables une fois un ordinateur quantique disponible ; migration à coordonner avec la PKI. Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31), EU-NIS2-PROPOSITION-PQC (—), et 5 autre(s), voir la section 3.
3. **SHA1** (SHA-1) : 16 occurrence(s), dont 13 en production ; algorithme déjà faible ou cassé avec des moyens classiques : à remplacer sans attendre l'ordinateur quantique. Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), CABF-SHA1-FIN-2026 (2026-09-15).
4. **ECDSA** (Signatures ECDSA) : 62 occurrence(s), dont 9 en production ; signatures falsifiables une fois un ordinateur quantique disponible ; migration à coordonner avec la PKI. Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31), CABF-VALIDITE-200J-2026 (2026-03-15), et 8 autre(s), voir la section 3.
5. **X25519_X448** (Échange de clés X25519 / X448) : 5 occurrence(s), dont 4 en production ; échange de clés cassable par un ordinateur quantique ; les échanges chiffrés aujourd'hui peuvent être enregistrés puis déchiffrés plus tard (« collecter maintenant, déchiffrer plus tard »). Exigences les plus pressantes : PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31), EU-NIS2-PROPOSITION-PQC (—), EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31), et 4 autre(s), voir la section 3.

### Points TLS sondés

Aucun point TLS n'a été sondé. La sonde doit être lancée depuis le réseau du client ou du partenaire.

## 2. Inventaire

### 2.1 Par famille

| Famille | Classe | Occurrences | Production | Test / exemple / doc. | Confiance (é / m / f) | Algorithmes observés |
|---|---|---:|---:|---:|---|---|
| RSA | Vulnérable (algorithme de Shor) | 81 | 3 | 78 | 81 / 0 / 0 | RSA, RSA-1024, RSA-2048, RSA-PSS |
| ECDSA | Vulnérable (algorithme de Shor) | 62 | 9 | 53 | 54 / 1 / 7 | EC, EC-P-256, EC-P-384, EC-P-521, ECDSA, ECDSA-P-256 et 2 autre(s) |
| ECDH | Vulnérable (algorithme de Shor) | 2 | 2 | 0 | 2 / 0 / 0 | ECDH |
| EDDSA | Vulnérable (algorithme de Shor) | 25 | 2 | 23 | 20 / 0 / 5 | Ed25519, Ed448 |
| X25519_X448 | Vulnérable (algorithme de Shor) | 5 | 4 | 1 | 5 / 0 / 0 | X25519 |
| DSA | Vulnérable (algorithme de Shor) | 36 | 15 | 21 | 33 / 3 / 0 | DSA, DSA-1024 |
| AES | Symétrique (taille de clé à vérifier) | 35 | 17 | 18 | 4 / 0 / 31 | AES, AES-128-CBC, AES-128-CTR, AES-192-CBC, AES-192-CTR, AES-256-CBC et 2 autre(s) |
| 3DES | Obsolète dès aujourd'hui | 3 | 3 | 0 | 0 / 0 / 3 | 3DES |
| MD5 | Obsolète dès aujourd'hui | 11 | 4 | 7 | 1 / 0 / 10 | HMAC-MD5, MD5 |
| SHA1 | Obsolète dès aujourd'hui | 16 | 13 | 3 | 12 / 0 / 4 | HMAC-SHA-1, SHA-1 |
| SHA2 | Hachage robuste | 1 | 1 | 0 | 1 / 0 / 0 | SHA-256 |

### 2.2 Par emplacement

| Emplacement | Famille | Détail | Contexte | Confiance | Règle | Extrait |
|---|---|---|---|---|---|---|
| `demos/demo.py:76` | RSA | RSA | exemple | élevée | `py-paramiko-cle` | `key = paramiko.RSAKey.from_private_key_file(path)` |
| `demos/demo.py:79` | RSA | RSA | exemple | élevée | `py-paramiko-cle` | `key = paramiko.RSAKey.from_private_key_file(path, password)` |
| `demos/demo.py:87` | DSA | DSA | exemple | élevée | `py-paramiko-cle` | `key = paramiko.DSSKey.from_private_key_file(path)` |
| `demos/demo.py:90` | DSA | DSA | exemple | élevée | `py-paramiko-cle` | `key = paramiko.DSSKey.from_private_key_file(path, password)` |
| `demos/demo_server.py:36` | RSA | RSA | exemple | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey(filename="test_rsa.key")` |
| `demos/demo_server.py:51` | RSA | RSA | exemple | élevée | `py-paramiko-cle` | `good_pub_key = paramiko.RSAKey(data=decodebytes(data))` |
| `demos/test_rsa.key:1` | RSA | RSA-1024 ; clé privée présente dans les fichiers analysés | exemple | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `demos/user_rsa_key:1` | RSA | RSA-1024 ; clé privée présente dans les fichiers analysés | exemple | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `demos/user_rsa_key.pub:1` | RSA | RSA-1024, vérification de signature ; clé publique SSH | exemple | élevée | `ssh-cle-publique` | `ssh-rsa [clé masquée]` |
| `paramiko/__init__.py:69` | DSA | DSA ; import du module, usage non confirmé | production | moyenne | `py-import-module` | `from paramiko.dsskey import DSSKey` |
| `paramiko/client.py:34` | DSA | DSA ; import du module, usage non confirmé | production | moyenne | `py-import-module` | `from paramiko.dsskey import DSSKey` |
| `paramiko/client.py:769` | ECDSA | ECDSA ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `(ECDSAKey, "ecdsa"),` |
| `paramiko/client.py:770` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `(Ed25519Key, "ed25519"),` |
| `paramiko/config.py:449` | SHA1 | SHA-1, empreinte | production | élevée | `py-hashlib` | `"%C": sha1(tohash.encode()).hexdigest(),` |
| `paramiko/dsskey.py:112` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `key = dsa.DSAPrivateNumbers(` |
| `paramiko/dsskey.py:114` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `public_numbers=dsa.DSAPublicNumbers(` |
| `paramiko/dsskey.py:116` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `parameter_numbers=dsa.DSAParameterNumbers(` |
| `paramiko/dsskey.py:121` | SHA1 | SHA-1, empreinte | production | élevée | `py-cryptography-hash` | `sig = key.sign(data, hashes.SHA1())` |
| `paramiko/dsskey.py:152` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `key = dsa.DSAPublicNumbers(` |
| `paramiko/dsskey.py:154` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `parameter_numbers=dsa.DSAParameterNumbers(` |
| `paramiko/dsskey.py:159` | SHA1 | SHA-1, empreinte | production | élevée | `py-cryptography-hash` | `key.verify(signature, data, hashes.SHA1())` |
| `paramiko/dsskey.py:166` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `key = dsa.DSAPrivateNumbers(` |
| `paramiko/dsskey.py:168` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `public_numbers=dsa.DSAPublicNumbers(` |
| `paramiko/dsskey.py:170` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `parameter_numbers=dsa.DSAParameterNumbers(` |
| `paramiko/dsskey.py:184` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `key = dsa.DSAPrivateNumbers(` |
| `paramiko/dsskey.py:186` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `public_numbers=dsa.DSAPublicNumbers(` |
| `paramiko/dsskey.py:188` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `parameter_numbers=dsa.DSAParameterNumbers(` |
| `paramiko/dsskey.py:211` | DSA | DSA, signature | production | élevée | `py-cryptography-dsa` | `numbers = dsa.generate_private_key(` |
| `paramiko/ecdsakey.py:103` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `_ECDSACurve(ec.SECP256R1, "nistp256"),` |
| `paramiko/ecdsakey.py:104` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `_ECDSACurve(ec.SECP384R1, "nistp384"),` |
| `paramiko/ecdsakey.py:105` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `_ECDSACurve(ec.SECP521R1, "nistp521"),` |
| `paramiko/ecdsakey.py:221` | ECDSA | ECDSA, signature / vérification de signature | production | élevée | `py-cryptography-ec` | `ecdsa = ec.ECDSA(self.ecdsa_curve.hash_object())` |
| `paramiko/ecdsakey.py:239` | ECDSA | ECDSA, signature / vérification de signature | production | élevée | `py-cryptography-ec` | `signature, data, ec.ECDSA(self.ecdsa_curve.hash_object())` |
| `paramiko/ecdsakey.py:277` | ECDSA | EC, génération de clé ; clé EC : ECDSA ou ECDH selon l'usage | production | élevée | `py-cryptography-ec` | `private_key = ec.generate_private_key(curve, backend=default_backend())` |
| `paramiko/ecdsakey.py:314` | ECDSA | EC, génération de clé ; clé EC : ECDSA ou ECDH selon l'usage | production | élevée | `py-cryptography-ec` | `key = ec.derive_private_key(` |
| `paramiko/hostkeys.py:296` | SHA1 | SHA-1, empreinte | production | élevée | `py-hashlib` | `salt = os.urandom(sha1().digest_size)` |
| `paramiko/hostkeys.py:301` | SHA1 | SHA-1, empreinte | production | élevée | `py-hashlib` | `assert len(salt) == sha1().digest_size` |
| `paramiko/hostkeys.py:302` | SHA1 | HMAC-SHA-1, MAC | production | élevée | `py-hmac` | `hmac = HMAC(salt, b(hostname), sha1).digest()` |
| `paramiko/kex_curve25519.py:30` | X25519_X448 | X25519, accord / dérivation de clé | production | élevée | `py-cryptography-xdh` | `X25519PrivateKey.generate()` |
| `paramiko/kex_curve25519.py:45` | X25519_X448 | X25519, accord / dérivation de clé | production | élevée | `py-cryptography-xdh` | `self.key = X25519PrivateKey.generate()` |
| `paramiko/kex_curve25519.py:71` | X25519_X448 | X25519, accord / dérivation de clé | production | élevée | `py-cryptography-xdh` | `peer_key = X25519PublicKey.from_public_bytes(peer_key_bytes)` |
| `paramiko/kex_curve25519.py:109` | X25519_X448 | X25519, accord / dérivation de clé | production | élevée | `py-cryptography-xdh` | `peer_key = X25519PublicKey.from_public_bytes(peer_key_bytes)` |
| `paramiko/kex_ecdh_nist.py:59` | ECDSA | EC, génération de clé ; clé EC : ECDSA ou ECDH selon l'usage | production | élevée | `py-cryptography-ec` | `self.P = ec.generate_private_key(self.curve, default_backend())` |
| `paramiko/kex_ecdh_nist.py:71` | ECDH | ECDH, accord / dérivation de clé | production | élevée | `py-cryptography-ec` | `K = self.P.exchange(ec.ECDH(), self.Q_C)` |
| `paramiko/kex_ecdh_nist.py:117` | ECDH | ECDH, accord / dérivation de clé | production | élevée | `py-cryptography-ec` | `K = self.P.exchange(ec.ECDH(), self.Q_S)` |
| `paramiko/kex_gss.py:230` | SHA1 | SHA-1, empreinte | production | élevée | `py-hashlib` | `H = sha1(str(hm)).digest()` |
| `paramiko/kex_gss.py:269` | SHA1 | SHA-1, empreinte | production | élevée | `py-hashlib` | `H = sha1(hm.asbytes()).digest()` |
| `paramiko/kex_gss.py:532` | SHA1 | SHA-1, empreinte | production | élevée | `py-hashlib` | `H = sha1(hm.asbytes()).digest()` |
| `paramiko/kex_gss.py:634` | SHA1 | SHA-1, empreinte | production | élevée | `py-hashlib` | `H = sha1(hm.asbytes()).digest()` |
| `paramiko/pkey.py:101` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"AES-128-CBC": {` |
| `paramiko/pkey.py:107` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"AES-256-CBC": {` |
| `paramiko/pkey.py:113` | 3DES | 3DES ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"DES-EDE3-CBC": {` |
| `paramiko/pkey.py:358` | MD5 | MD5, empreinte | production | élevée | `py-hashlib` | `return md5(self.asbytes()).digest()` |
| `paramiko/pkey.py:369` | SHA2 | SHA-256, empreinte | production | élevée | `py-hashlib` | `hashy = sha256(bytes(self))` |
| `paramiko/pkey.py:632` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `if cipher == b("aes256-cbc"):` |
| `paramiko/pkey.py:634` | AES | AES-256-CTR ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `elif cipher == b("aes256-ctr"):` |
| `paramiko/pkey.py:667` | AES | AES, chiffrement / déchiffrement | production | élevée | `py-cryptography-symetrique` | `decryptor = Cipher(` |
| `paramiko/rsakey.py:127` | RSA | RSA | production | élevée | `py-cryptography-rsa` | `padding=padding.PKCS1v15(),` |
| `paramiko/rsakey.py:155` | RSA | RSA | production | élevée | `py-cryptography-rsa` | `sign, data, padding.PKCS1v15(), self.HASHES[sig_algorithm]()` |
| `paramiko/rsakey.py:188` | RSA | RSA, génération de clé | production | élevée | `py-cryptography-rsa` | `key = rsa.generate_private_key(` |
| `paramiko/sftp_server.py:85` | MD5 | MD5 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `_hash_class = {"sha1": sha1, "md5": md5}` |
| `paramiko/sftp_server.py:85` | SHA1 | SHA-1 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `_hash_class = {"sha1": sha1, "md5": md5}` |
| `paramiko/transport.py:98` | DSA | DSA ; import du module, usage non confirmé | production | moyenne | `py-import-module` | `from paramiko.dsskey import DSSKey` |
| `paramiko/transport.py:180` | AES | AES-128-CTR ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes128-ctr",` |
| `paramiko/transport.py:181` | AES | AES-192-CTR ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes192-ctr",` |
| `paramiko/transport.py:182` | AES | AES-256-CTR ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes256-ctr",` |
| `paramiko/transport.py:183` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes128-cbc",` |
| `paramiko/transport.py:184` | AES | AES-192-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes192-cbc",` |
| `paramiko/transport.py:185` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes256-cbc",` |
| `paramiko/transport.py:186` | 3DES | 3DES ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"3des-cbc",` |
| `paramiko/transport.py:195` | SHA1 | HMAC-SHA-1 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"hmac-sha1",` |
| `paramiko/transport.py:196` | MD5 | HMAC-MD5 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"hmac-md5",` |
| `paramiko/transport.py:243` | AES | AES-128-CTR ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes128-ctr": {` |
| `paramiko/transport.py:249` | AES | AES-192-CTR ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes192-ctr": {` |
| `paramiko/transport.py:255` | AES | AES-256-CTR ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes256-ctr": {` |
| `paramiko/transport.py:261` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes128-cbc": {` |
| `paramiko/transport.py:267` | AES | AES-192-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes192-cbc": {` |
| `paramiko/transport.py:273` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"aes256-cbc": {` |
| `paramiko/transport.py:279` | 3DES | 3DES ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"3des-cbc": {` |
| `paramiko/transport.py:302` | SHA1 | HMAC-SHA-1 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"hmac-sha1": {"class": sha1, "size": 20},` |
| `paramiko/transport.py:308` | MD5 | HMAC-MD5 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"hmac-md5": {"class": md5, "size": 16},` |
| `setup.py:45` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | production | faible | `py-chaine-algorithme` | `"ed25519": [],` |
| `tests/_support/dss.key:1` | DSA | DSA-1024 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN DSA PRIVATE KEY----- [contenu masqué]` |
| `tests/_support/ecdsa-256.key:1` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/_support/ed25519.key:1` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/_support/ed448.key:1` | EDDSA | Ed448 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN PRIVATE KEY----- [contenu masqué]` |
| `tests/_support/rsa-lonely.key:1` | RSA | RSA-1024 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `tests/_support/rsa.key:1` | RSA | RSA-1024 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `tests/_util.py:176` | RSA | RSA-2048, génération de clé | test | élevée | `py-cryptography-rsa` | `private_key = rsa.generate_private_key(` |
| `tests/_util.py:183` | RSA | RSA-PSS, signature / vérification de signature | test | élevée | `py-cryptography-rsa` | `padding.PSS(` |
| `tests/_util.py:184` | SHA1 | SHA-1, empreinte | test | élevée | `py-cryptography-hash` | `mgf=padding.MGF1(hashes.SHA1()),` |
| `tests/_util.py:187` | SHA1 | SHA-1, empreinte | test | élevée | `py-cryptography-hash` | `hashes.SHA1(),` |
| `tests/_util.py:215` | DSA | DSA | test | élevée | `py-paramiko-cle` | `paranoid_key = DSSKey.from_private_key_file(_support("dss.key"))` |
| `tests/_util.py:411` | RSA | RSA | test | élevée | `py-paramiko-cle` | `hostkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/agent.py:135` | RSA | RSA | test | élevée | `py-paramiko-cle` | `inner_key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:88` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key = DSSKey.from_private_key_file(_support("dss.key"))` |
| `tests/auth.py:163` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:207` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:223` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:238` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:249` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:261` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:272` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:292` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:304` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/auth.py:316` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/badhash_key1.ed25519.key:1` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/badhash_key2.ed25519.key:1` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/conftest.py:88` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/pkey.py:122` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/pkey.py:160` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `edkey = Ed25519Key.from_private_key_file(_support("ed25519.key"))` |
| `tests/pkey.py:176` | ECDSA | ECDSA ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert key.algorithm_name == "ECDSA"` |
| `tests/pkey.py:178` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert key.algorithm_name == "ED25519"` |
| `tests/pkey.py:209` | RSA | RSA | test | élevée | `py-paramiko-cle` | `assert RSAKey.identifiers() == [` |
| `tests/pkey.py:219` | DSA | DSA | test | élevée | `py-paramiko-cle` | `assert DSSKey.identifiers() == ["ssh-dss"]` |
| `tests/pkey.py:222` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `assert Ed25519Key.identifiers() == ["ssh-ed25519"]` |
| `tests/pkey.py:225` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `assert ECDSAKey.identifiers() == [` |
| `tests/test_client.py:175` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(keypath)` |
| `tests/test_client.py:178` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.ECDSAKey.from_private_key_file(keypath)` |
| `tests/test_client.py:197` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_client.py:198` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = paramiko.RSAKey(data=host_key.asbytes())` |
| `tests/test_client.py:286` | ECDSA | ECDSA ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"ecdsa": "ecdsa-sha2-nistp256",` |
| `tests/test_client.py:295` | ECDSA | ECDSA ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `(["rsa", "ecdsa-256"], ["ecdsa"]),  # ECDSA success` |
| `tests/test_client.py:330` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `for type_ in ("rsa", "dss", "ecdsa-256", "ed25519"):` |
| `tests/test_client.py:345` | EDDSA | Ed25519 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `for type_ in ("rsa", "dss", "ecdsa-256", "ed25519"):` |
| `tests/test_client.py:388` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `public_host_key = paramiko.ECDSAKey.from_private_key_file(key_file)` |
| `tests/test_client.py:410` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_client.py:411` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = paramiko.RSAKey(data=host_key.asbytes())` |
| `tests/test_client.py:510` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_client.py:511` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = paramiko.RSAKey(data=host_key.asbytes())` |
| `tests/test_client.py:666` | ECDSA | ECDSA, génération de clé | test | élevée | `py-paramiko-cle` | `host_key = paramiko.ECDSAKey.generate()` |
| `tests/test_client.py:671` | RSA | RSA-2048, génération de clé | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.generate(2048)` |
| `tests/test_dss_openssh.key:1` | DSA | DSA ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/test_dss_password.key:1` | DSA | DSA ; clé privée présente dans les fichiers analysés ; clé chiffrée, paramètres non lus | test | élevée | `pem-cle-privee` | `-----BEGIN DSA PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ecdsa_384.key:1` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ecdsa_384_openssh.key:1` | ECDSA | ECDSA-P-384 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ecdsa_521.key:1` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ecdsa_password_256.key:1` | ECDSA | EC ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés ; clé chiffrée, paramètres non lus | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ecdsa_password_384.key:1` | ECDSA | EC ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés ; clé chiffrée, paramètres non lus | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ecdsa_password_521.key:1` | ECDSA | EC ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés ; clé chiffrée, paramètres non lus | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ed25519-funky-padding.key:1` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ed25519-funky-padding_password.key:1` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/test_ed25519_password.key:1` | EDDSA | Ed25519 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/test_hostkeys.py:39` | EDDSA | Ed25519, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-ed25519 [clé masquée]` |
| `tests/test_hostkeys.py:41` | ECDSA | ECDSA-P-256, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ecdsa-sha2-nistp256 [clé masquée]` |
| `tests/test_hostkeys.py:97` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = paramiko.RSAKey(data=decodebytes(keyblob))` |
| `tests/test_hostkeys.py:120` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = paramiko.RSAKey(data=decodebytes(keyblob))` |
| `tests/test_hostkeys.py:121` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key_dss = paramiko.DSSKey(data=decodebytes(keyblob_dss))` |
| `tests/test_kex.py:31` | ECDSA | EC ; clé EC : ECDSA ou ECDH selon l'usage ; import du module, usage non confirmé | test | moyenne | `py-import-module` | `from cryptography.hazmat.primitives.asymmetric import ec` |
| `tests/test_kex.py:135` | X25519_X448 | X25519, accord / dérivation de clé | test | élevée | `py-cryptography-xdh` | `static_x25519_key = x25519.X25519PrivateKey.from_private_bytes(` |
| `tests/test_kex_gss.py:83` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_kex_gss.py:99` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_kex_gss.py:100` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = paramiko.RSAKey(data=host_key.asbytes())` |
| `tests/test_packetizer.py:48` | AES | AES-CBC, chiffrement / déchiffrement | test | élevée | `py-cryptography-symetrique` | `encryptor = Cipher(` |
| `tests/test_packetizer.py:78` | AES | AES-CBC, chiffrement / déchiffrement | test | élevée | `py-cryptography-symetrique` | `decryptor = Cipher(` |
| `tests/test_packetizer.py:102` | AES | AES-CBC, chiffrement / déchiffrement | test | élevée | `py-cryptography-symetrique` | `encryptor = Cipher(` |
| `tests/test_pkey.py:52` | RSA | RSA-1024, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-rsa [clé masquée]` |
| `tests/test_pkey.py:53` | DSA | DSA, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-dss [clé masquée]` |
| `tests/test_pkey.py:54` | ECDSA | ECDSA-P-256, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ecdsa-sha2-nistp256 [clé masquée]` |
| `tests/test_pkey.py:55` | ECDSA | ECDSA-P-384, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ecdsa-sha2-nistp384 [clé masquée]` |
| `tests/test_pkey.py:56` | ECDSA | ECDSA-P-521, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ecdsa-sha2-nistp521 [clé masquée]` |
| `tests/test_pkey.py:57` | RSA | RSA-2048, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-rsa [clé masquée]` |
| `tests/test_pkey.py:60` | DSA | DSA, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-dss [clé masquée]` |
| `tests/test_pkey.py:61` | ECDSA | ECDSA-P-384, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ecdsa-sha2-nistp384 [clé masquée]` |
| `tests/test_pkey.py:76` | RSA | RSA-1024 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `tests/test_pkey.py:94` | DSA | DSA-1024 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN DSA PRIVATE KEY----- [contenu masqué]` |
| `tests/test_pkey.py:109` | ECDSA | EC-P-256 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_pkey.py:117` | ECDSA | EC-P-384 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_pkey.py:126` | ECDSA | EC-P-521 ; clé EC : ECDSA ou ECDH selon l'usage ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN EC PRIVATE KEY----- [contenu masqué]` |
| `tests/test_pkey.py:158` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_pkey.py:170` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key2 = RSAKey.from_private_key(s)` |
| `tests/test_pkey.py:181` | RSA | RSA | test | élevée | `py-paramiko-cle` | `RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_pkey.py:186` | RSA | RSA | test | élevée | `py-paramiko-cle` | `RSAKey.from_private_key_file(_support("blank_rsa.key"))` |
| `tests/test_pkey.py:189` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey.from_private_key_file(` |
| `tests/test_pkey.py:200` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key = DSSKey.from_private_key_file(_support("dss.key"))` |
| `tests/test_pkey.py:212` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key2 = DSSKey.from_private_key(s)` |
| `tests/test_pkey.py:216` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key = DSSKey.from_private_key_file(` |
| `tests/test_pkey.py:228` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_pkey.py:230` | RSA | RSA | test | élevée | `py-paramiko-cle` | `pub = RSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:237` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key = DSSKey.from_private_key_file(_support("dss.key"))` |
| `tests/test_pkey.py:239` | DSA | DSA | test | élevée | `py-paramiko-cle` | `pub = DSSKey(data=key.asbytes())` |
| `tests/test_pkey.py:245` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_pkey.py:255` | RSA | RSA | test | élevée | `py-paramiko-cle` | `pub = RSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:270` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key = DSSKey.from_private_key_file(_support("dss.key"))` |
| `tests/test_pkey.py:280` | DSA | DSA | test | élevée | `py-paramiko-cle` | `pub = DSSKey(data=key.asbytes())` |
| `tests/test_pkey.py:285` | RSA | RSA-1024, génération de clé | test | élevée | `py-paramiko-cle` | `key = RSAKey.generate(1024)` |
| `tests/test_pkey.py:291` | DSA | DSA-1024, génération de clé | test | élevée | `py-paramiko-cle` | `key = DSSKey.generate(1024)` |
| `tests/test_pkey.py:297` | ECDSA | ECDSA, génération de clé | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.generate()` |
| `tests/test_pkey.py:304` | ECDSA | ECDSA-P-256, génération de clé | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.generate(bits=256)` |
| `tests/test_pkey.py:311` | ECDSA | ECDSA-P-384, génération de clé | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.generate(bits=384)` |
| `tests/test_pkey.py:318` | ECDSA | ECDSA-P-521, génération de clé | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.generate(bits=521)` |
| `tests/test_pkey.py:326` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("ecdsa-256.key"))` |
| `tests/test_pkey.py:338` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key2 = ECDSAKey.from_private_key(s)` |
| `tests/test_pkey.py:342` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(` |
| `tests/test_pkey.py:354` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("ecdsa-256.key"))` |
| `tests/test_pkey.py:356` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `pub = ECDSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:363` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("ecdsa-256.key"))` |
| `tests/test_pkey.py:374` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `pub = ECDSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:378` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("test_ecdsa_384.key"))` |
| `tests/test_pkey.py:390` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key2 = ECDSAKey.from_private_key(s)` |
| `tests/test_pkey.py:394` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(` |
| `tests/test_pkey.py:413` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `ECDSAKey.from_private_key_file(path)` |
| `tests/test_pkey.py:417` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("test_ecdsa_384.key"))` |
| `tests/test_pkey.py:419` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `pub = ECDSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:426` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("test_ecdsa_384.key"))` |
| `tests/test_pkey.py:437` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `pub = ECDSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:441` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("test_ecdsa_521.key"))` |
| `tests/test_pkey.py:456` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key2 = ECDSAKey.from_private_key(s)` |
| `tests/test_pkey.py:460` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(` |
| `tests/test_pkey.py:472` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("test_ecdsa_521.key"))` |
| `tests/test_pkey.py:474` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `pub = ECDSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:481` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(_support("test_ecdsa_521.key"))` |
| `tests/test_pkey.py:492` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `pub = ECDSAKey(data=key.asbytes())` |
| `tests/test_pkey.py:496` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey.from_private_key_file(` |
| `tests/test_pkey.py:512` | RSA | RSA | test | élevée | `py-paramiko-cle` | `RSAKey.from_private_key_file(` |
| `tests/test_pkey.py:522` | DSA | DSA | test | élevée | `py-paramiko-cle` | `key = DSSKey.from_private_key_file(` |
| `tests/test_pkey.py:533` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey.from_private_key_file(` |
| `tests/test_pkey.py:549` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey(filename=file_, password=password)` |
| `tests/test_pkey.py:556` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key2 = RSAKey(filename=newfile, password=newpassword)` |
| `tests/test_pkey.py:563` | RSA | RSA | test | élevée | `py-paramiko-cle` | `RSAKey.from_private_key_file(_support("test_rsa_openssh_nopad.key"))` |
| `tests/test_pkey.py:566` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_pkey.py:571` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `key1 = Ed25519Key.from_private_key_file(_support("ed25519.key"))` |
| `tests/test_pkey.py:572` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `key2 = Ed25519Key.from_private_key_file(` |
| `tests/test_pkey.py:579` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `Ed25519Key.from_private_key_file(` |
| `tests/test_pkey.py:585` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `Ed25519Key.from_private_key_file(` |
| `tests/test_pkey.py:591` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `key = Ed25519Key.from_private_key_file(_support("ed25519.key"))` |
| `tests/test_pkey.py:593` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `pub = Ed25519Key(data=key.asbytes())` |
| `tests/test_pkey.py:605` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `original = Ed25519Key.from_private_key_file(` |
| `tests/test_pkey.py:608` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `generated = Ed25519Key.from_private_key_file(` |
| `tests/test_pkey.py:615` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `Ed25519Key.from_private_key_file(` |
| `tests/test_pkey.py:625` | EDDSA | Ed25519 | test | élevée | `py-paramiko-cle` | `key = Ed25519Key.from_private_key(pkey_fileobj)` |
| `tests/test_pkey.py:635` | RSA | RSA | test | élevée | `py-paramiko-cle` | `key = RSAKey(filename=file_, password=password)` |
| `tests/test_pkey.py:658` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey(filename=source, password=password)` |
| `tests/test_pkey.py:685` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `key = ECDSAKey(filename=source, password=password)` |
| `tests/test_pkey.py:692` | ECDSA | ECDSA | test | élevée | `py-paramiko-cle` | `reloaded = ECDSAKey(filename=new, password=newpassword)` |
| `tests/test_rsa.key.pub:1` | RSA | RSA-1024, vérification de signature ; clé publique SSH | test | élevée | `ssh-cle-publique` | `ssh-rsa [clé masquée]` |
| `tests/test_rsa_openssh.key:1` | RSA | RSA-2048 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/test_rsa_openssh_nopad.key:1` | RSA | RSA-2048 ; clé privée présente dans les fichiers analysés | test | élevée | `pem-cle-privee` | `-----BEGIN OPENSSH PRIVATE KEY----- [contenu masqué]` |
| `tests/test_rsa_password.key:1` | RSA | RSA ; clé privée présente dans les fichiers analysés ; clé chiffrée, paramètres non lus | test | élevée | `pem-cle-privee` | `-----BEGIN RSA PRIVATE KEY----- [contenu masqué]` |
| `tests/test_sftp.py:608` | SHA1 | SHA-1 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `sum = f.check("sha1")` |
| `tests/test_sftp.py:613` | MD5 | MD5 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `sum = f.check("md5", 0, 512)` |
| `tests/test_sftp.py:618` | MD5 | MD5 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `sum = f.check("md5", 0, 0, 510)` |
| `tests/test_ssh_exception.py:60` | RSA | RSA-2048, génération de clé | test | élevée | `py-paramiko-cle` | `got_key = RSAKey.generate(2048)` |
| `tests/test_ssh_exception.py:61` | RSA | RSA-2048, génération de clé | test | élevée | `py-paramiko-cle` | `wanted_key = RSAKey.generate(2048)` |
| `tests/test_ssh_gss.py:92` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_ssh_gss.py:103` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = paramiko.RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_ssh_gss.py:104` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = paramiko.RSAKey(data=host_key.asbytes())` |
| `tests/test_transport.py:119` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_transport.py:120` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = RSAKey(data=host_key.asbytes())` |
| `tests/test_transport.py:146` | AES | AES-192-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `self.assertTrue(("aes256-cbc", "aes192-cbc") != o.ciphers)` |
| `tests/test_transport.py:146` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `self.assertTrue(("aes256-cbc", "aes192-cbc") != o.ciphers)` |
| `tests/test_transport.py:147` | AES | AES-192-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `o.ciphers = ("aes256-cbc", "aes192-cbc")` |
| `tests/test_transport.py:147` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `o.ciphers = ("aes256-cbc", "aes192-cbc")` |
| `tests/test_transport.py:148` | AES | AES-192-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `self.assertEqual(("aes256-cbc", "aes192-cbc"), o.ciphers)` |
| `tests/test_transport.py:148` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `self.assertEqual(("aes256-cbc", "aes192-cbc"), o.ciphers)` |
| `tests/test_transport.py:150` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `o.ciphers = ("aes256-cbc", "made-up-cipher")` |
| `tests/test_transport.py:185` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_transport.py:186` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = RSAKey(data=host_key.asbytes())` |
| `tests/test_transport.py:211` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_transport.py:212` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = RSAKey(data=host_key.asbytes())` |
| `tests/test_transport.py:233` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `options.ciphers = ("aes256-cbc",)` |
| `tests/test_transport.py:237` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `self.assertEqual("aes256-cbc", self.tc.local_cipher)` |
| `tests/test_transport.py:238` | AES | AES-256-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `self.assertEqual("aes256-cbc", self.tc.remote_cipher)` |
| `tests/test_transport.py:861` | RSA | RSA | test | élevée | `py-paramiko-cle` | `host_key = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_transport.py:862` | RSA | RSA | test | élevée | `py-paramiko-cle` | `public_host_key = RSAKey(data=host_key.asbytes())` |
| `tests/test_transport.py:1109` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"ciphers": ["aes128-cbc"],` |
| `tests/test_transport.py:1110` | MD5 | HMAC-MD5 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"macs": ["hmac-md5"],` |
| `tests/test_transport.py:1115` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert "aes128-cbc" in t._preferred_ciphers` |
| `tests/test_transport.py:1116` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert "aes128-cbc" not in t.preferred_ciphers` |
| `tests/test_transport.py:1117` | MD5 | HMAC-MD5 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert "hmac-md5" in t._preferred_macs` |
| `tests/test_transport.py:1118` | MD5 | HMAC-MD5 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert "hmac-md5" not in t.preferred_macs` |
| `tests/test_transport.py:1129` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"ciphers": ["aes128-cbc"],` |
| `tests/test_transport.py:1130` | MD5 | HMAC-MD5 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `"macs": ["hmac-md5"],` |
| `tests/test_transport.py:1158` | AES | AES-128-CBC ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert "aes128-cbc" not in ciphers` |
| `tests/test_transport.py:1159` | MD5 | HMAC-MD5 ; nom d'algorithme dans une chaîne | test | faible | `py-chaine-algorithme` | `assert "hmac-md5" not in macs` |
| `tests/test_transport.py:1228` | RSA | RSA | test | élevée | `py-paramiko-cle` | `hostkey = RSAKey.from_private_key_file(_support("rsa.key"))` |
| `tests/test_transport.py:1250` | RSA | RSA | test | élevée | `py-paramiko-cle` | `privkey = RSAKey.from_private_key_file(_support("rsa.key"))` |

## 3. Correspondance réglementaire

Les exigences ci-dessous proviennent exclusivement du référentiel fourni (regles.json, version 2026-11-22). Leur applicabilité au client dépend de son secteur, de sa juridiction et de ses contrats ; le relecteur doit la confirmer.

### 3.1 Familles observées et exigences

| Famille | Exigences du référentiel (échéance, effet) |
|---|---|
| RSA | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; CABF-VALIDITE-200J-2026 (2026-03-15, autre) ; CABF-VALIDITE-100J-2027 (2027-03-15, autre) ; CABF-VALIDITE-47J-2029 (2029-03-15, autre) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| ECDSA | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; CABF-VALIDITE-200J-2026 (2026-03-15, autre) ; CABF-VALIDITE-100J-2027 (2027-03-15, autre) ; CABF-VALIDITE-47J-2029 (2029-03-15, autre) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| ECDH | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| EDDSA | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| X25519_X448 | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| DSA | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) ; G7-CEG-CIBLE-2035 (2035-12-31, recommandé) ; EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) ; EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) ; EU-ROADMAP-2035 (2035-12-31, recommandé) ; EU-NIS2-PROPOSITION-PQC (non précisée, autre) ; FR-ANSSI-CALENDRIER (2030-12-31, recommandé) |
| AES | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) |
| 3DES | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) |
| MD5 | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) |
| SHA1 | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) ; CABF-SHA1-FIN-2026 (2026-09-15, interdit) |
| SHA2 | PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) |

### 3.2 Détail des exigences citées

#### PCI-DSS-12.3.3-INVENTAIRE-SUITES (PCI DSS v4.0.1 — Payment Card Industry Data Security Standard)

- Émetteur, juridiction, nature : PCI Security Standards Council, INT, contraignant
- Public visé : Entités qui stockent, traitent ou transmettent des données de titulaires de carte, et prestataires pouvant affecter leur sécurité. L'obligation est contractuelle (réseaux de cartes, acquéreurs), pas légale.
- Résumé : Les suites et protocoles cryptographiques utilisés sont documentés et revus au moins tous les 12 mois : inventaire à jour (usage et emplacement), veille sur leur viabilité, stratégie documentée face aux vulnérabilités attendues. Obligatoire depuis le 31 mars 2025. Aucune échéance de migration PQC. Libellé principal vérifié sur un document hébergé par le PCI SSC ; les alinéas « veille » et « stratégie » proviennent de sources secondaires concordantes (texte de la norme, sous licence, non consulté).
- Échéance : 2025-03-31
- Effet : inventaire obligatoire
- Confiance du référentiel : moyenne
- Familles observées concernées : RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA, AES, 3DES, MD5, SHA1, SHA2
- Source : <https://www.pcisecuritystandards.org/day-1_t2_7_pci-dss-v4-0_final/> (source datée du 2024-08-20)

#### PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (PCI DSS v4.0.1 — Payment Card Industry Data Security Standard)

- Émetteur, juridiction, nature : PCI Security Standards Council, INT, contraignant
- Public visé : Entités qui stockent, traitent ou transmettent des données de titulaires de carte, et prestataires pouvant affecter leur sécurité. L'obligation est contractuelle (réseaux de cartes, acquéreurs), pas légale.
- Résumé : Inventaire des clés et certificats de confiance utilisés pour protéger le PAN en transmission, exigence applicable depuis le 31 mars 2025. Non vérifié dans le texte de la norme : seule une source secondaire a été lue.
- Échéance : 2025-03-31
- Effet : inventaire obligatoire
- Confiance du référentiel : faible (à vérifier dans la source primaire)
- Familles observées concernées : RSA, ECDSA, EDDSA, DSA
- Source : <https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/> (source datée du 2024-08-20)

#### CABF-VALIDITE-200J-2026 (CA/Browser Forum — Baseline Requirements, scrutin SC-081v3 (durées de validité des certificats TLS))

- Émetteur, juridiction, nature : CA/Browser Forum, INT, contraignant indirectement (marchés publics, contrats)
- Public visé : Autorités de certification publiques (obligation directe). Tout détenteur de certificats TLS publics en subit l'effet. Ce ne sont pas des exigences PQC.
- Résumé : Durée de validité maximale de 200 jours pour les certificats TLS publics émis à partir du 15 mars 2026 (en vigueur) ; réutilisation des validations de domaine limitée à 200 jours. Vérifié dans les Baseline Requirements v2.3.1.
- Échéance : 2026-03-15
- Effet : autre
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA
- Source : <https://github.com/cabforum/servercert/blob/main/docs/BR.md> (source datée du 2025-04-11)

#### CABF-SHA1-FIN-2026 (CA/Browser Forum — Baseline Requirements, scrutin SC-081v3 (durées de validité des certificats TLS))

- Émetteur, juridiction, nature : CA/Browser Forum, INT, contraignant indirectement (marchés publics, contrats)
- Public visé : Autorités de certification publiques (obligation directe). Tout détenteur de certificats TLS publics en subit l'effet. Ce ne sont pas des exigences PQC.
- Résumé : Fin de tout usage résiduel de SHA-1 dans les certificats et les listes de révocation à partir du 15 septembre 2026 (Baseline Requirements v2.3.1).
- Échéance : 2026-09-15
- Effet : interdit
- Confiance du référentiel : élevée
- Familles observées concernées : SHA1
- Source : <https://github.com/cabforum/servercert/blob/main/docs/BR.md> (source datée du 2025-04-11)

#### EU-ROADMAP-2026-PLANS-NATIONAUX (A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography (NIS Cooperation Group, v1.1))

- Émetteur, juridiction, nature : NIS Cooperation Group (groupe de travail PQC), avec la Commission européenne, EU, recommandation
- Public visé : États membres de l'UE. Le texte ne crée aucune obligation directe pour les entreprises ; il découle d'une recommandation de la Commission et n'a pas, à notre lecture, d'effet juridique contraignant.
- Résumé : D'ici le 31 décembre 2026 : premières étapes mises en œuvre par tous les États membres, feuilles de route nationales initiales établies, planification et pilotes lancés pour les usages à risque élevé et moyen.
- Échéance : 2026-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA
- Source : <https://ec.europa.eu/newsroom/dae/redirection/document/117507> (source datée du 2025-06-23)

#### CABF-VALIDITE-100J-2027 (CA/Browser Forum — Baseline Requirements, scrutin SC-081v3 (durées de validité des certificats TLS))

- Émetteur, juridiction, nature : CA/Browser Forum, INT, contraignant indirectement (marchés publics, contrats)
- Public visé : Autorités de certification publiques (obligation directe). Tout détenteur de certificats TLS publics en subit l'effet. Ce ne sont pas des exigences PQC.
- Résumé : Durée de validité maximale de 100 jours pour les certificats émis à partir du 15 mars 2027 ; réutilisation des validations de domaine limitée à 100 jours.
- Échéance : 2027-03-15
- Effet : autre
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA
- Source : <https://github.com/cabforum/servercert/blob/main/docs/BR.md> (source datée du 2025-04-11)

#### CABF-VALIDITE-47J-2029 (CA/Browser Forum — Baseline Requirements, scrutin SC-081v3 (durées de validité des certificats TLS))

- Émetteur, juridiction, nature : CA/Browser Forum, INT, contraignant indirectement (marchés publics, contrats)
- Public visé : Autorités de certification publiques (obligation directe). Tout détenteur de certificats TLS publics en subit l'effet. Ce ne sont pas des exigences PQC.
- Résumé : Durée de validité maximale de 47 jours pour les certificats émis à partir du 15 mars 2029 ; réutilisation des validations de domaine limitée à 10 jours.
- Échéance : 2029-03-15
- Effet : autre
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA
- Source : <https://github.com/cabforum/servercert/blob/main/docs/BR.md> (source datée du 2025-04-11)

#### EU-ROADMAP-2030-HAUT-RISQUE (A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography (NIS Cooperation Group, v1.1))

- Émetteur, juridiction, nature : NIS Cooperation Group (groupe de travail PQC), avec la Commission européenne, EU, recommandation
- Public visé : États membres de l'UE. Le texte ne crée aucune obligation directe pour les entreprises ; il découle d'une recommandation de la Commission et n'a pas, à notre lecture, d'effet juridique contraignant.
- Résumé : D'ici le 31 décembre 2030 : transition achevée pour les usages à haut risque (notamment les données devant rester confidentielles au moins 10 ans), mises à jour résistantes au quantique activées par défaut. Après 2030, aucun mécanisme à clé publique vulnérable ne devrait être utilisé seul pour ces usages.
- Échéance : 2030-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA
- Source : <https://ec.europa.eu/newsroom/dae/redirection/document/117507> (source datée du 2025-06-23)

#### FR-ANSSI-CALENDRIER (ANSSI — positions sur la transition post-quantique)

- Émetteur, juridiction, nature : ANSSI, FR, recommandation
- Public visé : Administrations, opérateurs et fournisseurs de produits évalués par l'ANSSI (périmètre exact non vérifié).
- Résumé : Selon le même site : déploiement à partir de 2026, usages à haut risque d'ici 2030, transition complète d'ici 2035, en cohérence avec la feuille de route européenne que l'ANSSI diffuse. Non vérifié dans un texte de l'ANSSI.
- Échéance : 2030-12-31
- Effet : recommandé
- Confiance du référentiel : faible (à vérifier dans la source primaire)
- Familles observées concernées : RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA
- Source : <https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/> (source datée du 2026-04-05)

#### EU-ROADMAP-2035 (A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography (NIS Cooperation Group, v1.1))

- Émetteur, juridiction, nature : NIS Cooperation Group (groupe de travail PQC), avec la Commission européenne, EU, recommandation
- Public visé : États membres de l'UE. Le texte ne crée aucune obligation directe pour les entreprises ; il découle d'une recommandation de la Commission et n'a pas, à notre lecture, d'effet juridique contraignant.
- Résumé : D'ici le 31 décembre 2035 : transition achevée pour les usages à risque moyen et, autant que possible, pour les usages à faible risque ; les États visent « autant de systèmes que possible ».
- Échéance : 2035-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA
- Source : <https://ec.europa.eu/newsroom/dae/redirection/document/117507> (source datée du 2025-06-23)

#### G7-CEG-CIBLE-2035 (G7 Cyber Expert Group — Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector)

- Émetteur, juridiction, nature : G7 Cyber Expert Group, INT, recommandation
- Public visé : Établissements financiers et autorités financières des pays du G7. Le texte se déclare non prescriptif.
- Résumé : Feuille de route en six phases, explicitement non contraignante : la déclaration « ne fixe ni orientations ni attentes réglementaires ». Elle cite 2035 comme cible générale et 2030-2032 pour les systèmes les plus critiques. Document daté « janvier 2026 » (le 12 janvier selon les notes).
- Échéance : 2035-12-31
- Effet : recommandé
- Confiance du référentiel : élevée
- Familles observées concernées : RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA
- Source : <https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf> (source datée du 2026-01-12)

#### EU-NIS2-PROPOSITION-PQC (Proposition de modification de la directive NIS2 — COM(2026) 13, procédure 2026/0012(COD))

- Émetteur, juridiction, nature : Commission européenne, EU, projet
- Public visé : États membres (stratégies nationales de cybersécurité). Aucune obligation PQC pour les entreprises, même une fois adoptée.
- Résumé : La proposition obligerait les États membres à adopter, dans leur stratégie nationale de cybersécurité, des politiques de migration vers la PQC. Ce n'est qu'une proposition, encore en commission (ITRE) au Parlement, avec une première lecture indicative le 8 mars 2027, puis une transposition. Le numéro d'article (7(2)(k)) et l'alignement sur 2030/2035 viennent de sources secondaires. Date de la proposition : 14 janv. 2026 selon l'Observatoire législatif, 20 janv. 2026 selon d'autres sources.
- Échéance : non précisée
- Effet : autre
- Confiance du référentiel : moyenne
- Familles observées concernées : RSA, ECDSA, ECDH, EDDSA, X25519_X448, DSA
- Source : <https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1884097> (source datée du 2026-01-14)

## 4. Feuille de route de migration

Priorités déduites de l'inventaire. Les échéances citées sont celles du référentiel fourni ; les actions sont des recommandations de méthode, à adapter par le relecteur.

### Horizon 1 : maintenant à fin 2027

1. **Valider l'inventaire.** Relire les 64 constats à confiance faible ou moyenne, confirmer le contexte (production ou test) de chaque emplacement et compléter le questionnaire sur les HSM, KMS, VPN, la PKI et les dépendances fournisseurs, que l'analyse statique ne voit pas.
2. **Remplacer sans attendre les algorithmes déjà obsolètes en production** : 3DES ×3, MD5 ×4, SHA1 ×13.
3. **Sonder les points TLS exposés** depuis le réseau du client, puis activer l'échange hybride X25519MLKEM768 là où il manque.
4. **Documenter l'inventaire des suites et protocoles et le revoir au moins une fois par an** ; exigences d'inventaire du référentiel : PCI-DSS-12.3.3-INVENTAIRE-SUITES, PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS.
5. **Rendre la cryptographie agile** : regrouper le choix des algorithmes dans une configuration centrale plutôt que dans le code (9 fichier(s) en production fixent un algorithme à clé publique), et vérifier que les bibliothèques et modules certifiés utilisés prendront en charge ML-KEM et ML-DSA.

Échéances du référentiel dans cet horizon :
- CABF-SHA1-FIN-2026 (2026-09-15, interdit) : <https://github.com/cabforum/servercert/blob/main/docs/BR.md>
- CABF-VALIDITE-100J-2027 (2027-03-15, autre) : <https://github.com/cabforum/servercert/blob/main/docs/BR.md>
- CABF-VALIDITE-200J-2026 (2026-03-15, autre) : <https://github.com/cabforum/servercert/blob/main/docs/BR.md>
- EU-ROADMAP-2026-PLANS-NATIONAUX (2026-12-31, recommandé) : <https://ec.europa.eu/newsroom/dae/redirection/document/117507>
- PCI-DSS-12.3.3-INVENTAIRE-SUITES (2025-03-31, inventaire obligatoire) : <https://www.pcisecuritystandards.org/day-1_t2_7_pci-dss-v4-0_final/>
- PCI-DSS-4.2.1.1-INVENTAIRE-CLES-CERTIFICATS (2025-03-31, inventaire obligatoire) : <https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/>

### Horizon 2 : 2028 à 2030

1. **Remplacer d'abord l'échange de clés et le chiffrement à clé publique** (ECDH, X25519/X448, DH, RSA en chiffrement) par ML-KEM ou un mode hybride : 7 occurrence(s) dans 3 fichier(s) ou point(s) ; 76 occurrence(s) RSA dont l'usage (chiffrement ou signature) reste à préciser.
2. **Remplacer ensuite les signatures** (RSA, ECDSA, EdDSA, DSA) par ML-DSA ou SLH-DSA, en coordination avec la PKI, les autorités de certification et les HSM : 128 occurrence(s) dans 34 fichier(s) ou point(s).
3. Cet ordre suit la logique de dépréciation des algorithmes à clé publique décrite dans NIST IR 8547 : vérifier les dates exactes dans le référentiel (section 3).

Échéances du référentiel dans cet horizon :
- CABF-VALIDITE-47J-2029 (2029-03-15, autre) : <https://github.com/cabforum/servercert/blob/main/docs/BR.md>
- EU-ROADMAP-2030-HAUT-RISQUE (2030-12-31, recommandé) : <https://ec.europa.eu/newsroom/dae/redirection/document/117507>
- FR-ANSSI-CALENDRIER (2030-12-31, recommandé) : <https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/>

### Horizon 3 : 2031 à 2035

1. **Terminer la migration avant les dates d'interdiction** : traiter les résidus, y compris le code de test et d'exemple (176 occurrence(s) vulnérables hors production), les dépendances fournisseurs et les équipements à longue durée de vie.
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

constats.json : 227 fichier(s) analysé(s) ; ignorés : 24 binaire(s), 1 trop volumineux, 0 exclu(s).

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
