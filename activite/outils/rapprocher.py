#!/usr/bin/env python3
"""Rapproche les prospects (entreprises quantiques) des opportunités de financement.

Le moteur signale des pistes ; il ne décide jamais de l'éligibilité. Chaque piste
porte ses raisons, ses réserves et les liens vers les sources, pour qu'un humain
confirme avant tout envoi.

Usage :
    python3 rapprocher.py \
        --prospects ../prospects/prospects.jsonl \
        --opportunites ../opportunites/opportunites.jsonl \
        --groupes ../opportunites/groupes_pays.json \
        --aujourdhui 2026-11-22 \
        --sortie rapprochements.jsonl \
        --fiches fiches/ --nb-fiches 20
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

STATUTS_ACTIFS = {"ouvert", "a_venir"}
SEGMENTS_LARGES = {"transverse", "inconnu"}
MOTS_VIDES = {
    "the", "and", "for", "with", "of", "in", "on", "to", "a", "an", "des", "les", "pour",
    "et", "de", "la", "le", "du", "en", "quantum", "quantique", "quantiques", "technology",
    "technologies", "project", "projet", "based", "using", "new", "novel", "development",
}


def lire_jsonl(chemin: Path) -> list[dict]:
    lignes = []
    with chemin.open(encoding="utf-8") as f:
        for numero, ligne in enumerate(f, 1):
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                lignes.append(json.loads(ligne))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{chemin}:{numero}: JSON invalide ({exc})")
    return lignes


def date_iso(valeur) -> dt.date | None:
    if not valeur:
        return None
    try:
        return dt.date.fromisoformat(str(valeur)[:10])
    except ValueError:
        return None


def developper_pays(pays_eligibles, groupes: dict) -> set[str] | None:
    """Renvoie l'ensemble des codes pays éligibles, ou None si l'information manque."""
    if not pays_eligibles:
        return None
    codes: set[str] = set()
    for item in pays_eligibles:
        if item in groupes and isinstance(groupes[item], list):
            codes.update(groupes[item])
        elif isinstance(item, str) and re.fullmatch(r"[A-Z]{2}", item):
            codes.add(item)
        else:
            # Groupe inconnu : on ne peut pas conclure.
            return None
    return codes


def jetons(texte: str) -> set[str]:
    mots = re.findall(r"[a-zà-ÿ0-9-]{3,}", texte.lower())
    return {m for m in mots if m not in MOTS_VIDES}


def texte_prospect(p: dict) -> str:
    morceaux = [p.get("segment_justification") or ""]
    for f in p.get("financements_obtenus") or []:
        morceaux.append(f.get("projet") or "")
        morceaux.append(f.get("acronyme") or "")
    return " ".join(morceaux)


def evaluer(p: dict, o: dict, groupes: dict, aujourdhui: dt.date) -> dict | None:
    """Renvoie une piste (dict) ou None si l'opportunité est hors jeu pour ce prospect."""
    if o.get("statut") not in STATUTS_ACTIFS:
        return None
    cloture = date_iso(o.get("cloture"))
    if cloture is not None and cloture < aujourdhui:
        return None

    raisons: list[str] = []
    reserves: list[str] = []
    eligibilite: list[str] = []
    score = 0

    # Éligibilité géographique.
    pays_ok = developper_pays(o.get("pays_eligibles"), groupes)
    if pays_ok is None:
        reserves.append("pays éligibles non précisés ou groupe inconnu : à vérifier dans le texte de l'appel")
    elif p.get("pays") not in pays_ok:
        return None
    else:
        eligibilite.append(f"le pays ({p.get('pays')})")

    # Type d'organisation.
    types = o.get("types_eligibles") or []
    if types:
        if p.get("type_org") not in types:
            return None
        eligibilite.append(f"le type d'organisation ({p.get('type_org')})")
    else:
        reserves.append("types d'organisation éligibles non précisés")

    # Adéquation technologique.
    seg_p = p.get("segment") or "inconnu"
    segs_o = set(o.get("segments") or [])
    mots_o = jetons(" ".join(o.get("mots_cles") or []) + " " + (o.get("intitule") or ""))
    communs = sorted(mots_o & jetons(texte_prospect(p)))
    if seg_p in segs_o and seg_p not in SEGMENTS_LARGES:
        score += 40
        raisons.append(f"segment « {seg_p} » visé par l'appel")
    elif "transverse" in segs_o or seg_p in SEGMENTS_LARGES:
        # Appel généraliste ou segment flou : on n'en parle que si un lien thématique existe.
        if not communs:
            return None
        score += 10
        if "transverse" in segs_o:
            raisons.append("appel ouvert à toutes les technologies quantiques")
        else:
            reserves.append("segment de l'entreprise incertain : adéquation à confirmer")
    else:
        return None

    if communs:
        score += min(20, 5 * len(communs))
        # Le projet passé le plus proche de l'appel sert d'argument concret.
        meilleur, communs_meilleur = None, set()
        for f in p.get("financements_obtenus") or []:
            c = mots_o & jetons(f"{f.get('projet') or ''} {f.get('acronyme') or ''}")
            if len(c) > len(communs_meilleur):
                meilleur, communs_meilleur = f, c
        if meilleur:
            raisons.append(
                f"votre projet {meilleur.get('acronyme') or meilleur.get('projet')} ({meilleur.get('programme')}, "
                f"{(meilleur.get('debut') or '')[:4]}) porte sur des thèmes proches de l'appel : "
                + ", ".join(sorted(communs_meilleur)[:5])
            )
        else:
            raisons.append("thèmes communs entre vos projets passés et l'appel : " + ", ".join(communs[:6]))

    # Activité récente : un projet encore en cours vaut mieux qu'un historique ancien.
    derniere = date_iso(p.get("derniere_activite"))
    if derniere and derniere >= aujourdhui:
        score += 5
        raisons.append("au moins un projet financé encore en cours")
    elif derniere and derniere < dt.date(2022, 1, 1):
        score -= 10
        reserves.append(f"dernier projet financé terminé en {derniere.year} : l'activité actuelle est à confirmer")

    # Expérience des financements publics.
    financements = p.get("financements_obtenus") or []
    pilotes = [f for f in financements if f.get("role") in ("coordinateur", "beneficiaire_unique")]
    if pilotes:
        score += 10
        plus_gros = max(pilotes, key=lambda f: f.get("contribution_eur") or 0)
        role = "coordonné" if plus_gros.get("role") == "coordinateur" else "porté seul"
        raisons.append(
            f"vous avez déjà {role} un projet financé ({plus_gros.get('acronyme') or plus_gros.get('projet')}, "
            f"{plus_gros.get('programme')}, {format_eur(plus_gros.get('contribution_eur'))})"
        )
    if len(financements) >= 2:
        score += 5
        raisons.append(f"{len(financements)} projets financés dans votre historique public")
    financeur = (o.get("financeur") or "").lower()
    programme = (o.get("programme") or "").lower()
    if any(
        (f.get("programme") or "").lower() in (financeur + " " + programme)
        for f in financements
        if f.get("programme")
    ):
        score += 10
        raisons.append("vous connaissez déjà ce programme ou ce financeur")

    # Calendrier.
    jours = (cloture - aujourdhui).days if cloture else None
    if jours is None:
        reserves.append("date de clôture inconnue")
    elif jours < 14:
        reserves.append(f"clôture dans {jours} jours : délai probablement trop court")
    elif jours <= 90:
        score += 10
    else:
        score += 5

    if o.get("consortium_requis"):
        taille = o.get("taille_min_consortium")
        reserves.append(
            "consortium à constituer" + (f" (au moins {taille} partenaires)" if taille else "")
        )
    if o.get("confiance") == "faible":
        reserves.append("informations de l'appel non vérifiées sur la source primaire")

    return {
        "prospect_id": p.get("id"),
        "prospect_nom": p.get("nom"),
        "opportunite_id": o.get("id"),
        "opportunite_intitule": o.get("intitule"),
        "financeur": o.get("financeur"),
        "cloture": o.get("cloture"),
        "jours_avant_cloture": jours,
        "score": max(0, min(score, 100)),
        "raisons": raisons,
        "eligibilite": eligibilite,
        "reserves": reserves,
        "liens": {
            "prospect": (p.get("sources") or [None])[0],
            "opportunite": o.get("url") or o.get("source_url"),
        },
    }


