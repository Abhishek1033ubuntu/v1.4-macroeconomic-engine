class EconomicSector:
    """
    Represents an economic sector classified under one of the 4 Universal Taxonomy Classes.
    Calculates tax yield based on upstream telemetry gate logic rather than store-level audits.
    """
    TAXONOMY_CLASSES = {
        "CLASS_1_PERISHABLE_AGRI": {
            "description": "Perishable, Bio-Resource & Agri (Fisheries, Dairy, Farming)",
            "taxable_share": 0.40,  # 60% informal/artisanal exempt
            "gate_rate": 0.030,      # 3.0% Processing/Harbor Gate Levy
        },
        "CLASS_2_HIGH_EXCISE": {
            "description": "High-Excise & Regulated Goods (Alcohol, Tobacco)",
            "taxable_share": 1.00,  # 100% captured at manufacturing/depot gate
            "gate_rate": 0.500,      # 50.0% Distillery/Depot Gate Levy
        },
        "CLASS_3_HEAVY_RESOURCE": {
            "description": "Heavy Resource, Energy & Capital Assets (Fuel, Power, Land)",
            "taxable_share": 1.00,  # 100% captured at grid/weighbridge/registry
            "gate_rate": 0.050,      # 5.0% Primary Grid/Registry Rail
        },
        "CLASS_4_DISCRETE_FMCG": {
            "description": "Discrete Manufacturing & Consumer Goods (Pharma, Textiles, FMCG)",
            "taxable_share": 0.35,  # 35% packaged B2B stock; unbranded staples 0%
            "gate_rate": 0.022,      # 2.2% B2B Wholesale Gate Levy
        }
    }

    def __init__(self, name: str, macro_share: float, taxonomy_class: str):
        if taxonomy_class not in self.TAXONOMY_CLASSES:
            raise ValueError(f"Invalid class '{taxonomy_class}'. Must be one of {list(self.TAXONOMY_CLASSES.keys())}")
        
        self.name = name
        self.macro_share = macro_share
        self.taxonomy_class = taxonomy_class
        self.config = self.TAXONOMY_CLASSES[taxonomy_class]

    def calculate_monthly_yield(self, base_volume: float, bypass_friction: float) -> float:
        """
        Calculates monthly upstream yield for the sector.
        """
        sector_volume = base_volume * self.macro_share
        taxable_volume = sector_volume * self.config["taxable_share"]
        effective_volume = taxable_volume * (1.0 - bypass_friction)
        return effective_volume * self.config["gate_rate"]
