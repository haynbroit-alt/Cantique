# Outils de l'atelier PQC (v0)

`pqc-inventaire` produit, pour une base de code, trois livrables relisibles par une personne :

1. un **inventaire cryptographique** (`constats.json`) au format du contrat `../referentiel/SCHEMA.md` ;
2. un **CBOM CycloneDX 1.6** (`cbom.json`), validé contre le schéma officiel ;
3. un **rapport Markdown** de préparation post-quantique, en français ou en anglais, éventuellement en marque blanche.

L'analyse est déterministe : mêmes entrées, même sortie. Aucune IA, aucun accès réseau, aucune télémétrie.

## État de la v0

| Élément | État |
|---|---|
| `scan-code` (Python par AST ; Java/Kotlin, Go, JS/TS, C/C++, configurations TLS et SSH, PEM/DER, clés SSH par règles) | fonctionne, testé |
| `cbom` + `--validate` | fonctionne, le CBOM des fixtures valide contre CycloneDX 1.6 |
| `rapport` (fr/en, `--marque`) | fonctionne, testé avec un `regles.json` de test |
| `regles` (liste des 107 règles avec identifiant et description) | fonctionne |
| **Sonde TLS en Go (`sonde-tls`) et sous-commande `pqc-inventaire sonde-tls`** | **non réalisée** (arrêt du chantier décidé avant son démarrage) |
| Entrées TLS de `cbom` et `rapport` | code présent (protocoles, suites, certificats, synthèse TLS) mais **non testé** faute de sonde |

## Installation

Python 3.11 ou plus récent. Le cœur n'utilise que la bibliothèque standard.

```bash
cd atelier-pqc/outils
python3 -m venv .venv && . .venv/bin/activate
pip install .                                    # commande pqc-inventaire
pip install cryptography                         # facultatif : lecture des certificats
pip install 'cyclonedx-python-lib[json-validation]' pytest   # facultatif : validation du CBOM, tests
```

Sans installation : `python3 -m pqc_inventaire …` depuis `atelier-pqc/outils`.

Sans `cryptography`, un lecteur DER minimal (bibliothèque standard) lit quand même l'algorithme, la taille ou la courbe de la clé publique, la signature et les dates des certificats. Si les deux échouent, l'élément est rangé dans `a_verifier` (famille inconnue, confiance faible).

## Exemple de bout en bout

```bash
pqc-inventaire scan-code /chemin/du/client -o constats.json
pqc-inventaire cbom constats.json -o cbom.json --validate --nom "Application X"
pqc-inventaire rapport constats.json --regles ../referentiel/regles.json \
    --client "Client X" --langue fr -o rapport.md
# marque blanche, en anglais :
pqc-inventaire rapport constats.json --regles ../referentiel/regles.json \
    --client "Client X" --langue en --marque "Partenaire SAS" -o report.md
```

Options utiles :

- `scan-code` : `--inclure-vendor` (analyse aussi `node_modules`, `venv`, `.venv`, `__pycache__`, `dist`, `build`, `vendor`, `third_party`, `target`… ; `.git`, `.hg`, `.svn` restent exclus), `--exclure 'motif/*'`, `--taille-max` (2 Mio par défaut). Les liens symboliques ne sont pas suivis.
- `cbom` : `--date 2026-11-22T00:00:00Z` pour un fichier strictement reproductible (le numéro de série est déjà dérivé du contenu). Code de sortie 1 si le CBOM est invalide, 2 si le validateur n'est pas installé.
- `rapport` : `--date`, `--max-lignes` (taille du tableau par emplacement, 400 par défaut).

## Ce que fait chaque outil

### `scan-code`

Parcourt l'arborescence et applique une table de règles précises (appels d'API, directives de configuration), jamais un simple mot : « rsa » dans un identifiant, « RSA » dans un texte français ou un commentaire de documentation ne déclenchent rien.

