"""
Sector-specific configurations for the V1.4 Macroeconomic Engine.
"""

from src.sectors.fmcg import fmcg_formal, fmcg_informal
from src.sectors.excise import liquor_excise
from src.sectors.energy import energy_fuel
from src.sectors.real_estate import real_estate
from src.sectors.fisheries import fisheries

__all__ = [
    "fmcg_formal",
    "fmcg_informal",
    "liquor_excise",
    "energy_fuel",
    "real_estate",
    "fisheries",
]
