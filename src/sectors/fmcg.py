from src.taxonomy import EconomicSector

fmcg_formal = EconomicSector(
    name="FMCG Formal Retail",
    macro_share=0.10,
    taxonomy_class="CLASS_3_HEAVY_RESOURCE"  # Captured via 5% Upstream Freight/Highway Rail
)

fmcg_informal = EconomicSector(
    name="FMCG Kirana / Informal",
    macro_share=0.50,
    taxonomy_class="CLASS_4_DISCRETE_FMCG"  # Captured via 2.2% B2B Wholesale Gate
)
