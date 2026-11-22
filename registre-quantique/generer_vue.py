#!/usr/bin/env python3
"""Construit registre.md, vue lisible de affirmations.jsonl (bibliothèque standard uniquement).

La vue regroupe les affirmations par acteur, dans l'ordre chronologique, avec un
tableau par acteur, et rassemble dans une section « Q-Day » les estimations de
ressources, les enquêtes d'experts et les marchés prédictifs. Elle est entièrement
dérivée du JSONL : on ne la modifie jamais à la main.

Usage : python3 generer_vue.py [affirmations.jsonl] [-o registre.md]
Lancer valider.py avant : ce script suppose un fichier valide.
"""

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ICI = Path(__file__).resolve().parent

TYPES = {
    "feuille_de_route": "feuille de route",
    "demonstration": "démonstration",
    "estimation_ressources": "estimation de ressources",
    "programme_public": "programme public",
    "prix": "prix",
    "revendication_avantage": "revendication d'avantage",
    "refutation": "réfutation ou contestation",
    "financement": "financement",
    "enquete_experts": "enquête ou avis d'experts",
    "marche_predictif": "marché prédictif",
    "resultat_financier": "résultat financier",
}
STATUTS = {
    "promis": ("promis", "Engagement ou cible future, non échue, ou sans information de livraison postérieure."),
    "demontre": ("annoncé ou publié", "L'acteur a publié ou annoncé le résultat, le chiffre ou la cible ; aucune vérification indépendante n'est revendiquée."),
    "verifie_tiers": ("vérifié par un tiers", "Un tiers indépendant (revue à comité de lecture, DARPA, reproduction, attribution d'un prix) le confirme ; la source du statut est indiquée."),
    "contredit": ("contredit", "Une source tierce ou un dépôt ultérieur rapporte un résultat contraire ou le réfute ; la source du statut est indiquée."),
    "en_retard": ("en retard", "L'échéance est passée sans livraison constatée par une source ; la source du statut est indiquée."),
    "retire": ("retiré ou remplacé", "L'acteur lui-même a retiré ou remplacé l'affirmation ; la source du statut est indiquée."),
    "inconnu": ("inconnu, à vérifier", "Fait non vérifié, contradictoire ou connu par un simple résumé, ou échéance passée sans information."),
}
METRIQUES = {
    "qubits_physiques": "qubits physiques",
    "qubits_logiques": "qubits logiques",
    "taux_erreur_logique": "taux d'erreur logique",
    "erreur_porte_2q": "erreur de porte à 2 qubits",
    "erreur_porte_logique_2q": "erreur de porte logique à 2 qubits",
    "fidelite_2q": "fidélité à 2 qubits",
    "portes_toffoli": "portes Toffoli",
    "portes_t_logiques": "portes T logiques",
    "operations_logiques": "opérations logiques",
    "duree_execution": "durée d'exécution",
    "probabilite_succes": "probabilité de succès",
    "latence_decodage": "latence de décodage",
    "cycles_qec": "cycles de correction",
    "facteur_reduction_surcout": "réduction du surcoût",
    "taille_cle_cassee": "taille de clé cassée",
    "aleatoire_certifie": "aléa certifié",
    "bits_entropie_certifies": "bits d'entropie certifiés",
    "complexite_algorithme": "complexité de l'algorithme",
    "avantage_quantique": "avantage quantique",
    "jalon": "jalon",
    "mise_en_service": "mise en service",
    "nombre_jalons": "nombre de jalons",
    "nombre_soumissions": "nombre de soumissions",
    "nombre_entreprises": "nombre d'entreprises",
    "appreciation_qualitative": "appréciation qualitative",
    "probabilite_crqc": "probabilité d'un CRQC",
    "horizon_crqc": "horizon d'un CRQC",
    "horizon_tolerance_fautes": "horizon de la tolérance aux fautes",
    "horizon_commercialisation": "horizon de commercialisation",
    "probabilite_marche": "probabilité de marché",
    "volume_marche": "volume du marché",
    "part_repondants": "part des répondants",
    "prix_minute": "prix à la minute",
    "prix_tache": "prix par tâche",
    "prix_tir": "prix par tir",
    "prix_heure": "prix à l'heure",
    "prix_porte_tir": "prix par porte-tir",
    "prix_programme_min": "prix minimal par programme",
    "engagement_minimum": "engagement minimal",
    "minutes_gratuites": "minutes gratuites",
    "credits_gratuits": "crédits gratuits",
    "chiffre_affaires": "chiffre d'affaires",
    "ebitda_ajuste": "EBITDA ajusté",
    "montant_financement": "montant du financement",
    "valorisation": "valorisation",
    "ratio_realise_projete": "ratio réalisé / projeté",
    "echeance_migration_pqc": "échéance de migration post-quantique",
    "statut_proposition": "statut de la proposition",
    "delai_apres_activation": "délai après activation",
}
COMPARATEURS = {"=": "", "<": "< ", "<=": "≤ ", ">": "> ", ">=": "≥ ", "~": "≈ "}


