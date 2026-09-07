import numpy as np
import pandas as pd
from typing import List
from src.taxonomy import EconomicSector

class V14MasterEconomyModel:
    """
    Unified Multi-Sector Macroeconomic Simulation Engine (V1.4).
    Simulates monthly public expenditures against traditional GST baseline 
    versus V1.4 Upstream Telemetry Framework.
    """
    def __init__(self, years: int = 5, gdp_growth_rate: float = 0.065):
        self.years = years
        self.months = years * 12
        self.gdp_growth_rate = gdp_growth_rate
        
        # Macro Base (Lakh INR)
        self.monthly_gross_base = 100000.0  # ₹10,000 Cr Base Monthly Volume
        
        # Monthly Outflow Baselines (Lakh INR)
        self.payroll_pensions = 1200.0
        self.debt_servicing = 600.0
        self.capex_infrastructure = 800.0
        self.social_welfare = 1053.13
        self.monthly_total_outflow = (
            self.payroll_pensions + self.debt_servicing + 
            self.capex_infrastructure + self.social_welfare
        )
        
        # Friction Parameters
        self.trad_compliance_rate = 0.70  # 70% audit compliance under GST
        self.v14_telemetry_friction = 0.05 # 5% evasion leakage
        
        # Default Taxed Sectors
        self.sectors: List[EconomicSector] = []

    def register_sector(self, sector: EconomicSector):
        self.sectors.append(sector)

    def run_simulation((self) -> pd.DataFrame:
        records = []
        cum_v14_treasury = 0.0
        cum_trad_treasury = 0.0
        cum_expenditure = 0.0
        
        for m in range(1, self.months + 1):
            growth_factor = (1 + self.gdp_growth_rate) ** (m / 12.0)
            base_vol = self.monthly_gross_base * growth_factor
            current_outflow = self.monthly_total_outflow * growth_factor
            
            # --- Traditional Indirect Tax Baseline ---
            trad_formal = (base_vol * 0.10 * self.trad_compliance_rate) * 0.05
            trad_informal = (base_vol * 0.50) * 0.002
            trad_excise = (base_vol * 0.08) * 0.20
            monthly_trad = trad_formal + trad_informal + trad_excise
            
            # --- V1.4 Upstream Telemetry Yield ---
            monthly_v14 = sum(
                sec.calculate_monthly_yield(base_vol, self.v14_telemetry_friction)
                for sec in self.sectors
            )
            # Add Agri-Procurement Post-MSP Share
            monthly_v14 += (118.83 * growth_factor)
            
            # Cumulative Totals
            cum_trad_treasury += monthly_trad
            cum_v14_treasury += monthly_v14
            cum_expenditure += current_outflow
            
            records.append({
                'Month': m,
                'Monthly_Outflow': current_outflow,
                'Monthly_Trad_Revenue': monthly_trad,
                'Monthly_V14_Revenue': monthly_v14,
                'Cum_Expenditure': cum_expenditure,
                'Cum_Trad_Revenue': cum_trad_treasury,
                'Cum_V14_Revenue': cum_v14_treasury,
                'Trad_Net_Position': cum_trad_treasury - cum_expenditure,
                'V14_Net_Position': cum_v14_treasury - cum_expenditure
            })
            
        return pd.DataFrame(records)
