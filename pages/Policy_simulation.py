import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils import DataManager

st.set_page_config(page_title="🔄 Smart Resource Allocation & Policy Simulation", layout="wide")
st.title("💡 Smart Resource Allocation & Policy Impact Simulation")


# Load data
dm = DataManager()
building = dm.load_energy()
gas = dm.load_gas()
water = dm.load_water()

st.sidebar.title("⚙️ Configuration")
campus = st.sidebar.selectbox("Select Campus", sorted(building['campus_id'].unique()))
policy = st.sidebar.multiselect("Apply Policies", 
    ["Reduce Heating by 10%", "Efficient Water Fixtures", "Solar Panels Installed", "Shorten Building Hours"])

bld_c = building[building["campus_id"] == campus]
gas_c = gas[gas["campus_id"] == campus]
water_c = water[water["campus_id"] == campus]

st.subheader("💸 Resource Allocation and Optimization Simulation")

def simulate_allocation_reduction(df, policy):
    impact_factors = {
        "Reduce Heating by 10%": 0.1,
        "Efficient Water Fixtures": 0.15,
        "Solar Panels Installed": 0.2,
        "Shorten Building Hours": 0.1
    }
    
    total_impact = 0
    if "Reduce Heating by 10%" in policy:
        total_impact += impact_factors["Reduce Heating by 10%"] * df["consumption"].sum()
    if "Efficient Water Fixtures" in policy:
        total_impact += impact_factors["Efficient Water Fixtures"] * water_c["consumption"].sum()
    if "Solar Panels Installed" in policy:
        total_impact += impact_factors["Solar Panels Installed"] * bld_c["consumption"].sum()
    if "Shorten Building Hours" in policy:
        total_impact += impact_factors["Shorten Building Hours"] * bld_c["consumption"].sum()

    return total_impact

impact = simulate_allocation_reduction(bld_c, policy)

st.metric("Estimated Resource Savings After Policies (kWh)", f"{impact:,.2f}")

fig = go.Figure()
fig.add_trace(go.Bar(x=["Energy", "Water", "Gas"], y=[impact * 0.5, impact * 0.2, impact * 0.3], name="Savings"))
fig.update_layout(title="Estimated Resource Savings by Category", xaxis_title="Resource Type", yaxis_title="Savings (kWh)")
st.plotly_chart(fig, use_container_width=True)

st.subheader("💵 Cost Savings Simulation")

cost_factors = {"electricity": 0.12, "gas": 0.08, "water": 0.005}  # cost per kWh/unit in USD

def simulate_cost_savings(df, impact):
    energy_cost_savings = impact * cost_factors["electricity"]
    gas_cost_savings = impact * cost_factors["gas"]
    water_cost_savings = impact * cost_factors["water"]

    total_cost_savings = energy_cost_savings + gas_cost_savings + water_cost_savings
    return total_cost_savings

cost_savings = simulate_cost_savings(bld_c, impact)

st.metric("Estimated Cost Savings (USD)", f"${cost_savings:,.2f}")

st.subheader("📊 Policy Comparison")

policy_effects = {policy: simulate_allocation_reduction(bld_c, [policy]) for policy in ["Reduce Heating by 10%", "Efficient Water Fixtures", "Solar Panels Installed", "Shorten Building Hours"]}

fig = go.Figure()
for policy, savings in policy_effects.items():
    fig.add_trace(go.Bar(x=[policy], y=[savings], name=policy))

fig.update_layout(title="Policy Impact Comparison", xaxis_title="Policy", yaxis_title="Savings (kWh)")
st.plotly_chart(fig, use_container_width=True)


