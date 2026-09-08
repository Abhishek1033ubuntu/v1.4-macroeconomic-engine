# V1.4 Macroeconomic Upstream Telemetry Framework Engine
> **An Open-Source Macroeconomic Simulation System for Zero-Deficit Fiscal Policy**

<!-- Badges -->
[![Built with Gemini](https://img.shields.io/badge/Built%20with-Gemini%20AI-8E75B5?style=flat-square&logo=googlegemini&logoColor=white)](https://gemini.google.com)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22640628-blue?style=for-the-badge&logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22640628) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Executive Summary
Traditional tax frameworks (such as GST/VAT) rely heavily on merchant-level invoicing, post-facto tax filing, and intrusive store-level audits. This structural reliance creates massive compliance friction and revenue leakage, particularly within unorganized retail and informal economic sectors.

The **V1.4 Master Macroeconomic Framework** transitions indirect tax collection from **"merchant-level auditing"** to **"upstream physical telemetry."** By placing automated transaction and physical gate levies at primary supply chain bottlenecks (processing plants, refineries, B2B wholesale hubs, and digital registries), the state collects revenues automatically while guaranteeing a **0% tax and 0% audit burden** on small retailers and artisanal producers.

---

## The Universal 4-Class Upstream Taxonomy

Instead of writing bespoke tax rules for every industry, V1.4 classifies all business models into **4 Universal Taxonomy Classes**:

| Taxonomy Class | Scope / Target Sectors | Capture Node / Gate | Model Rate | Small-Producer Protection |
| :--- | :--- | :--- | :--- | :--- |
| **Class 1: Perishable / Agri** | Fisheries, Dairy, Agriculture | Processing Mills, Cold Storage, Harbors | **3.0%** | Primary farmers & fishermen = **0% Tax / 0% Audit** |
| **Class 2: High-Excise** | Alcohol, Spirits, Tobacco | Distillery / Depot Gates | **50.0%** | Retail shops buy duty-paid stock; keep standard margins |
| **Class 3: Heavy Resource / Energy** | Fuel Refineries, Power Grid, Real Estate | Grid Telemetry, Digital Land Registry | **4.5% – 6.0%** | Direct automated collection at major infrastructure nodes |
| **Class 4: Discrete FMCG** | Textiles, Pharma, Packaged FMCG, Kirana | Primary B2B Wholesale Gates | **2.2%** | Unbranded loose staples = **0% Zero-Rated** |

---

## Key Performance Results (5-Year Run)

Simulated over a 60-month period with an organic 6.5% annual GDP growth rate:

- **5-Year Public Expenditure Need:** ₹2,58,298.62 Lakhs
- **Traditional GST System Yield:** ₹1,44,947.53 Lakhs (**-₹1,13,351.09 Lakhs Deficit**)
- **V1.4 Framework Revenue Yield:** ₹4,33,257.36 Lakhs (**+₹1,74,958.74 Lakhs Net Surplus**)
- **Expenditure Coverage Ratio:** **167.7%** (Full Outflow Neutralization)

---

## Quick Start & Installation

```bash
# Clone the repository
git clone [https://github.com/your-username/v1.4-macroeconomic-engine.git](https://github.com/your-username/v1.4-macroeconomic-engine.git)
cd v1.4-macroeconomic-engine

# Install dependencies
pip install -r requirements.txt

# Run the master macroeconomic simulation
python main.py
```

Seeding New Business Models
Adding a new economic sector (e.g., Mining or Textiles) requires only a single-line declaration using the taxonomy engine:
```
from src.taxonomy import EconomicSector

# Seed Coal & Mining into the Engine
mining_sector = EconomicSector(
    name="Coal & Heavy Mining",
    macro_share=0.05,  # 5% of gross GDP
    taxonomy_class="CLASS_3_HEAVY_RESOURCE"
)

model.register_sector(mining_sector)
```

# Citation & Academic Reference

If you use this simulation model or framework in policy whitepapers or research articles, please cite:
```
@software{v14_macroeconomic_engine_2026,
  author = {Abhishek Singh},
  title = {V1.4 Macroeconomic Upstream Telemetry Framework: A Zero-Deficit Fiscal Simulation Engine},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{[https://github.com/Abhishek1033ubuntu/v1.4-macroeconomic-engine](https://github.com/Abhishek1033ubuntu/v1.4-macroeconomic-engine)}}
}
```
# License

Distributed under the MIT License. See LICENSE for details.


