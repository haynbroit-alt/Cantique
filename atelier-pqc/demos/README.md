# Dossiers de démonstration

Deux dossiers produits le 22 novembre 2026 par la chaîne `outils/pqc_inventaire` sur des bibliothèques libres téléchargées depuis PyPI :

| Bibliothèque | Version | Constats | Fichiers produits |
|---|---|---:|---|
| paramiko (SSH) | 3.5.1 | 277 | `constats.json`, `cbom.json` (CycloneDX 1.6 validé), `rapport.md` |
| PyJWT (jetons JWT) | 2.10.1 | 238 | `constats.json`, `cbom.json` (CycloneDX 1.6 validé), `rapport.md` |

Commandes utilisées (depuis `atelier-pqc/outils`) :

```
python -m pqc_inventaire scan-code <sources> -o ../demos/<lib>/constats.json
python -m pqc_inventaire cbom ../demos/<lib>/constats.json -o ../demos/<lib>/cbom.json --validate --date 2026-11-22
python -m pqc_inventaire rapport ../demos/<lib>/constats.json --regles ../referentiel/regles.json \
  --client "<lib> (démonstration, bibliothèque libre)" --langue fr --date 2026-11-22 --juridictions INT,EU,FR \
  -o ../demos/<lib>/rapport.md
```

Ces dossiers montrent le format des livrables ; ce ne sont pas des audits de ces projets. Ils n'ont pas été relus ligne à ligne : la majorité des constats se trouvent dans les tests des bibliothèques, ce qui est attendu pour du code cryptographique.
