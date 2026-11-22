"""Structures communes : détection brute et registre des règles."""
from __future__ import annotations

from dataclasses import dataclass, field

from .familles import Algo

CONFIANCES = ("elevee", "moyenne", "faible")
CONTEXTES = ("production", "test", "exemple", "documentation")

# identifiant de règle -> (langages, description). Rempli par les modules d'analyse.
REGISTRE: dict[str, tuple[str, str]] = {}


def enregistrer(regle: str, langages: str, description: str) -> str:
    if regle in REGISTRE and REGISTRE[regle] != (langages, description):
        raise ValueError(f"règle déjà définie différemment : {regle}")
    REGISTRE[regle] = (langages, description)
    return regle


@dataclass
class Detection:
    """Résultat brut d'une règle, avant mise au format du contrat."""

    ligne: int
    regle: str
    algo: Algo | None  # None : famille inconnue (rangé « à vérifier »)
    confiance: str
    fonctions: tuple[str, ...] = ()
    notes: list[str] = field(default_factory=list)
    extra: dict = field(default_factory=dict)  # version_tls, suites, certificat...
    extrait: str | None = None  # imposé (ex. en-tête PEM) au lieu de la ligne source