def libelle_metrique(code):
    return METRIQUES.get(code, code.replace("_", " "))
TYPES_QDAY = {"estimation_ressources", "enquete_experts", "marche_predictif"}
EXPOSANTS = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def cle_tri_nom(nom):
    sans_accents = unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode()
    return sans_accents.casefold()


def ancre(nom):
    return "acteur-" + re.sub(r"[^a-z0-9]+", "-", cle_tri_nom(nom)).strip("-")


def cle_tri_date(texte):
    morceaux = [int(x) for x in texte.split("-")]
    return tuple(morceaux + [0] * (3 - len(morceaux)))


def cellule(texte):
    return str(texte).replace("\n", " ").replace("|", "\\|")


def titre_lien(texte):
    return cellule(texte).replace("[", "(").replace("]", ")")


def grouper(chiffres):
    return f"{chiffres:,}".replace(",", " ")


def nombre(v, unite):
    if isinstance(v, float) and not v.is_integer():
        monetaire = bool(unite) and unite.startswith(("USD", "EUR", "AUD"))
        if 0 < abs(v) < 0.01 and not monetaire:
            mantisse, exposant = f"{v:.2e}".split("e")
            mantisse = mantisse.rstrip("0").rstrip(".").replace(".", ",")
            return f"{mantisse}×10{str(int(exposant)).translate(EXPOSANTS)}"
        if monetaire and abs(v) < 1:
            return f"{v:.6f}".rstrip("0").rstrip(".").replace(".", ",")
        return f"{v:g}".replace(".", ",")
    n = int(v)
    if abs(n) >= 1_000_000_000:
        return f"{n / 1e9:.4g}".replace(".", ",") + " Md"
    if abs(n) >= 1_000_000:
        return f"{n / 1e6:.4g}".replace(".", ",") + " M"
    return grouper(n)


def valeur_simple(v, unite, comparateur):
    texte = v if isinstance(v, str) else nombre(v, unite)
    prefixe = COMPARATEURS.get(comparateur or "=", "")
    return f"{prefixe}{texte}" + (f" {unite}" if unite else "")


def valeur(e):
    parties = [valeur_simple(e["valeur"], e["unite"], e.get("comparateur"))]
    for m in e.get("mesures_complementaires", []):
        texte = valeur_simple(m["valeur"], m["unite"], m.get("comparateur"))
        precisions = []
        if m["metrique"] != e["metrique"] or not m.get("libelle"):
            precisions.append(libelle_metrique(m["metrique"]))
        if m.get("libelle"):
            precisions.append(m["libelle"])
        parties.append(f"{texte} ({', '.join(precisions)})")
    return "<br>".join(cellule(p) for p in parties)


def date_affichee(e):
    prefixe = "≤ " if e.get("precision_date") == "au_plus_tard" else ""
    return prefixe + e["date_affirmation"]


def statut_affiche(e):
    libelle = STATUTS[e["statut"]][0]
    if e["statut"] in ("contredit", "verifie_tiers", "retire", "en_retard"):
        libelle = f"**{libelle}**"
    if e.get("statut_source_url"):
        libelle += f" ([source du statut]({e['statut_source_url']}))"
    return libelle


def source_affichee(e):
    return f"[{titre_lien(e['source_titre'])}]({e['source_url']}) ({e['source_type']})"


def enonce_affiche(e, via=None, limite=200):
    texte = e["enonce"]
    if len(texte) > limite:
        texte = texte[: limite - 1].rstrip() + "…"
    if via:
        texte = f"(via {via}) {texte}"
    return f"{cellule(texte)}<br><sub>`{e['id']}`</sub>"


def tableau(lignes, entetes):
    sortie = ["| " + " | ".join(entetes) + " |", "|" + "---|" * len(entetes)]
    sortie += ["| " + " | ".join(l) + " |" for l in lignes]
    return sortie


