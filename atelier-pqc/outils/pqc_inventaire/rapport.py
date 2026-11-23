"""Rapport Markdown de préparation post-quantique (français ou anglais).

Règle absolue : aucun contenu réglementaire n'est rédigé ici. Toute exigence,
échéance ou source citée provient du fichier regles.json fourni ; si une
famille n'y est rattachée à aucune exigence, le rapport le dit.
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from datetime import date as _date

from . import __version__
from .familles import (CLASSES_LIBELLES, ECHANGE_CLES, FAMILLES, FAMILLES_LIBELLES, ORDRE_CLASSES, SIGNATURES,
                       composer_detail)

MARQUE_ATELIER = "Atelier PQC"

_EFFETS = {"deprecie": ("déprécié", "deprecated"), "interdit": ("interdit", "disallowed"),
           "inventaire_obligatoire": ("inventaire obligatoire", "mandatory inventory"),
           "migration_requise": ("migration requise", "migration required"),
           "recommande": ("recommandé", "recommended"), "autre": ("autre", "other")}
_NATURES = {"contraignant": ("contraignant", "binding"),
            "contraignant_indirect": ("contraignant indirectement (marchés publics, contrats)",
                                      "indirectly binding (procurement, contracts)"),
            "recommandation": ("recommandation", "recommendation"), "projet": ("projet", "draft")}
_CONFIANCES = {"elevee": ("élevée", "high"), "moyenne": ("moyenne", "medium"), "faible": ("faible", "low")}
_CONTEXTES = {"production": ("production", "production"), "test": ("test", "test"),
              "exemple": ("exemple", "example"), "documentation": ("documentation", "documentation")}
_POIDS_CLASSE = {"obsolete_classique": 3.0, "vulnerable_shor": 2.0}
_POIDS_CONTEXTE = {"production": 1.0, "test": 0.2, "exemple": 0.2, "documentation": 0.1}
_POIDS_CONFIANCE = {"elevee": 1.0, "moyenne": 0.6, "faible": 0.3}
_OBSOLETES_ALGOS = {"MD5", "SHA1", "DES", "3DES", "RC4"}

# Textes fixes. Chaque entrée : (français, anglais).
T = {
    "titre": ("Préparation post-quantique : inventaire cryptographique", "Post-quantum readiness: cryptographic inventory"),
    "client": ("Client", "Client"), "prepare_par": ("Préparé par", "Prepared by"), "date": ("Date", "Date"),
    "sources": ("Sources analysées", "Analysed sources"),
    "referentiel": ("Référentiel réglementaire", "Regulatory reference set"),
    "statut": ("Statut", "Status"),
    "statut_val": ("Projet à relire, compléter et signer par le relecteur", "Draft to be reviewed, completed and signed by the reviewer"),
    "avert_fixe": (
        "Ce document est un produit d'information issu d'une analyse automatisée, relu par une personne. "
        "Il ne constitue ni un avis juridique, ni une certification, ni un audit de conformité.",
        "This document is an information product derived from automated analysis and reviewed by a person. "
        "It is neither legal advice, nor a certification, nor a compliance audit."),
    "s_synthese": ("1. Synthèse", "1. Executive summary"),
    "synthese_intro": (
        "L'analyse a relevé **{n} constats** répartis en **{f} familles cryptographiques**, dont **{p}** dans du code "
        "ou des configurations classés « production ». {v} constats portent sur de la cryptographie à clé publique "
        "classique, vulnérable à un futur ordinateur quantique (algorithme de Shor) ; {o} portent sur des algorithmes "
        "ou protocoles déjà obsolètes aujourd'hui.",
        "The analysis found **{n} findings** across **{f} cryptographic families**, of which **{p}** are in code or "
        "configuration classified as \"production\". {v} findings concern classical public-key cryptography, which a "
        "future quantum computer could break (Shor's algorithm); {o} concern algorithms or protocols that are already "
        "obsolete today."),
    "aucun_constat": ("Aucun constat cryptographique n'a été relevé dans les sources fournies. Cela ne prouve pas "
                      "l'absence de cryptographie (voir les limites de l'analyse).",
                      "No cryptographic finding was made in the supplied sources. This does not prove that no "
                      "cryptography is used (see the limits of the analysis)."),
    "s_classes": ("Répartition par classe", "Breakdown by class"),
    "col_classe": ("Classe", "Class"), "col_constats": ("Constats", "Findings"),
    "col_prod": ("dont production", "of which production"), "col_familles": ("Familles", "Families"),
    "s_risques": ("Principaux risques", "Top risks"),
    "risques_intro": ("Classement par gravité de la classe, contexte (la production compte davantage que les tests) "
                      "et confiance du constat.",
                      "Ranked by class severity, context (production weighs more than tests) and finding confidence."),
    "aucun_risque": ("Aucun algorithme vulnérable ou obsolète n'a été relevé.", "No vulnerable or obsolete algorithm was found."),
    "occ": ("{n} occurrence(s), dont {p} en production", "{n} occurrence(s), {p} in production"),
    "r_obsolete": ("algorithme déjà faible ou cassé avec des moyens classiques : à remplacer sans attendre l'ordinateur quantique.",
                   "already weak or broken with classical means: replace it without waiting for quantum computers."),
    "r_tls_legacy": ("protocole obsolète encore configuré ou accepté : à désactiver.",
                     "obsolete protocol still configured or accepted: disable it."),
    "r_kex": ("échange de clés cassable par un ordinateur quantique ; les échanges chiffrés aujourd'hui peuvent être "
              "enregistrés puis déchiffrés plus tard (« collecter maintenant, déchiffrer plus tard »).",
              "key exchange breakable by a quantum computer; traffic encrypted today can be recorded and decrypted later "
              "(\"harvest now, decrypt later\")."),
    "r_rsa": ("cryptographie à clé publique cassable par l'algorithme de Shor (chiffrement, échange de clés, signature).",
              "public-key cryptography breakable by Shor's algorithm (encryption, key exchange, signatures)."),
    "r_sig": ("signatures falsifiables une fois un ordinateur quantique disponible ; migration à coordonner avec la PKI.",
              "signatures forgeable once a quantum computer exists; migration must be coordinated with the PKI."),
    "r_exigences": ("Exigences les plus pressantes : {ids}.", "Most pressing requirements: {ids}."),
    "r_autres": ("et {n} autre(s), voir la section 3", "and {n} more, see section 3"),
    "s_tls": ("Points TLS sondés", "Probed TLS endpoints"),
    "tls_resume": ("{n} point(s) sondé(s) ; échange hybride X25519MLKEM768 accepté sur {h} ; TLS 1.0 ou 1.1 accepté "
                   "sur {l} ; erreurs sur {e}.",
                   "{n} endpoint(s) probed; hybrid X25519MLKEM768 key exchange accepted on {h}; TLS 1.0 or 1.1 accepted "
                   "on {l}; errors on {e}."),
    "tls_aucun": ("Aucun point TLS n'a été sondé. La sonde doit être lancée depuis le réseau du client ou du partenaire.",
                  "No TLS endpoint was probed. The probe must be run from the client's or partner's network."),
    "s_inventaire": ("2. Inventaire", "2. Inventory"),
    "s_par_famille": ("2.1 Par famille", "2.1 By family"),
    "col_famille": ("Famille", "Family"), "col_occ": ("Occurrences", "Occurrences"), "col_production": ("Production", "Production"),
    "col_autres": ("Test / exemple / doc.", "Test / example / docs"),
    "col_confiance": ("Confiance (é / m / f)", "Confidence (h / m / l)"),
    "col_algos": ("Algorithmes observés", "Observed algorithms"),
    "s_par_emplacement": ("2.2 Par emplacement", "2.2 By location"),
    "col_emplacement": ("Emplacement", "Location"), "col_detail": ("Détail", "Detail"),
    "col_contexte": ("Contexte", "Context"), "col_conf": ("Confiance", "Confidence"), "col_regle": ("Règle", "Rule"),
    "col_extrait": ("Extrait", "Excerpt"),
    "tronque": ("Tableau limité aux {m} premiers constats sur {n} ; la liste complète figure dans le fichier de constats JSON.",
                "Table limited to the first {m} of {n} findings; the full list is in the JSON findings file."),
    "s_a_verifier": ("2.3 Éléments à vérifier manuellement", "2.3 Items to check manually"),
    "a_verifier_intro": ("Matériel cryptographique repéré dont la famille n'a pas pu être établie (certificat illisible, "
                         "clé privée chiffrée, bloc PGP…). Ces éléments ne sont pas comptés dans la synthèse.",
                         "Cryptographic material whose family could not be established (unreadable certificate, encrypted "
                         "private key, PGP block…). These items are not counted in the summary."),
    "s_regl": ("3. Correspondance réglementaire", "3. Regulatory mapping"),
    "regl_intro": ("Les exigences ci-dessous proviennent exclusivement du référentiel fourni ({src}, version {v}). Leur "
                   "applicabilité au client dépend de son secteur, de sa juridiction et de ses contrats ; le relecteur "
                   "doit la confirmer.",
                   "The requirements below come exclusively from the supplied reference set ({src}, version {v}). Whether "
                   "they apply to the client depends on its sector, jurisdiction and contracts; the reviewer must confirm it."),
    "regl_avert": ("Avertissement du référentiel", "Reference-set disclaimer"),
    "s_familles_exig": ("3.1 Familles observées et exigences", "3.1 Observed families and requirements"),
    "col_exigences": ("Exigences du référentiel (échéance, effet)", "Reference-set requirements (deadline, effect)"),
    "aucune_exig": ("Aucune exigence du référentiel ne vise cette famille.", "No requirement in the reference set targets this family."),
    "s_detail_exig": ("3.2 Détail des exigences citées", "3.2 Details of the cited requirements"),
    "aucune_exig_globale": ("Aucune exigence du référentiel ne vise les familles observées.",
                            "No requirement in the reference set targets the observed families."),
    "e_emetteur": ("Émetteur, juridiction, nature", "Issuer, jurisdiction, nature"),
    "e_public": ("Public visé", "Target audience"), "e_resume": ("Résumé", "Summary"),
    "e_echeance": ("Échéance", "Deadline"), "e_effet": ("Effet", "Effect"),
    "e_confiance": ("Confiance du référentiel", "Reference-set confidence"),
    "e_faible": ("à vérifier dans la source primaire", "to be checked against the primary source"),
    "e_familles": ("Familles observées concernées", "Observed families concerned"),
    "e_source": ("Source", "Source"), "e_consultee": ("source datée du {d}", "source dated {d}"),
    "non_precisee": ("non précisée", "not specified"),
    "s_feuille": ("4. Feuille de route de migration", "4. Migration roadmap"),
    "feuille_intro": ("Priorités déduites de l'inventaire. Les échéances citées sont celles du référentiel fourni ; "
                      "les actions sont des recommandations de méthode, à adapter par le relecteur.",
                      "Priorities derived from the inventory. Deadlines quoted are those of the supplied reference set; "
                      "actions are methodological recommendations for the reviewer to adapt."),
    "h1": ("Horizon 1 : maintenant à fin 2027", "Horizon 1: now to end of 2027"),
    "h2": ("Horizon 2 : 2028 à 2030", "Horizon 2: 2028 to 2030"),
    "h3": ("Horizon 3 : 2031 à 2035", "Horizon 3: 2031 to 2035"),
    "h_echeances": ("Échéances du référentiel dans cet horizon", "Reference-set deadlines in this horizon"),
    "h_aucune": ("aucune échéance du référentiel ne tombe dans cet horizon pour les familles observées.",
                 "no reference-set deadline falls in this horizon for the observed families."),
    "a_valider": ("**Valider l'inventaire.** Relire les {f} constats à confiance faible ou moyenne, confirmer le "
                  "contexte (production ou test) de chaque emplacement et compléter le questionnaire sur les HSM, KMS, "
                  "VPN, la PKI et les dépendances fournisseurs, que l'analyse statique ne voit pas.",
                  "**Validate the inventory.** Review the {f} low- or medium-confidence findings, confirm the context "
                  "(production or test) of each location, and complete the questionnaire on HSMs, KMSs, VPNs, the PKI "
                  "and supplier dependencies, which static analysis cannot see."),
    "a_obsoletes": ("**Remplacer sans attendre les algorithmes déjà obsolètes en production** : {liste}.",
                    "**Replace already-obsolete algorithms in production without waiting**: {liste}."),
    "a_obsoletes_aucun": ("Aucun algorithme déjà obsolète n'a été relevé en production.",
                          "No already-obsolete algorithm was found in production."),
    "a_tls_legacy": ("**Désactiver TLS 1.0 / 1.1 et SSL** là où ils sont configurés ou acceptés : {liste}.",
                     "**Disable TLS 1.0 / 1.1 and SSL** where they are configured or accepted: {liste}."),
    "a_hybride": ("**Activer l'échange de clés hybride X25519MLKEM768 (TLS 1.3)** sur les points qui ne l'acceptent pas : {liste}.",
                  "**Enable the X25519MLKEM768 hybrid key exchange (TLS 1.3)** on endpoints that do not accept it: {liste}."),
    "a_hybride_ok": ("Tous les points TLS sondés acceptent déjà l'échange hybride X25519MLKEM768 : le maintenir et l'étendre "
                     "aux points non sondés.",
                     "All probed TLS endpoints already accept the X25519MLKEM768 hybrid key exchange: keep it and extend it "
                     "to endpoints that were not probed."),
    "a_hybride_sonde": ("**Sonder les points TLS exposés** depuis le réseau du client, puis activer l'échange hybride "
                        "X25519MLKEM768 là où il manque.",
                        "**Probe the exposed TLS endpoints** from the client's network, then enable the X25519MLKEM768 "
                        "hybrid key exchange where it is missing."),
    "a_inventaire": ("**Documenter l'inventaire des suites et protocoles et le revoir au moins une fois par an** ; "
                     "exigences d'inventaire du référentiel : {ids}.",
                     "**Document the inventory of cipher suites and protocols and review it at least yearly**; inventory "
                     "requirements in the reference set: {ids}."),
    "a_inventaire_aucun": ("**Documenter l'inventaire des suites et protocoles** ; le référentiel fourni ne contient pas "
                           "d'exigence d'inventaire obligatoire pour les familles observées.",
                           "**Document the inventory of cipher suites and protocols**; the supplied reference set contains "
                           "no mandatory-inventory requirement for the observed families."),
    "a_agilite": ("**Rendre la cryptographie agile** : regrouper le choix des algorithmes dans une configuration centrale "
                  "plutôt que dans le code ({n} fichier(s) en production fixent un algorithme à clé publique), et vérifier "
                  "que les bibliothèques et modules certifiés utilisés prendront en charge ML-KEM et ML-DSA.",
                  "**Make cryptography agile**: move algorithm choices into a central configuration rather than code "
                  "({n} production file(s) hard-code a public-key algorithm), and check that the certified libraries and "
                  "modules in use will support ML-KEM and ML-DSA."),
    "a_kex": ("**Remplacer d'abord l'échange de clés et le chiffrement à clé publique** (ECDH, X25519/X448, DH, RSA en "
              "chiffrement) par ML-KEM ou un mode hybride : {n} occurrence(s) dans {f} fichier(s) ou point(s){ex}.",
              "**Replace key exchange and public-key encryption first** (ECDH, X25519/X448, DH, RSA encryption) with "
              "ML-KEM or a hybrid mode: {n} occurrence(s) in {f} file(s) or endpoint(s){ex}."),
    "a_sig": ("**Remplacer ensuite les signatures** (RSA, ECDSA, EdDSA, DSA) par ML-DSA ou SLH-DSA, en coordination avec "
              "la PKI, les autorités de certification et les HSM : {n} occurrence(s) dans {f} fichier(s) ou point(s){ex}.",
              "**Then replace signatures** (RSA, ECDSA, EdDSA, DSA) with ML-DSA or SLH-DSA, in coordination with the "
              "PKI, certificate authorities and HSMs: {n} occurrence(s) in {f} file(s) or endpoint(s){ex}."),
    "a_rsa_indet": (" ; {n} occurrence(s) RSA dont l'usage (chiffrement ou signature) reste à préciser",
                    "; {n} RSA occurrence(s) whose use (encryption or signature) is still to be determined"),
    "a_ordre": ("Cet ordre suit la logique de dépréciation des algorithmes à clé publique décrite dans NIST IR 8547 : "
                "vérifier les dates exactes dans le référentiel (section 3).",
                "This order follows the public-key deprecation logic described in NIST IR 8547: check the exact dates "
                "in the reference set (section 3)."),
    "a_finir": ("**Terminer la migration avant les dates d'interdiction** : traiter les résidus, y compris le code de test "
                "et d'exemple ({n} occurrence(s) vulnérables hors production), les dépendances fournisseurs et les "
                "équipements à longue durée de vie.",
                "**Complete the migration before disallowance dates**: handle the remainder, including test and example "
                "code ({n} vulnerable occurrence(s) outside production), supplier dependencies and long-lived equipment."),
    "a_reevaluer": ("Réévaluer les modes hybrides et les tailles de clés symétriques au regard des exigences alors en "
                    "vigueur ; refaire l'inventaire pour confirmer qu'il ne reste aucun algorithme vulnérable.",
                    "Reassess hybrid modes and symmetric key sizes against the requirements then in force; repeat the "
                    "inventory to confirm that no vulnerable algorithm remains."),
    "s_limites": ("5. Limites de l'analyse", "5. Limits of the analysis"),
    "limites": ((
        "**Analyse statique uniquement.** Le code et les fichiers de configuration sont lus sans être exécutés ; un "
        "algorithme choisi à l'exécution, chargé dynamiquement ou fourni par une dépendance binaire peut échapper à l'analyse.",
        "**Faux positifs et faux négatifs.** Les règles visent des appels d'API et des directives précises, mais un "
        "constat peut concerner du code mort, et une forme d'écriture non prévue peut passer inaperçue. La confiance "
        "indiquée pour chaque constat (élevée, moyenne, faible) guide la relecture ; elle ne remplace pas la vérification.",
        "**Aucune visibilité sur l'exécution, les HSM, les KMS, la PKI interne, les VPN ni les micrologiciels.** Ces "
        "éléments relèvent du questionnaire et de l'accès privilégié du partenaire.",
        "**Sondes TLS.** Elles mesurent ce que voit le poste d'où elles sont lancées. Un proxy ou un équipement "
        "d'inspection TLS sur le chemin fausse la mesure : il faut les lancer depuis un réseau sans interception.",
        "**Ni certification, ni audit de conformité, ni avis juridique.** Ce rapport aide à préparer une démarche de "
        "conformité ; il ne l'atteste pas.",
        "**Le relecteur humain reste responsable** du tri des constats, de l'applicabilité des exigences au client et "
        "des recommandations finales.",
        "**Aucune cryptographie maison.** Ce rapport ne recommande jamais d'implémenter soi-même un algorithme : la "
        "migration doit s'appuyer sur des bibliothèques et modules cryptographiques reconnus et, lorsque c'est exigé, "
        "certifiés.",
        "**Référentiel daté.** Les exigences citées sont celles du fichier regles.json fourni (version {v}) ; les textes "
        "évoluent et doivent être revérifiés à la source avant toute décision.",
    ), (
        "**Static analysis only.** Code and configuration files are read without being executed; an algorithm chosen at "
        "run time, loaded dynamically or supplied by a binary dependency may be missed.",
        "**False positives and false negatives.** Rules target specific API calls and directives, but a finding may "
        "concern dead code, and an unforeseen coding pattern may go unnoticed. Each finding's confidence (high, medium, "
        "low) guides the review; it does not replace verification.",
        "**No visibility of run time, HSMs, KMSs, the internal PKI, VPNs or firmware.** These are covered by the "
        "questionnaire and the partner's privileged access.",
        "**TLS probes.** They measure what the machine they run on can see. A proxy or TLS inspection device on the path "
        "distorts the measurement: run them from a network without interception.",
        "**Not a certification, compliance audit or legal advice.** This report helps prepare a compliance effort; it "
        "does not attest to it.",
        "**The human reviewer remains responsible** for triaging findings, deciding which requirements apply to the "
        "client, and the final recommendations.",
        "**No home-made cryptography.** This report never recommends implementing an algorithm yourself: migration must "
        "rely on recognised and, where required, certified cryptographic libraries and modules.",
        "**Dated reference set.** The requirements quoted are those of the supplied regles.json (version {v}); texts "
        "change and must be re-checked at the source before any decision.",
    )),
    "s_controle": ("6. Liste de contrôle du relecteur", "6. Reviewer checklist"),
    "controle": ((
        "Vérifier un échantillon d'au moins dix constats à confiance élevée en ouvrant le fichier à la ligne indiquée.",
        "Trier chaque constat à confiance faible ou moyenne : confirmer, requalifier ou écarter, et le noter.",
        "Confirmer le contexte (production, test, exemple, documentation) des emplacements ambigus.",
        "Vérifier qu'aucun extrait du rapport ne contient de secret ; les clés privées trouvées doivent être signalées au client.",
        "Pour chaque point TLS, vérifier que la sonde a été lancée depuis un réseau sans proxy d'interception.",
        "Vérifier la version et la date du référentiel, puis ouvrir chaque source citée pour confirmer l'exigence et l'échéance.",
        "Confirmer avec le client quelles exigences lui sont réellement applicables (secteur, juridiction, contrats).",
        "Compléter le questionnaire HSM, KMS, VPN, PKI et dépendances fournisseurs.",
        "Adapter la feuille de route au contexte du client, puis dater et signer le rapport.",
    ), (
        "Check a sample of at least ten high-confidence findings by opening the file at the stated line.",
        "Triage every low- or medium-confidence finding: confirm, requalify or dismiss, and record the decision.",
        "Confirm the context (production, test, example, documentation) of ambiguous locations.",
        "Check that no excerpt in the report contains a secret; private keys found must be reported to the client.",
        "For each TLS endpoint, check that the probe ran from a network without an intercepting proxy.",
        "Check the reference set's version and date, then open each cited source to confirm the requirement and deadline.",
        "Confirm with the client which requirements actually apply (sector, jurisdiction, contracts).",
        "Complete the HSM, KMS, VPN, PKI and supplier-dependency questionnaire.",
        "Adapt the roadmap to the client's situation, then date and sign the report.",
    )),
    "s_annexe": ("Annexe : méthode", "Appendix: method"),
    "annexe_outil": ("Constats produits par pqc-inventaire {v} ({r} règles).", "Findings produced by pqc-inventaire {v} ({r} rules)."),
    "annexe_outil_marque": ("Constats produits par un outillage d'analyse statique ({r} règles).",
                            "Findings produced by static-analysis tooling ({r} rules)."),
    "annexe_tls": ("Constats TLS importés depuis : {s}.", "TLS findings imported from: {s}."),
    "annexe_fichiers": ("{a} fichier(s) analysé(s) ; ignorés : {b} binaire(s), {t} trop volumineux, {x} exclu(s).",
                        "{a} file(s) analysed; skipped: {b} binary, {t} too large, {x} excluded."),
    "annexe_classes": ("Classes utilisées", "Classes used"),
    "pied": ("Document produit par l'{m} avec pqc-inventaire {v}.", "Document produced by {m} with pqc-inventaire {v}."),
    "pied_marque": ("Document préparé par {m}.", "Document prepared by {m}."),
    "src_code": ("{s} (code, {n} fichier(s))", "{s} (code, {n} file(s))"),
    "src_tls": ("{s} (TLS, {n} point(s))", "{s} (TLS, {n} endpoint(s))"),
    "src_autre": ("{s}", "{s}"),
    "regles_absent": ("aucun", "none"),
    "et_autres": (" et {n} autre(s)", " and {n} more"),
}

_DEFINITIONS_CLASSES = {
    "vulnerable_shor": ("cryptographie à clé publique classique, cassable par un ordinateur quantique (algorithme de Shor)",
                        "classical public-key cryptography, breakable by a quantum computer (Shor's algorithm)"),
    "obsolete_classique": ("algorithme ou protocole déjà faible avec des moyens classiques",
                           "algorithm or protocol already weak with classical means"),
    "hybride": ("échange de clés combinant un algorithme classique et un algorithme post-quantique",
                "key exchange combining a classical and a post-quantum algorithm"),
    "pqc": ("algorithme post-quantique normalisé par le NIST (FIPS 203, 204, 205 ; FIPS 206 en projet)",
            "NIST-standardised post-quantum algorithm (FIPS 203, 204, 205; FIPS 206 in draft)"),
    "symetrique": ("chiffrement symétrique ; l'impact quantique dépend de la taille de clé",
                   "symmetric encryption; quantum impact depends on key size"),
    "hachage_ok": ("fonction de hachage robuste", "robust hash function"),
    "inventaire": ("suite ou protocole TLS relevé pour l'inventaire", "TLS suite or protocol recorded for the inventory"),
}


def _md(texte) -> str:
    return str(texte).replace("|", "\\|").replace("\n", " ").strip()


def _code(texte: str) -> str:
    t = _md(texte).replace("`", "'")
    return f"`{t}`" if t else ""


class _Rapport:
    def __init__(self, documents, constats, a_verifier, regles, regles_chemin, client, langue, marque, date, max_lignes):
        self.docs, self.constats, self.a_verifier = documents, constats, a_verifier
        self.regles, self.regles_chemin = regles or {}, regles_chemin
        self.client, self.i, self.marque = client, 0 if langue == "fr" else 1, marque
        self.date, self.max_lignes = date, max_lignes
        self.lignes: list[str] = []
        self.exigences = self._exigences()

    # -- utilitaires ---------------------------------------------------------------
    def t(self, cle: str, **kw) -> str:
        return T[cle][self.i].format(**kw) if kw else T[cle][self.i]

    def lib(self, table: dict, cle: str | None) -> str:
        return table.get(cle, (cle or "?", cle or "?"))[self.i]

    def w(self, *lignes: str) -> None:
        self.lignes.extend(lignes)

    def detail(self, c: dict) -> str:
        if self.i == 0 or not c.get("parametres"):
            return c.get("detail") or ""
        return composer_detail(c["parametres"], "en")

    def _exigences(self) -> list[dict]:
        res = []
        for ref in self.regles.get("referentiels") or []:
            for e in ref.get("exigences") or []:
                inconnues = [f for f in e.get("familles") or [] if f not in FAMILLES]
                if inconnues:
                    print(f"avertissement : regles.json, exigence {e.get('id')} : familles inconnues ignorées {inconnues}",
                          file=sys.stderr)
                res.append({**e, "_ref": ref, "familles": [f for f in e.get("familles") or [] if f in FAMILLES]})
        return res

    def exigences_de(self, famille: str) -> list[dict]:
        return [e for e in self.exigences if famille in e["familles"]]

    _RANG_NATURE = {"contraignant": 0, "contraignant_indirect": 1, "projet": 2, "recommandation": 3}

    def priorite_exig(self, e: dict) -> tuple:
        """Contraignant d'abord, puis échéance la plus proche ; les exigences sans date passent après."""
        nature = (e.get("_ref") or {}).get("nature")
        return (self._RANG_NATURE.get(nature, 4), e.get("echeance") or "9999-12-31", e.get("id") or "")

    def resume_exig(self, e: dict) -> str:
        return e.get("resume_fr" if self.i == 0 else "summary_en") or e.get("resume_fr") or e.get("summary_en") or ""

    @property
    def familles_observees(self) -> list[str]:
        presentes = {c["famille"] for c in self.constats}
        return [f for f in FAMILLES if f in presentes]

    def score(self, c: dict) -> float:
        poids = _POIDS_CLASSE.get(c["classe"], 0.0)
        if c["famille"] in ECHANGE_CLES:
            poids += 0.5
        return poids * _POIDS_CONTEXTE.get(c.get("contexte"), 0.5) * _POIDS_CONFIANCE.get(c.get("confiance"), 0.5)

    def usage(self, c: dict) -> str:
        """echange | signature | indetermine | autre"""
        f = c["famille"]
        p = c.get("parametres") or {}
        if f in ECHANGE_CLES:
            return "echange"
        if f in SIGNATURES:
            return "signature"
        if f == "RSA":
            fonctions = set(p.get("fonctions") or [])
            if p.get("primitive") == "signature" or fonctions & {"sign", "verify"}:
                return "signature"
            if p.get("primitive") == "pke" and fonctions & {"encrypt", "decrypt"}:
                return "echange"
            return "indetermine"
        return "autre"

    def liste_courte(self, elements: list[str], n: int = 8) -> str:
        elements = sorted(set(elements))
        texte = ", ".join(_md(e) for e in elements[:n])
        if len(elements) > n:
            texte += self.t("et_autres", n=len(elements) - n)
        return texte

    def cibles_tls(self) -> list[dict]:
        return [c for d in self.docs if d.get("type") == "tls" for c in d.get("cibles") or []]

    # -- sections ------------------------------------------------------------------------
    def entete(self) -> None:
        sources = []
        for d in self.docs:
            if d.get("type") == "code":
                n = (d.get("statistiques") or {}).get("fichiers_analyses", "?")
                sources.append(self.t("src_code", s=d["_source"], n=n))
            elif d.get("type") == "tls":
                sources.append(self.t("src_tls", s=d["_source"], n=len(d.get("cibles") or [])))
            else:
                sources.append(self.t("src_autre", s=d["_source"]))
        nb_ref = len(self.regles.get("referentiels") or [])
        ref = f"{_md(self.regles_chemin)}, version {_md(self.regles.get('version', '?'))} ({nb_ref} texte(s))" if self.i == 0 \
            else f"{_md(self.regles_chemin)}, version {_md(self.regles.get('version', '?'))} ({nb_ref} text(s))"
        self.w(f"# {self.t('titre')}", "", f"## {_md(self.client)}", "",
               "| | |", "|---|---|",
               f"| {self.t('client')} | {_md(self.client)} |",
               f"| {self.t('prepare_par')} | {_md(self.marque or MARQUE_ATELIER)} |",
               f"| {self.t('date')} | {self.date} |",
               f"| {self.t('sources')} | {'; '.join(sources) or self.t('regles_absent')} |",
               f"| {self.t('referentiel')} | {ref} |",
               f"| {self.t('statut')} | {self.t('statut_val')} |", "")
        avert = self.regles.get("avertissement_fr" if self.i == 0 else "disclaimer_en")
        self.w(f"> {self.t('avert_fixe')}")
        if avert:
            self.w(">", f"> **{self.t('regl_avert')}** : {_md(avert)}" if self.i == 0 else f"> **{self.t('regl_avert')}**: {_md(avert)}")
        self.w("")

    def synthese(self) -> None:
        c = self.constats
        self.w(f"## {self.t('s_synthese')}", "")
        if not c:
            self.w(self.t("aucun_constat"), "")
        else:
            prod = sum(1 for x in c if x.get("contexte") == "production")
            vuln = sum(1 for x in c if x["classe"] == "vulnerable_shor")
            obs = sum(1 for x in c if x["classe"] == "obsolete_classique")
            self.w(self.t("synthese_intro", n=len(c), f=len(self.familles_observees), p=prod, v=vuln, o=obs), "")
            self.w(f"### {self.t('s_classes')}", "",
                   f"| {self.t('col_classe')} | {self.t('col_constats')} | {self.t('col_prod')} | {self.t('col_familles')} |",
                   "|---|---:|---:|---|")
            for classe in ORDRE_CLASSES:
                xs = [x for x in c if x["classe"] == classe]
                if xs:
                    fams = [f for f in FAMILLES if any(x["famille"] == f for x in xs)]
                    self.w(f"| {self.lib(CLASSES_LIBELLES, classe)} | {len(xs)} | "
                           f"{sum(1 for x in xs if x.get('contexte') == 'production')} | {', '.join(fams)} |")
            self.w("")
        self.risques()
        self.w(f"### {self.t('s_tls')}", "")
        cibles = self.cibles_tls()
        if not cibles:
            self.w(self.t("tls_aucun"), "")
        else:
            h = sum(1 for x in cibles if x.get("hybride_pq") is True)
            legacy = sum(1 for x in cibles if x.get("tls10") is True or x.get("tls11") is True)
            err = sum(1 for x in cibles if x.get("erreurs"))
            self.w(self.t("tls_resume", n=len(cibles), h=h, l=legacy, e=err), "")

    def risques(self) -> None:
        self.w(f"### {self.t('s_risques')}", "", self.t("risques_intro"), "")
        scores: dict[str, float] = defaultdict(float)
        for x in self.constats:
            scores[x["famille"]] += self.score(x)
        classement = sorted((f for f in scores if scores[f] > 0), key=lambda f: (-scores[f], list(FAMILLES).index(f)))[:5]
        if not classement:
            self.w(self.t("aucun_risque"), "")
            return
        for rang, f in enumerate(classement, 1):
            xs = [x for x in self.constats if x["famille"] == f]
            prod = sum(1 for x in xs if x.get("contexte") == "production")
            if f == "TLS_LEGACY":
                raison = self.t("r_tls_legacy")
            elif FAMILLES[f] == "obsolete_classique":
                raison = self.t("r_obsolete")
            elif f in ECHANGE_CLES:
                raison = self.t("r_kex")
            elif f == "RSA":
                raison = self.t("r_rsa")
            else:
                raison = self.t("r_sig")
            exigences = sorted(self.exigences_de(f), key=self.priorite_exig)
            ids = [f"{e['id']} ({e.get('echeance') or '—'})" for e in exigences[:3]]
            if len(exigences) > 3:
                ids.append(self.t("r_autres", n=len(exigences) - 3))
            suite = " " + self.t("r_exigences", ids=", ".join(ids)) if ids else ""
            self.w(f"{rang}. **{f}** ({self.lib(FAMILLES_LIBELLES, f)}) : {self.t('occ', n=len(xs), p=prod)} ; {raison}{suite}"
                   if self.i == 0 else
                   f"{rang}. **{f}** ({self.lib(FAMILLES_LIBELLES, f)}): {self.t('occ', n=len(xs), p=prod)}; {raison}{suite}")
        self.w("")

    def inventaire(self) -> None:
        self.w(f"## {self.t('s_inventaire')}", "", f"### {self.t('s_par_famille')}", "")
        if self.constats:
            self.w(f"| {self.t('col_famille')} | {self.t('col_classe')} | {self.t('col_occ')} | {self.t('col_production')} | "
                   f"{self.t('col_autres')} | {self.t('col_confiance')} | {self.t('col_algos')} |",
                   "|---|---|---:|---:|---:|---|---|")
            for f in self.familles_observees:
                xs = [x for x in self.constats if x["famille"] == f]
                conf = Counter(x.get("confiance") for x in xs)
                prod = sum(1 for x in xs if x.get("contexte") == "production")
                algos = [(x.get("parametres") or {}).get("algorithme") or f for x in xs]
                self.w(f"| {f} | {self.lib(CLASSES_LIBELLES, FAMILLES[f])} | {len(xs)} | {prod} | {len(xs) - prod} | "
                       f"{conf['elevee']} / {conf['moyenne']} / {conf['faible']} | {self.liste_courte(algos, 6)} |")
        else:
            self.w(self.t("aucun_constat"))
        self.w("", f"### {self.t('s_par_emplacement')}", "")
        if self.constats:
            self.w(f"| {self.t('col_emplacement')} | {self.t('col_famille')} | {self.t('col_detail')} | "
                   f"{self.t('col_contexte')} | {self.t('col_conf')} | {self.t('col_regle')} | {self.t('col_extrait')} |",
                   "|---|---|---|---|---|---|---|")
            tries = sorted(self.constats, key=lambda x: (x["fichier"], x.get("ligne") or 0, x["famille"]))
            for x in tries[: self.max_lignes]:
                lieu = f"{x['fichier']}:{x['ligne']}" if x.get("ligne") else x["fichier"]
                self.w(f"| {_code(lieu)} | {x['famille']} | {_md(self.detail(x))} | {self.lib(_CONTEXTES, x.get('contexte'))} | "
                       f"{self.lib(_CONFIANCES, x.get('confiance'))} | {_code(x.get('regle', ''))} | {_code(x.get('extrait', ''))} |")
            if len(tries) > self.max_lignes:
                self.w("", self.t("tronque", m=self.max_lignes, n=len(tries)))
        self.w("")
        if self.a_verifier:
            self.w(f"### {self.t('s_a_verifier')}", "", self.t("a_verifier_intro"), "",
                   f"| {self.t('col_emplacement')} | {self.t('col_detail')} | {self.t('col_regle')} | {self.t('col_extrait')} |",
                   "|---|---|---|---|")
            for x in sorted(self.a_verifier, key=lambda x: (x.get("fichier", ""), x.get("ligne") or 0)):
                self.w(f"| {_code(str(x.get('fichier')) + ':' + str(x.get('ligne')))} | {_md(self.detail(x))} | "
                       f"{_code(x.get('regle', ''))} | {_code(x.get('extrait', ''))} |")
            self.w("")

    def reglementaire(self) -> None:
        self.w(f"## {self.t('s_regl')}", "",
               self.t("regl_intro", src=_md(self.regles_chemin), v=_md(self.regles.get("version", "?"))), "",
               f"### {self.t('s_familles_exig')}", "",
               f"| {self.t('col_famille')} | {self.t('col_exigences')} |", "|---|---|")
        citees: dict[str, dict] = {}
        for f in self.familles_observees:
            exs = self.exigences_de(f)
            if exs:
                morceaux = []
                for e in exs:
                    citees[e["id"]] = e
                    morceaux.append(f"{_md(e['id'])} ({e.get('echeance') or self.t('non_precisee')}, "
                                    f"{self.lib(_EFFETS, e.get('effet'))})")
                self.w(f"| {f} | {' ; '.join(morceaux) if self.i == 0 else '; '.join(morceaux)} |")
            else:
                self.w(f"| {f} | {self.t('aucune_exig')} |")
        self.w("", f"### {self.t('s_detail_exig')}", "")
        if not citees:
            self.w(self.t("aucune_exig_globale"), "")
        sep = " : " if self.i == 0 else ": "
        observees = set(self.familles_observees)
        for e in sorted(citees.values(), key=lambda e: ((e.get("echeance") or "9999"), e["id"])):
            ref = e["_ref"]
            nature = self.lib(_NATURES, ref.get("nature"))
            public = ref.get("public_vise_fr" if self.i == 0 else "target_audience_en") or ""
            conf = self.lib(_CONFIANCES, e.get("confiance"))
            if e.get("confiance") == "faible":
                conf += f" ({self.t('e_faible')})"
            date_src = ref.get("date_source")
            source = e.get("source_url") or ref.get("source_url") or "?"
            self.w(f"#### {_md(e['id'])} ({_md(ref.get('nom') or ref.get('id') or '')})", "",
                   f"- {self.t('e_emetteur')}{sep}{_md(ref.get('emetteur', '?'))}, {_md(ref.get('juridiction', '?'))}, {nature}")
            if public:
                self.w(f"- {self.t('e_public')}{sep}{_md(public)}")
            self.w(f"- {self.t('e_resume')}{sep}{_md(self.resume_exig(e))}",
                   f"- {self.t('e_echeance')}{sep}{e.get('echeance') or self.t('non_precisee')}",
                   f"- {self.t('e_effet')}{sep}{self.lib(_EFFETS, e.get('effet'))}",
                   f"- {self.t('e_confiance')}{sep}{conf}",
                   f"- {self.t('e_familles')}{sep}{', '.join(f for f in e['familles'] if f in observees)}",
                   f"- {self.t('e_source')}{sep}<{source}>" + (f" ({self.t('e_consultee', d=date_src)})" if date_src else ""),
                   "")

    def _echeances(self, debut: int, fin: int) -> list[str]:
        observees = set(self.familles_observees)
        res = []
        for e in self.exigences:
            ech = e.get("echeance")
            if not ech or not observees & set(e["familles"]):
                continue
            try:
                annee = int(str(ech)[:4])
            except ValueError:
                continue
            if debut <= annee <= fin:
                res.append(f"{_md(e['id'])} ({ech}, {self.lib(_EFFETS, e.get('effet'))}) : <{e.get('source_url') or e['_ref'].get('source_url')}>"
                           if self.i == 0 else
                           f"{_md(e['id'])} ({ech}, {self.lib(_EFFETS, e.get('effet'))}): <{e.get('source_url') or e['_ref'].get('source_url')}>")
        return sorted(res)

    def _horizon(self, titre: str, actions: list[str], debut: int, fin: int) -> None:
        self.w(f"### {self.t(titre)}", "")
        for n, a in enumerate(actions, 1):
            self.w(f"{n}. {a}")
        echeances = self._echeances(debut, fin)
        self.w("", f"{self.t('h_echeances')}{' :' if self.i == 0 else ':'}" + ("" if echeances else f" {self.t('h_aucune')}"))
        for e in echeances:
            self.w(f"- {e}")
        self.w("")

    def feuille_de_route(self) -> None:
        c = self.constats
        prod = [x for x in c if x.get("contexte") == "production"]
        self.w(f"## {self.t('s_feuille')}", "", self.t("feuille_intro"), "")
        # Horizon 1
        douteux = sum(1 for x in c if x.get("confiance") in ("faible", "moyenne")) + len(self.a_verifier)
        actions = [self.t("a_valider", f=douteux)]
        obs = Counter(x["famille"] for x in prod if x["famille"] in _OBSOLETES_ALGOS)
        actions.append(self.t("a_obsoletes", liste=", ".join(f"{f} ×{n}" for f, n in sorted(obs.items())))
                       if obs else self.t("a_obsoletes_aucun"))
        legacy = [f"{x['fichier']}" + (f":{x['ligne']}" if x.get("ligne") else "") for x in c if x["famille"] == "TLS_LEGACY"]
        if legacy:
            actions.append(self.t("a_tls_legacy", liste=self.liste_courte(legacy)))
        cibles = self.cibles_tls()
        if not cibles:
            actions.append(self.t("a_hybride_sonde"))
        else:
            sans = [x.get("cible", "?") for x in cibles if x.get("hybride_pq") is not True]
            actions.append(self.t("a_hybride", liste=self.liste_courte(sans)) if sans else self.t("a_hybride_ok"))
        inv = sorted({e["id"] for e in self.exigences if e.get("effet") == "inventaire_obligatoire"
                      and set(e["familles"]) & set(self.familles_observees)})
        actions.append(self.t("a_inventaire", ids=", ".join(inv)) if inv else self.t("a_inventaire_aucun"))
        fichiers_pk = {x["fichier"] for x in prod if x["classe"] == "vulnerable_shor" and x.get("langage") not in ("tls",)}
        actions.append(self.t("a_agilite", n=len(fichiers_pk)))
        self._horizon("h1", actions, 0, 2027)
        # Horizon 2
        kex = [x for x in c if self.usage(x) == "echange"]
        sig = [x for x in c if self.usage(x) == "signature"]
        indet = [x for x in c if self.usage(x) == "indetermine"]
        ex_kex = self.t("a_rsa_indet", n=len(indet)) if indet else ""
        actions = [self.t("a_kex", n=len(kex), f=len({x["fichier"] for x in kex}), ex=ex_kex),
                   self.t("a_sig", n=len(sig), f=len({x["fichier"] for x in sig}), ex=""),
                   self.t("a_ordre")]
        self._horizon("h2", actions, 2028, 2030)
        # Horizon 3
        hors_prod = sum(1 for x in c if x["classe"] == "vulnerable_shor" and x.get("contexte") != "production")
        self._horizon("h3", [self.t("a_finir", n=hors_prod), self.t("a_reevaluer")], 2031, 2035)

    def limites(self) -> None:
        self.w(f"## {self.t('s_limites')}", "")
        for li in T["limites"][self.i]:
            self.w(f"- {li.format(v=_md(self.regles.get('version', '?')))}")
        self.w("", f"## {self.t('s_controle')}", "")
        for li in T["controle"][self.i]:
            self.w(f"- [ ] {li}")
        self.w("")

    def annexe(self) -> None:
        self.w(f"## {self.t('s_annexe')}", "")
        nb_regles = max([(d.get("statistiques") or {}).get("regles", 0) for d in self.docs] or [0])
        self.w(self.t("annexe_outil_marque", r=nb_regles) if self.marque else self.t("annexe_outil", v=__version__, r=nb_regles))
        tls = [d["_source"] for d in self.docs if d.get("type") == "tls"]
        if tls:
            self.w("", self.t("annexe_tls", s=", ".join(tls)))
        for d in self.docs:
            s = d.get("statistiques")
            if d.get("type") == "code" and s:
                self.w("", f"{_md(d['_source'])}{' :' if self.i == 0 else ':'} " + self.t("annexe_fichiers", a=s.get("fichiers_analyses", 0),
                                                                b=s.get("binaire", 0), t=s.get("taille", 0), x=s.get("exclu", 0)))
        self.w("", f"**{self.t('annexe_classes')}**", "")
        for classe in ORDRE_CLASSES:
            self.w(f"- {self.lib(CLASSES_LIBELLES, classe)} (`{classe}`) : {self.lib(_DEFINITIONS_CLASSES, classe)}" if self.i == 0
                   else f"- {self.lib(CLASSES_LIBELLES, classe)} (`{classe}`): {self.lib(_DEFINITIONS_CLASSES, classe)}")
        self.w("", "---", "", self.t("pied_marque", m=_md(self.marque)) if self.marque
               else self.t("pied", m=MARQUE_ATELIER, v=__version__), "")

    def produire(self) -> str:
        self.entete()
        self.synthese()
        self.inventaire()
        self.reglementaire()
        self.feuille_de_route()
        self.limites()
        self.annexe()
        return "\n".join(self.lignes)


def generer_rapport(documents: list[dict], constats: list[dict], a_verifier: list[dict], regles: dict,
                    client: str, langue: str = "fr", marque: str | None = None, date: str | None = None,
                    regles_chemin: str = "regles.json", max_lignes: int = 400) -> str:
    if langue not in ("fr", "en"):
        raise ValueError("langue : fr ou en")
    return _Rapport(documents, constats, a_verifier, regles, regles_chemin, client, langue, marque,
                    date or _date.today().isoformat(), max_lignes).produire()