def rapprocher(prospects, opportunites, groupes, aujourdhui, score_min=30, max_par_prospect=5):
    pistes = []
    for p in prospects:
        siennes = [x for o in opportunites if (x := evaluer(p, o, groupes, aujourdhui)) and x["score"] >= score_min]
        siennes.sort(key=lambda x: (-x["score"], x["jours_avant_cloture"] if x["jours_avant_cloture"] is not None else 10**6))
        for x in siennes[:max_par_prospect]:
            x["type_org"] = p.get("type_org")
        pistes.extend(siennes[:max_par_prospect])
    pistes.sort(key=lambda x: (-x["score"], x["jours_avant_cloture"] if x["jours_avant_cloture"] is not None else 10**6))
    return pistes


def format_eur(montant) -> str:
    if montant is None:
        return "montant non publié"
    return f"{montant:,.0f} €".replace(",", " ")


AIDE_GRATUITE = {
    "GB": "à Innovate UK Business Connect (https://iuk-business-connect.org.uk/) et au Point de contact national "
          "britannique pour Horizon Europe (https://www.ukri.org/apply-for-funding/horizon-europe/)",
}
AIDE_GRATUITE_DEFAUT = (
    "au Point de contact national de votre pays "
    "(https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/support/ncp) et au réseau "
    "Enterprise Europe Network (https://een.ec.europa.eu/)"
)


