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
    score = 0

    # Éligibilité géographique.
    pays_ok = developper_pays(o.get("pays_eligibles"), groupes)
    if pays_ok is None:
        reserves.append("pays éligibles non précisés ou groupe inconnu : à vérifier dans le texte de l'appel")
    elif p.get("pays") not in pays_ok:
        return None
    else:
        raisons.append(f"pays {p.get('pays')} éligible")

    # Type d'organisation.
    types = o.get("types_eligibles") or []
    if types:
        if p.get("type_org") not in types:
            return None
        raisons.append(f"type d'organisation {p.get('type_org')} éligible")
    else:
        reserves.append("types d'organisation éligibles non précisés")

    # Adéquation technologique.
    seg_p = p.get("segment") or "inconnu"
    segs_o = set(o.get("segments") or [])
    if seg_p in segs_o:
        score += 40
        raisons.append(f"segment « {seg_p} » visé par l'appel")
    elif "transverse" in segs_o:
        score += 20
        raisons.append("appel ouvert à tous les segments quantiques")
    elif seg_p in SEGMENTS_LARGES:
        score += 10
        reserves.append("segment de l'entreprise incertain : adéquation à confirmer")
    else:
        return None

    mots_o = jetons(" ".join(o.get("mots_cles") or []) + " " + (o.get("intitule") or ""))
    communs = sorted(mots_o & jetons(texte_prospect(p)))
    if communs:
        bonus = min(20, 5 * len(communs))
        score += bonus
        raisons.append("mots-clés communs avec ses projets passés : " + ", ".join(communs[:6]))

    # Expérience des financements publics.
    financements = p.get("financements_obtenus") or []
    if any(f.get("role") == "coordinateur" for f in financements):
        score += 10
        raisons.append("a déjà coordonné un projet financé")
    if len(financements) >= 2:
        score += 5
        raisons.append(f"{len(financements)} projets financés dans l'historique public")
    financeur = (o.get("financeur") or "").lower()
    programme = (o.get("programme") or "").lower()
    if any(
        (f.get("programme") or "").lower() in (financeur + " " + programme)
        for f in financements
        if f.get("programme")
    ):
        score += 10
        raisons.append("connaît déjà ce programme ou ce financeur")

    # Calendrier.
    jours = (cloture - aujourdhui).days if cloture else None
    if jours is None:
        reserves.append("date de clôture inconnue")
    elif jours < 14:
        reserves.append(f"clôture dans {jours} jours : délai probablement trop court")
    elif jours <= 90:
        score += 10
        raisons.append(f"clôture dans {jours} jours")
    else:
        score += 5
        raisons.append(f"clôture dans {jours} jours : temps de préparer un bon dossier")

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
        "score": min(score, 100),
        "raisons": raisons,
        "reserves": reserves,
        "liens": {
            "prospect": (p.get("sources") or [None])[0],
            "opportunite": o.get("url") or o.get("source_url"),
        },
    }


def rapprocher(prospects, opportunites, groupes, aujourdhui, score_min=30):
    pistes = []
    for p in prospects:
        for o in opportunites:
            piste = evaluer(p, o, groupes, aujourdhui)
            if piste and piste["score"] >= score_min:
                pistes.append(piste)
    pistes.sort(key=lambda x: (-x["score"], x["jours_avant_cloture"] if x["jours_avant_cloture"] is not None else 10**6))
    return pistes


def format_eur(montant) -> str:
    if montant is None:
        return "montant non publié"
    return f"{montant:,.0f} €".replace(",", " ")


def ecrire_fiche(dossier: Path, p: dict, pistes: list[dict], opp_index: dict, aujourdhui: dt.date) -> Path:
    nom_fichier = re.sub(r"[^a-z0-9]+", "-", (p.get("nom") or p.get("id")).lower()).strip("-") + ".md"
    lignes = [
        f"# Pistes de financement public — {p.get('nom')}",
        "",
        f"*Fiche préparée le {aujourdhui.isoformat()} à partir de données publiques. "
        "Elle signale des pistes à vérifier ; ce n'est pas un avis d'éligibilité.*",
        "",
        "## Ce que les données publiques montrent",
        "",
        f"- Pays : {p.get('pays')} ; type : {p.get('type_org')} ; segment estimé : {p.get('segment')}.",
        f"- Projets financés recensés : {p.get('nb_projets', len(p.get('financements_obtenus') or []))}, "
        f"pour un total de {format_eur(p.get('total_obtenu_eur'))}.",
    ]
    for f in sorted(p.get("financements_obtenus") or [], key=lambda x: x.get("debut") or "", reverse=True)[:5]:
        lignes.append(
            f"  - {f.get('acronyme') or f.get('projet')} ({f.get('programme')}, {f.get('role')}, "
            f"{format_eur(f.get('contribution_eur'))}) — [source]({f.get('source_url')})"
        )
    lignes += ["", "## Appels qui semblent correspondre", ""]
    for i, piste in enumerate(pistes, 1):
        o = opp_index.get(piste["opportunite_id"], {})
        lignes += [
            f"### {i}. {piste['opportunite_intitule']}",
            "",
            f"- Financeur : {piste['financeur']} ; clôture : {piste['cloture'] or 'inconnue'}"
            + (f" (dans {piste['jours_avant_cloture']} jours)" if piste["jours_avant_cloture"] is not None else ""),
            f"- Budget : {format_eur(o.get('budget_total_eur'))} au total ; "
            f"par projet : {format_eur(o.get('montant_par_projet_eur'))}.",
            f"- Pourquoi : " + " ; ".join(piste["raisons"]) + ".",
        ]
        if piste["reserves"]:
            lignes.append("- À vérifier : " + " ; ".join(piste["reserves"]) + ".")
        lignes += [f"- Texte de l'appel : {piste['liens']['opportunite']}", ""]
    lignes += [
        "## Limites",
        "",
        "Cette fiche est produite automatiquement à partir des bases publiques (CORDIS, UKRI et portails "
        "des financeurs), puis relue. Elle ignore les financements nationaux non publiés et ne connaît "
        "ni la stratégie, ni la feuille de route de l'entreprise. L'éligibilité se confirme toujours dans "
        "le texte officiel de l'appel.",
        "",
    ]
    chemin = dossier / nom_fichier
    chemin.write_text("\n".join(lignes), encoding="utf-8")
    return chemin


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prospects", type=Path, required=True)
    ap.add_argument("--opportunites", type=Path, required=True)
    ap.add_argument("--groupes", type=Path, required=True)
    ap.add_argument("--aujourdhui", default=dt.date.today().isoformat())
    ap.add_argument("--score-min", type=int, default=30)
    ap.add_argument("--sortie", type=Path, default=Path("rapprochements.jsonl"))
    ap.add_argument("--fiches", type=Path, help="dossier où écrire les fiches Markdown")
    ap.add_argument("--nb-fiches", type=int, default=20)
    ap.add_argument("--pistes-par-fiche", type=int, default=3)
    args = ap.parse_args(argv)

    aujourdhui = dt.date.fromisoformat(args.aujourdhui)
    prospects = lire_jsonl(args.prospects)
    opportunites = lire_jsonl(args.opportunites)
    groupes = json.loads(args.groupes.read_text(encoding="utf-8"))

    pistes = rapprocher(prospects, opportunites, groupes, aujourdhui, args.score_min)
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
        for pid, ses_pistes in classement[: args.nb_fiches]:
            chemin = ecrire_fiche(args.fiches, index_p[pid], ses_pistes[: args.pistes_par_fiche], index_o, aujourdhui)
            print(f"fiche : {chemin}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
