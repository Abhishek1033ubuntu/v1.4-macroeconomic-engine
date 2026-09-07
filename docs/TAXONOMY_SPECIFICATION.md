# Universal 4-Class Upstream Taxonomy Specification

## 1. Overview
The V1.4 Upstream Taxonomy Engine solves the scalability challenge of indirect tax modeling. Instead of configuring custom logic for every individual industry, economic sectors are mapped into one of four primary physical supply-chain archetypes.

---

## 2. Taxonomy Classes Specification

### Class 1: Perishable / Agri (`CLASS_1_PERISHABLE_AGRI`)
- **Target Sectors:** Fisheries, Aquaculture, Dairy, Fresh Produce, Grain Farming.
- **Economic Mechanics:** Highly perishable goods with a large unorganized primary producer base.
- **Capture Strategy:**
  - Primary Artisanal/Farmer Volume: **0% Taxed / 0% Audited** (Exempt).
  - Commercial Gate: Tax applied exclusively at primary aggregation nodes (cold storage, processing/canning units, dairy plants).
- **Default Parameters:** 40% taxable commercial share, **3.0% Gate Levy**.

### Class 2: High-Excise Goods (`CLASS_2_HIGH_EXCISE`)
- **Target Sectors:** Alcohol, Spirits, Tobacco, Gaming.
- **Economic Mechanics:** High-tax commodities where downstream merchant tax enforcement leads to smuggling and compliance evasion.
- **Capture Strategy:** 
  - Tax point placed 100% upstream at distillery gates and manufacturing depots.
  - Retail merchants purchase duty-paid stock and operate on standard profit margins.
- **Default Parameters:** 100% taxable gate share, **50.0% Distillery/Depot Levy**.

### Class 3: Heavy Resource, Energy & Digital Assets (`CLASS_3_HEAVY_RESOURCE`)
- **Target Sectors:** Fuel Refineries, Power Generation, Real Estate Registries, Mining.
- **Economic Mechanics:** High-value, centralized physical infrastructure or legally mandated registries.
- **Capture Strategy:**
  - Direct digital telemetry integration at refineries, power grid entry points, and land registry clearance.
- **Default Parameters:** 100% telemetry share, **4.5% – 6.0% Automated Rail Rate**.

### Class 4: Discrete Manufacturing & Consumer Goods (`CLASS_4_DISCRETE_FMCG`)
- **Target Sectors:** Packaged FMCG, Consumer Electronics, Pharmaceuticals, Textiles.
- **Economic Mechanics:** Multi-tier wholesale distribution supplying millions of micro-retailers (Kirana stores).
- **Capture Strategy:**
  - Unbranded loose staples: **0% Zero-Rated**.
  - Packaged stock captured exclusively at primary B2B wholesale distribution hubs.
- **Default Parameters:** 35% packaged stock ratio, **2.2% B2B Wholesale Gate Levy**.