def slug(texte: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", texte.lower()).strip("-")


def ecrire_fiche(dossier: Path, p: dict, piste: dict, o: dict, aujourdhui: dt.date, signature: str) -> Path:
    """Fiche opportunité (service A) : une entreprise, un appel, une page. Format de
    offre/LIVRABLES/fiche-opportunite.md ; un humain la relit avant tout envoi."""
    ident = o.get("identifiant_appel") or o.get("id")
    lignes = [
        f"# Fiche opportunité : {p.get('nom')} × {ident}",
        "",
        f"*Fiche gratuite, établie le {aujourdhui.isoformat()} à partir de données publiques uniquement. "
        "Ce n'est ni un avis d'éligibilité, ni une recommandation de candidater.*",
        "",
        "## Ce que disent les sources publiques sur vos financements",
        "",
        f"| Programme | Projet (acronyme) | Période | Contribution à {p.get('nom')} | Rôle | Source |",
        "|---|---|---|---|---|---|",
    ]
    for f in sorted(p.get("financements_obtenus") or [], key=lambda x: x.get("debut") or "", reverse=True)[:4]:
        lignes.append(
            f"| {f.get('programme')} | {f.get('acronyme') or f.get('projet')} | {f.get('debut') or '?'} → "
            f"{f.get('fin') or '?'} | {format_eur(f.get('contribution_eur'))} | {f.get('role')} | "
            f"[fiche publique]({f.get('source_url')}) |"
        )
    reste = len(p.get("financements_obtenus") or []) - 4
    if reste > 0:
        lignes.append(f"| … | {reste} autre(s) projet(s) | | | | |")
    lignes += [
        "",
        f"Segment retenu : **{p.get('segment')}**. Justification : {p.get('segment_justification') or 'non précisée'}.",
        "",
        "## L'appel",
        "",
        f"- **{o.get('intitule')}** ({ident}), {o.get('financeur')}, {o.get('programme') or 'programme à préciser'}.",
        f"- **Clôture : {o.get('cloture') or 'inconnue'}** (heure et fuseau à relire sur la page officielle). "
        f"Vérifiée le {o.get('date_verification') or '?'} sur la [page officielle]({o.get('url') or o.get('source_url')}).",
        f"- Nature : {o.get('nature') or 'à vérifier'}. Budget : {format_eur(o.get('budget_total_eur'))}. "
        f"Montant indicatif par projet : {format_eur(o.get('montant_par_projet_eur'))}.",
        "- Consortium : "
        + ((f"exigé, au moins {o['taille_min_consortium']} entités" if o.get("taille_min_consortium") else "exigé")
           if o.get("consortium_requis") else "non exigé")
        + f". Pays éligibles : {', '.join(o.get('pays_eligibles') or ['à vérifier'])}.",
        "",
        "## Pourquoi cet appel pourrait vous concerner",
        "",
    ]
    lignes += [f"{i}. {r[0].upper() + r[1:]}." for i, r in enumerate(piste["raisons"][:4], 1)]
    if piste.get("eligibilite"):
        lignes += ["", "D'après la fiche de l'appel, " + " et ".join(piste["eligibilite"])
                   + " semblent compatibles avec les conditions de participation, sous réserve des règles détaillées."]
    lignes += ["", "## À vérifier avant d'y consacrer du temps", ""]
    reserves = piste["reserves"] or ["conditions détaillées d'éligibilité et taux de financement, sur la page du topic"]
    lignes += [f"- {r[0].upper() + r[1:]}." for r in reserves]
    jours = piste["jours_avant_cloture"]
    lignes += ["", "## Calendrier", ""]
    if jours is None:
        lignes.append("La date de clôture n'est pas connue : à confirmer avant toute préparation.")
    else:
        semaines = jours // 7
        if o.get("consortium_requis") and semaines < 12:
            realisme = "réaliste surtout si un consortium existe déjà ou se forme dans les prochaines semaines"
        elif semaines < 3:
            realisme = "délai très court"
        else:
            realisme = "délai suffisant pour préparer un dossier sérieux"
        lignes.append(f"Il reste **{semaines} semaine(s)** avant la clôture : {realisme}.")
    lignes += [
        "",
        "## Aide gratuite",
        "",
        f"Vous pouvez aussi vous adresser gratuitement {AIDE_GRATUITE.get(p.get('pays'), AIDE_GRATUITE_DEFAUT)}, "
        "ainsi qu'au service d'assistance indiqué sur la page de l'appel.",
        "",
        "## Pour aller plus loin",
        "",
        "Si vous le souhaitez, une **note d'éligibilité et d'adéquation** tranche en 5 jours ouvrés : go, go sous "
        "conditions ou no-go, avec les justifications. Elle coûte 490 € HT (245 € pour les 5 premiers clients) et "
        "elle est remboursée si je la livre en retard.",
        "",
        "---",
        f"*{signature}. Fiche préparée avec des outils d'IA sur des sources publiques, puis vérifiée et rédigée par "
        "un humain. Elle peut contenir des erreurs ; aucune garantie de résultat. Mon historique : 0 dossier "
        "accompagné à ce jour. Pour ne plus recevoir de fiches : répondez « stop ».*",
        "",
    ]
    chemin = dossier / f"{slug(p.get('nom') or p.get('id'))}--{slug(ident)}.md"
    chemin.write_text("\n".join(lignes), encoding="utf-8")
    return chemin


def ecrire_tableau(chemin: Path, classement: list, index_p: dict, aujourdhui: dt.date) -> None:
    """Vue interne pour le fondateur : toutes les pistes, prospect par prospect."""
    lignes = [
        f"# Pistes par prospect (usage interne, {aujourdhui.isoformat()})",
        "",
        "Chaque piste est une hypothèse du moteur. Avant d'envoyer une fiche, suivre la liste de contrôle de "
        "`offre/LIVRABLES/fiche-opportunite.md`.",
        "",
        "| Prospect | Type | Pays | Segment | Appel | Clôture | Score | Réserves |",
        "|---|---|---|---|---|---|---:|---|",
    ]
    for pid, pistes in classement:
        p = index_p[pid]
        for piste in pistes:
            lignes.append(
                f"| {p.get('nom')} | {p.get('type_org')} | {p.get('pays')} | {p.get('segment')} | {piste['opportunite_intitule']} | "
                f"{piste['cloture'] or '?'} | {piste['score']} | {len(piste['reserves'])} |"
            )
    chemin.write_text("\n".join(lignes) + "\n", encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prospects", type=Path, required=True)
    ap.add_argument("--opportunites", type=Path, required=True)
    ap.add_argument("--groupes", type=Path, required=True)
    ap.add_argument("--aujourdhui", default=dt.date.today().isoformat())
    ap.add_argument("--score-min", type=int, default=30)
    ap.add_argument("--max-pistes", type=int, default=5, help="pistes gardées par prospect")
    ap.add_argument("--types-fiches", default="PME",
                    help="types d'organisation qui reçoivent une fiche, séparés par des virgules (défaut : PME)")
    ap.add_argument("--sortie", type=Path, default=Path("rapprochements.jsonl"))
    ap.add_argument("--fiches", type=Path, help="dossier où écrire les fiches Markdown")
    ap.add_argument("--nb-fiches", type=int, default=20, help="nombre de prospects qui reçoivent une fiche")
    ap.add_argument("--part-quantique-min", type=float, default=0.5,
                    help="part minimale des projets publics de l'entreprise qui portent sur le quantique (si connue)")
    ap.add_argument("--signature", default="{Nom commercial}, {Prénom Nom}, {e-mail}",
                    help="pied de page des fiches (nom commercial, nom, e-mail du fondateur)")
    args = ap.parse_args(argv)

    aujourdhui = dt.date.fromisoformat(args.aujourdhui)
    prospects = lire_jsonl(args.prospects)
    opportunites = lire_jsonl(args.opportunites)
    groupes = json.loads(args.groupes.read_text(encoding="utf-8"))

    pistes = rapprocher(prospects, opportunites, groupes, aujourdhui, args.score_min, args.max_pistes)
    with args.sortie.open("w", encoding="utf-8") as f:
        for piste in pistes:
            f.write(json.dumps(piste, ensure_ascii=False) + "\n")

    par_prospect: dict[str, list[dict]] = {}
    for piste in pistes:
        par_prospect.setdefault(piste["prospect_id"], []).append(piste)
    print(f"{len(prospects)} prospects, {len(opportunites)} opportunités, {len(pistes)} pistes "
          f"(score ≥ {args.score_min}), {len(par_prospect)} prospects avec au moins une piste.")

    if args.fiches:
        args.fiches.mkdir(parents=True, exist_ok=True)
        index_p = {p.get("id"): p for p in prospects}
        index_o = {o.get("id"): o for o in opportunites}
        classement = sorted(par_prospect.items(), key=lambda kv: -max(x["score"] for x in kv[1]))
        ecrire_tableau(args.fiches / "_pistes-par-prospect.md", classement, index_p, aujourdhui)
        types_fiches = {t.strip() for t in args.types_fiches.split(",") if t.strip()}

        def cible(p: dict) -> bool:
            """Cible commerciale : PME dont le quantique est le cœur de métier, hors cabinets de projets européens."""
            if p.get("type_org") not in types_fiches or p.get("profil_consultant_ue"):
                return False
            part = p.get("part_quantique")
            return part is None or part >= args.part_quantique_min

        eligibles = [(pid, ps) for pid, ps in classement if cible(index_p[pid])]
        print(f"{len(eligibles)} prospects ciblés (types {', '.join(sorted(types_fiches))}, "
              f"part quantique ≥ {args.part_quantique_min}, hors profils de consultants).")
        for pid, ses_pistes in eligibles[: args.nb_fiches]:
            meilleure = ses_pistes[0]
            chemin = ecrire_fiche(args.fiches, index_p[pid], meilleure, index_o[meilleure["opportunite_id"]],
                                  aujourdhui, args.signature)
            print(f"fiche : {chemin}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