def charger(chemin):
    entrees = []
    for n, ligne in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), 1):
        if not ligne.strip():
            continue
        try:
            entrees.append(json.loads(ligne))
        except json.JSONDecodeError as exc:
            sys.exit(f"ligne {n} : JSON invalide ({exc.msg}) ; lancer valider.py")
    return entrees


def construire(entrees):
    par_id = {e["id"]: e for e in entrees}
    tri = lambda e: (cle_tri_date(e["date_affirmation"]), e["id"])
    derniere_saisie = max(e["date_saisie"] for e in entrees)
    derniere_consultation = max(e["date_consultation"] for e in entrees)
    nb_inconnu = sum(e["statut"] == "inconnu" for e in entrees)
    nb_apt = sum(e.get("precision_date") == "au_plus_tard" for e in entrees)

    md = [
        "# Registre horodaté des affirmations quantiques (v0)",
        "",
        f"> Vue générée par `generer_vue.py` à partir de `affirmations.jsonl` : {len(entrees)} affirmations, "
        f"dernière saisie le {derniere_saisie}, dernière consultation de source le {derniere_consultation}. "
        "Ne pas modifier ce fichier à la main : corriger le JSONL, lancer `valider.py`, puis régénérer.",
        "",
        "Ce registre consigne les affirmations datées sur la route de l'informatique quantique tolérante aux fautes "
        "et du Q-Day (l'arrivée d'un ordinateur quantique capable de casser la cryptographie à clé publique) : "
        "feuilles de route des fabricants, démonstrations publiées, étapes de la DARPA, revendications d'avantage "
        "et leurs contestations, estimations de ressources pour RSA et les courbes elliptiques, enquêtes d'experts, "
        "marchés prédictifs, prix publics, projections et résultats financiers.",
        "",
        "## Méthode : consigner sans trancher",
        "",
        "- Chaque ligne reprend une affirmation telle que sa source la formule, avec l'URL, la date de l'affirmation, "
        "la date de consultation et un statut. Le registre ne juge pas lui-même si un résultat de physique « tient » une promesse.",
        "- Un statut autre que « promis », « annoncé ou publié » ou « inconnu » doit citer la source qui le fonde : "
        "publication à comité de lecture, annonce de la DARPA, dépôt réglementaire, mesure indépendante, ou déclaration "
        "ultérieure de l'acteur lui-même. Le lien figure dans la colonne Statut.",
        "- Les conflits d'intérêts connus sont notés (fabricant qui estime sa propre feuille de route, vendeur à découvert, "
        "enquête financée par un fabricant).",
        "- Une contestation est une entrée à part, de type « réfutation ou contestation », liée à l'affirmation visée. "
        "L'affirmation garde son statut tant qu'aucune source ne la dit réfutée.",
        "- Les métriques des autres (Metriq, DARPA, publications évaluées par les pairs) sont reprises, pas recalculées.",
        "",
        "## Politique de correction",
        "",
        "- Une correction est une nouvelle ligne ou une mise à jour de statut qui cite sa source (`statut_source_url`, `statut_date`).",
        "- Un identifiant ne change jamais et une ligne n'est jamais supprimée sans trace : l'historique est celui du dépôt git, "
        "et chaque modification passe par un commit qui en donne la raison.",
        "- Une erreur matérielle (URL, chiffre mal recopié) se corrige en place, avec la source dans le message de commit.",
        "- Les demandes de correction des acteurs cités sont acceptées si elles s'appuient sur une source publique.",
        "",
        "## Lire les statuts",
        "",
    ]
    md += tableau([[f"`{k}`", v[0], v[1]] for k, v in STATUTS.items()], ["Code", "Libellé", "Signification"])
    md += [
        "",
        "Une date précédée de « ≤ » signifie que la source n'est pas datée : l'affirmation existait au plus tard à cette date. "
        "Une année ou un mois seuls indiquent la précision de la source. Les énoncés sont dans la langue de la source "
        "et peuvent être tronqués ici ; le JSONL contient le texte complet, les notes et les sources complémentaires.",
        "",
        "## Vue d'ensemble",
        "",
        f"{len(entrees)} affirmations, dont {nb_inconnu} au statut « inconnu, à vérifier » et {nb_apt} tirées de sources non datées.",
        "",
    ]
    par_type = Counter(e["type"] for e in entrees)
    par_statut = Counter(e["statut"] for e in entrees)
    md += tableau([[TYPES[t], str(n)] for t, n in sorted(par_type.items(), key=lambda kv: (-kv[1], kv[0]))],
                  ["Type", "Entrées"])
    md += [""]
    md += tableau([[STATUTS[s][0], str(n)] for s, n in sorted(par_statut.items(), key=lambda kv: (-kv[1], kv[0]))],
                  ["Statut", "Entrées"])

    # Section Q-Day
    qday_ids = {e["id"] for e in entrees
                if e["type"] in TYPES_QDAY or e["metrique"] == "taille_cle_cassee"}
    qday_ids |= {e["id"] for e in entrees
                 if e["type"] == "refutation" and any(l in qday_ids for l in e["liens"])}
    qday = sorted((par_id[i] for i in qday_ids), key=tri)
    md += [
        "",
        "## Q-Day : estimations de ressources, enquêtes et marchés",
        "",
        "Estimations publiées du coût d'une attaque contre RSA-2048 ou les courbes elliptiques, plus grande clé cassée "
        "publiquement, enquêtes et avis d'experts, marchés prédictifs, et contestations qui les visent. "
        "« Horizon » désigne l'échéance de la question posée.",
        "",
    ]
    md += tableau(
        [[date_affichee(e), cellule(e["acteur"]), TYPES[e["type"]], libelle_metrique(e["metrique"]), valeur(e),
          e["echeance_promise"] or "—", statut_affiche(e), enonce_affiche(e), source_affichee(e)]
         for e in qday],
        ["Date", "Acteur", "Type", "Métrique", "Valeur", "Horizon", "Statut", "Énoncé", "Source"],
    )

    # Sections par acteur : une section par acteur principal, qui reprend aussi les entrées
    # où il n'est qu'associé (mention « via ») ; les acteurs seulement associés sont résumés à la fin.
    groupes = defaultdict(list)
    for e in entrees:
        groupes[e["acteur"]].append((e, None))
    associes_seuls = defaultdict(list)
    for e in entrees:
        for a in e.get("acteurs_associes", []):
            (groupes[a] if a in groupes else associes_seuls[a]).append((e, e["acteur"]))
    acteurs = sorted(groupes, key=cle_tri_nom)
    md += [
        "",
        "## Par acteur",
        "",
        "Une section par acteur auteur d'au moins une affirmation. Les entrées où il n'est qu'associé "
        "(entreprise retenue par un programme, partenaire) portent la mention « via ». Les organisations "
        "seulement associées sont regroupées dans le dernier tableau.",
        "",
        " · ".join(f"[{cellule(a)}](#{ancre(a)}) ({len(groupes[a])})" for a in acteurs)
        + f" · [Organisations seulement associées](#acteurs-associes) ({len(associes_seuls)})",
    ]
    for a in acteurs:
        lignes = sorted(groupes[a], key=lambda ev: tri(ev[0]))
        md += ["", f'<a id="{ancre(a)}"></a>', "", f"### {a}", ""]
        md += tableau(
            [[date_affichee(e), TYPES[e["type"]], libelle_metrique(e["metrique"]), valeur(e),
              e["echeance_promise"] or "—", statut_affiche(e), enonce_affiche(e, via), source_affichee(e)]
             for e, via in lignes],
            ["Date", "Type", "Métrique", "Valeur", "Échéance", "Statut", "Énoncé", "Source"],
        )
    md += ["", '<a id="acteurs-associes"></a>', "", "### Organisations seulement associées", ""]
    md += tableau(
        [[cellule(a), "<br>".join(f"{date_affichee(e)} · via {cellule(via)} · `{e['id']}`"
                                  for e, via in sorted(associes_seuls[a], key=lambda ev: tri(ev[0])))]
         for a in sorted(associes_seuls, key=cle_tri_nom)],
        ["Organisation", "Entrées (date · acteur principal · identifiant)"],
    )
    md += [""]
    return "\n".join(md)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("fichier", nargs="?", default=str(ICI / "affirmations.jsonl"))
    ap.add_argument("-o", "--sortie", default=str(ICI / "registre.md"))
    args = ap.parse_args()
    entrees = charger(args.fichier)
    if not entrees:
        sys.exit("aucune entrée")
    Path(args.sortie).write_text(construire(entrees), encoding="utf-8")
    print(f"{args.sortie} écrit ({len(entrees)} affirmations)")


if __name__ == "__main__":
    main()