- **Python** : analyse par l'arbre syntaxique (`ast`) — `cryptography`, PyCryptodome (`Crypto`/`Cryptodome`), `hashlib`, `hmac`, `ssl`, `paramiko`, PyJWT / python-jose / authlib, noms OpenSSL dans des chaînes. Les noms sont résolus à partir des imports, les docstrings et commentaires ignorés, la taille de clé lue même via une constante de module (`KEY_SIZE = 2048`). Repli par expressions régulières si le fichier n'est pas du Python 3 valide.
- **Java/Kotlin** : `KeyPairGenerator`, `Cipher`, `Signature`, `MessageDigest`, `KeyAgreement`, `Mac`, `KEM`… `getInstance("…")` (taille lue dans `initialize(2048)`, courbe dans `ECGenParameterSpec`), `SSLContext`, Bouncy Castle (classes et paquets PQC), jjwt / Nimbus / auth0.
- **Go** : `crypto/rsa`, `ecdsa`, `ed25519`, `ecdh`, `elliptic`, `mlkem`, `md5`, `sha1`, `des`, `rc4`, `aes`, `crypto/tls` (dont `tls.X25519MLKEM768`, versions, suites), golang-jwt.
- **JavaScript/TypeScript** : `node:crypto` (`generateKeyPair`, `createSign`, `createHash`, `createHmac`, `createCipheriv`, `createECDH`, Diffie-Hellman), WebCrypto (`name: 'RSA-OAEP'`…, `subtle.digest`), jsonwebtoken / jose, options `node:tls`.
- **C/C++ (OpenSSL)** : `EVP_PKEY_*`, `EVP_PKEY_Q_keygen`, `EVP_*_fetch`, `EVP_aes_256_gcm()`…, API historiques `RSA_*`, `EC_KEY_*`, `DH_*`, `DSA_*`, `MD5()`, `DES_*`, `SSL_CTX_set1_groups_list`, `set_cipher_list`, versions minimales.
- **Configurations** (`.conf`, `.cnf`, `.cfg`, `.ini`, `.yaml`, `.yml`, `.properties`, `.toml`) : protocoles (nginx, Apache `SSLProtocol` avec `all`/`-TLSv1`, HAProxy, OpenSSL, Spring, PostgreSQL), suites (avec repérage des suites faibles réellement activées : `!RC4` est une exclusion), groupes d'échange de clés (`X25519MLKEM768`…). Lignes commentées ignorées.
- **SSH** (`sshd_config`, `ssh_config`) : `KexAlgorithms` (dont `mlkem768x25519-sha256`, `sntrup761x25519-sha512`), algorithmes de clés d'hôte, `Ciphers`, `MACs`.
- **Matériel cryptographique** dans tout fichier texte : blocs PEM (clés privées PKCS#1/SEC1/PKCS#8/OpenSSH, clés publiques, CSR, certificats, paramètres DH/EC), certificats DER (`.der`, `.cer`, `.crt`), clés publiques OpenSSH. **Le contenu d'une clé privée n'est jamais recopié** : l'extrait se limite à l'en-tête suivi de « [contenu masqué] », et tout extrait est en outre purgé des longues séquences base64 ou hexadécimales.

Chaque constat porte : famille et classe du contrat, détail, fichier, ligne, extrait, langage, règle, `confiance` (`elevee` : appel explicite avec algorithme déterminé ; `moyenne` : import seul, constante générique, contexte TLS par défaut ; `faible` : chaîne isolée, ligne commentée) et `contexte` déduit du chemin (`test` : `tests/`, `test_*.py`, `*_test.go`, `*Test.java`, `*.spec.ts`… ; `exemple` : `examples/`, `demo/`… ; `documentation` : `docs/`, `.md`… ; sinon `production`).

**Extension du contrat** : chaque constat contient aussi un objet `parametres` (algorithme canonique, primitive, taille, courbe, mode, fonctions, notes, certificat). Les consommateurs qui ne le connaissent pas peuvent l'ignorer. Le fichier enveloppe les constats : `{"type": "code", "constats": [...], "a_verifier": [...], "statistiques": {...}}` ; `cbom` et `rapport` acceptent aussi une simple liste de constats.

**`a_verifier`** : matériel cryptographique dont la famille n'a pas pu être établie (certificat illisible, PKCS#8 chiffré, bloc PGP). Faute d'identifiant de famille, ces éléments ne sont pas des constats du contrat ; ils sont listés à part dans le rapport.

### `cbom`

Un composant `cryptographic-asset` par algorithme distinct (dédupliqué par nom canonique, par ex. `RSA-2048`), avec `primitive`, `parameterSetIdentifier`, `curve`, `mode`, `padding`, `cryptoFunctions`, `classicalSecurityLevel` (NIST SP 800-57) et `nistQuantumSecurityLevel` quand ils se déduisent (0 pour toute clé publique classique et pour MD5, SHA-1, DES, 3DES, RC4). Toutes les occurrences sont listées dans `evidence.occurrences` (fichier, ligne, règle, contexte, confiance). S'y ajoutent : un composant `protocol` par version TLS observée (suites dans `protocolProperties.cipherSuites`, nom du champ dans le schéma 1.6), un composant `certificate` par certificat relié à son algorithme de signature et à sa clé publique (`related-crypto-material`), et un composant `related-crypto-material` de type `private-key` par clé privée trouvée.

### `rapport`

Synthèse (comptes par classe, cinq principaux risques), inventaire par famille et par emplacement, correspondance réglementaire, feuille de route en trois horizons (maintenant–2027, 2028–2030, 2031–2035), limites de l'analyse, liste de contrôle du relecteur, annexe de méthode. **Aucun texte réglementaire n'est rédigé par l'outil** : exigences, échéances, effets, niveaux de confiance et `source_url` viennent tous de `regles.json` ; une famille sans exigence est signalée comme telle ; les identifiants de famille inconnus de `regles.json` sont ignorés avec un avertissement. Avec `--marque`, le nom du partenaire figure dans l'en-tête et le pied de page, et ni « Atelier PQC » ni le nom de l'outil n'apparaissent.

## Sondes TLS : avertissement sur les proxys

La sonde TLS n'est pas livrée dans cette v0. Quand elle le sera, elle devra être lancée **depuis le poste ou le réseau du client ou du partenaire**. Dans l'environnement où ces outils ont été écrits, tout le trafic TLS sortant est re-terminé par un proxy d'interception : sonder Internet depuis là mesurerait le proxy et non la cible. Toute mesure TLS faite derrière un proxy ou un équipement d'inspection TLS est fausse.

## Limites

- Analyse statique uniquement : un algorithme choisi à l'exécution, chargé dynamiquement ou venant d'une dépendance binaire échappe à l'analyse ; les règles sont ligne à ligne ou sur un appel, sans suivi de flux (une taille de clé passée par une variable locale n'est pas lue).
- Faux positifs (code mort, chaînes isolées en confiance faible) et faux négatifs (API ou syntaxe non couvertes : Rust, C#, PHP, Ruby, magasins de clés JKS/PKCS#12, BLAKE2, SSH par `paramiko` hors classes de clés…).
- Une clé EC générée sans indication d'usage est classée `ECDSA` avec la note « ECDSA ou ECDH selon l'usage » : à trancher à la relecture.
- Aucune visibilité sur l'exécution, les HSM, les KMS, la PKI interne, les VPN ni les micrologiciels.
- Ce n'est ni une certification, ni un audit de conformité, ni un avis juridique ; le relecteur humain reste responsable. L'outil ne recommande jamais de cryptographie maison : la migration s'appuie sur des bibliothèques et modules reconnus et, si exigé, certifiés.

## Vérifier la sortie (relecteur)

1. `pqc-inventaire regles` : relire l'identifiant et la description de chaque règle citée.
2. Ouvrir au moins dix constats à confiance élevée au fichier et à la ligne indiqués ; trier tous les constats moyens et faibles.
3. Vérifier le `contexte` des chemins ambigus et l'absence de secret dans les extraits ; signaler au client toute clé privée trouvée.
4. Vérifier la version et la date de `regles.json`, ouvrir chaque `source_url` citée, confirmer l'applicabilité au client.
5. Relancer `cbom --validate` sur le fichier livré.
6. Cocher la liste de contrôle en fin de rapport, puis dater et signer.

## Tests

```bash
cd atelier-pqc/outils
python -m pytest -q        # 39 tests ; la validation de schéma est sautée si cyclonedx-python-lib est absent
```

Les fixtures (`tests/fixtures/code`) couvrent Python, Java, Go, JavaScript, C, nginx et un certificat public de test ; les clés privées sont générées pendant les tests et jamais stockées dans le dépôt. `tests/fixtures/regles_fixture.json` est un référentiel fictif : les tests ne dépendent pas du vrai `regles.json`.
