# Contrat de données de l'atelier PQC

Ce fichier fixe les identifiants et les formats partagés entre le scanner, le générateur de rapport et le référentiel réglementaire. Toute modification doit être reportée dans les trois.

## Familles cryptographiques

Chaque constat du scanner porte exactement un identifiant de famille parmi la liste ci-dessous.

| Identifiant | Famille | Classe quantique |
|---|---|---|
| `RSA` | RSA (chiffrement, signature, échange de clés) | `vulnerable_shor` |
| `ECDSA` | Signatures ECDSA (P-256, P-384, secp256k1…) | `vulnerable_shor` |
| `ECDH` | Échange de clés ECDH sur courbes NIST ou Brainpool | `vulnerable_shor` |
| `EDDSA` | Ed25519, Ed448 | `vulnerable_shor` |
| `X25519_X448` | Échange de clés X25519, X448 | `vulnerable_shor` |
| `DH` | Diffie-Hellman à corps fini | `vulnerable_shor` |
| `DSA` | DSA | `vulnerable_shor` |
| `ML-KEM` | ML-KEM (FIPS 203), Kyber | `pqc` |
| `ML-DSA` | ML-DSA (FIPS 204), Dilithium | `pqc` |
| `SLH-DSA` | SLH-DSA (FIPS 205), SPHINCS+ | `pqc` |
| `FN-DSA` | FN-DSA (FIPS 206 en projet), Falcon | `pqc` |
| `HYBRID_KEM` | Échange hybride classique + PQC (X25519MLKEM768…) | `hybride` |
| `AES` | AES (préciser la taille de clé dans le constat) | `symetrique` |
| `CHACHA20` | ChaCha20, ChaCha20-Poly1305 | `symetrique` |
| `3DES` | Triple DES | `obsolete_classique` |
| `DES` | DES | `obsolete_classique` |
| `RC4` | RC4 | `obsolete_classique` |
| `MD5` | MD5 | `obsolete_classique` |
| `SHA1` | SHA-1 | `obsolete_classique` |
| `SHA2` | SHA-224, SHA-256, SHA-384, SHA-512 | `hachage_ok` |
| `SHA3` | SHA-3, SHAKE | `hachage_ok` |
| `TLS_LEGACY` | Protocoles SSL 3.0, TLS 1.0, TLS 1.1 | `obsolete_classique` |
| `TLS_SUITE` | Toute suite TLS observée (sert à l'inventaire PCI DSS 12.3.3) | `inventaire` |

## Référentiel réglementaire lisible par machine

Fichier : `atelier-pqc/referentiel/regles.json`. Le générateur de rapport le lit pour rattacher chaque famille aux exigences applicables.

```json
{
  "version": "AAAA-MM-JJ",
  "avertissement_fr": "…",
  "disclaimer_en": "…",
  "referentiels": [
    {
      "id": "NIST-IR-8547",
      "nom": "NIST IR 8547 — Transition to Post-Quantum Cryptography Standards",
      "juridiction": "US",
      "emetteur": "NIST",
      "nature": "contraignant | contraignant_indirect | recommandation | projet",
      "public_vise_fr": "…",
      "target_audience_en": "…",
      "source_url": "https://…",
      "date_source": "AAAA-MM-JJ",
      "exigences": [
        {
          "id": "NIST-IR-8547-DEPRECATION-2030",
          "resume_fr": "…",
          "summary_en": "…",
          "echeance": "AAAA-MM-JJ ou null",
          "familles": ["RSA", "ECDSA", "ECDH", "EDDSA", "X25519_X448", "DH", "DSA"],
          "effet": "deprecie | interdit | inventaire_obligatoire | migration_requise | recommande | autre",
          "source_url": "https://…",
          "confiance": "elevee | moyenne | faible"
        }
      ]
    }
  ]
}
```

Règles :
- `familles` ne contient que des identifiants de la table ci-dessus.
- Une exigence qui vise tout l'inventaire (comme PCI DSS 12.3.3) liste `TLS_SUITE` et toutes les familles concernées.
- Toute date ou exigence non vérifiée dans une source primaire porte `"confiance": "faible"` et le dit dans `resume_fr`.

## Constat du scanner (format interne JSON)

```json
{
  "famille": "RSA",
  "classe": "vulnerable_shor",
  "detail": "RSA-2048, génération de clé",
  "fichier": "chemin/relatif.py",
  "ligne": 42,
  "extrait": "rsa.generate_private_key(public_exponent=65537, key_size=2048)",
  "langage": "python",
  "regle": "py-cryptography-rsa-generate",
  "confiance": "elevee | moyenne | faible",
  "contexte": "production | test | exemple | documentation",
  "parametres": {"algorithme": "RSA-2048", "primitive": "pke", "taille_cle": 2048, "courbe": null, "mode": null,
                 "fonctions": ["keygen"], "certificat": null, "notes": []}
}
```

`parametres` est facultatif ; `cbom` et `rapport` s'en servent quand il est présent.

Le fichier de constats enveloppe la liste : `{"type": "code" | "tls", "constats": […], "a_verifier": […], "statistiques": {…}}`. Une liste nue de constats est aussi acceptée. `a_verifier` recueille le matériel cryptographique dont la famille n'a pas pu être établie (certificat illisible, clé PKCS#8 chiffrée, bloc PGP) : ces éléments restent hors de `constats` et figurent dans le rapport pour relecture humaine.
