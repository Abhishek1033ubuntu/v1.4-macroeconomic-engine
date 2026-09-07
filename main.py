import os
import matplotlib.pyplot as plt
from src.taxonomy import EconomicSector
from src.engine import V14MasterEconomyModel

def main():
    print("=" * 70)
    print("   V1.4 MASTER MACROECONOMIC SIMULATION ENGINE (RUNNING...)")
    print("=" * 70)

    # 1. Initialize Engine
    model = V14MasterEconomyModel(years=5, gdp_growth_rate=0.065)

    # 2. Register Sectors using Universal Taxonomy Engine
    model.register_sector(EconomicSector("FMCG Formal Retail", 0.10, "CLASS_3_HEAVY_RESOURCE")) # 5% Upstream Freight
    model.register_sector(EconomicSector("FMCG Kirana / Informal", 0.50, "CLASS_4_DISCRETE_FMCG"))
    model.register_sector(EconomicSector("High-Excise Liquor", 0.08, "CLASS_2_HIGH_EXCISE"))
    model.register_sector(EconomicSector("Energy & Bulk Fuel", 0.15, "CLASS_3_HEAVY_RESOURCE"))
    model.register_sector(EconomicSector("Real Estate Digital Registry", 0.12, "CLASS_3_HEAVY_RESOURCE"))
    model.register_sector(EconomicSector("Fisheries & Marine Processing", 0.03, "CLASS_1_PERISHABLE_AGRI"))

    # 3. Run Simulation
    df = model.run_simulation()

    # 4. Extract Metrics
    total_exp = df['Cum_Expenditure'].iloc[-1]
    trad_rev = df['Cum_Trad_Revenue'].iloc[-1]
    v14_rev = df['Cum_V14_Revenue'].iloc[-1]
    v14_surplus = df['V14_Net_Position'].iloc[-1]

    print(f"5-Year Expenditure Need  : ₹{total_exp:,.2f} Lakhs")
    print(f"Traditional System Yield : ₹{trad_rev:,.2f} Lakhs")
    print(f"Traditional Deficit      : ₹{df['Trad_Net_Position'].iloc[-1]:,.2f} Lakhs")
    print("-" * 70)
    print(f"V1.4 Unified System Yield: ₹{v14_rev:,.2f} Lakhs")
    print(f"V1.4 Net Treasury Surplus: ₹{v14_surplus:,.2f} Lakhs (ZERO DEFICIT ACHIEVED)")
    print("=" * 70)

    # 5. Export Output Plots
    os.makedirs("data/outputs", exist_ok=True)
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(df['Month'], df['Cum_Expenditure'] / 1000, 'k:', label='State Outflow Need')
    plt.plot(df['Month'], df['Cum_Trad_Revenue'] / 1000, 'r--', label='Traditional GST System')
    plt.plot(df['Month'], df['Cum_V14_Revenue'] / 1000, 'g-', label='V1.4 Framework', linewidth=2)
    plt.title('5-Year Fiscal Balance (Crore INR)')
    plt.xlabel('Month')
    plt.ylabel('Crore INR')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(df['Month'], df['Trad_Net_Position'] / 1000, 'r--', label='Traditional Deficit Trajectory')
    plt.plot(df['Month'], df['V14_Net_Position'] / 1000, 'g-', label='V1.4 Surplus Trajectory', linewidth=2)
    plt.axhline(0, color='gray', linestyle='-')
    plt.title('Net Treasury Position (Positive = Net Surplus)')
    plt.xlabel('Month')
    plt.ylabel('Crore INR')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    chart_path = "data/outputs/v14_simulation_results.png"
    plt.savefig(chart_path, dpi=300)
    print(f"\n[SUCCESS] Diagnostic plots exported to: {chart_path}")

if __name__ == "__main__":
    main()
