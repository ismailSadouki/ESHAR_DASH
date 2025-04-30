import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from utils import DataManager

st.set_page_config(page_title="University Utilities Consumption Dashboard", layout="wide")
st.title("🔥 Gas Consumption Analysis")


# Load Data
dm = DataManager()
df_building = dm.load_energy()
df_gas = dm.load_gas()

campuses_gas = st.sidebar.multiselect("Select Building ID(s) for Gas Data", df_gas['campus_id'].unique(), default=df_gas['campus_id'].unique())
df_gas = df_gas[df_gas['campus_id'].isin(campuses_gas)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Daily Total Gas Consumption")
    daily_gas_total = df_gas.groupby('day')['consumption'].sum()
    fig1 = px.line(daily_gas_total, x=daily_gas_total.index, y='consumption', title="Daily Total Gas Consumption")
    fig1.update_layout(xaxis_title="Date", yaxis_title="Gas Consumption")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🏢 Total Gas Consumption by Building")
    campus_gas_total = df_gas.groupby('campus_id')['consumption'].sum()
    fig2 = px.bar(campus_gas_total, x=campus_gas_total.index, y='consumption', title="Total Gas Consumption per Building")
    fig2.update_layout(xaxis_title="Campus ID", yaxis_title="Gas Consumption")
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("📆 Monthly Gas Consumption Trend")
    monthly_gas = df_gas.groupby(['month', 'campus_id'])['consumption'].sum().reset_index()
    fig3 = px.line(monthly_gas, x='month', y='consumption', color='campus_id', title="Monthly Gas Consumption per Campus")
    fig3.update_layout(xaxis_title="Month", yaxis_title="Gas Consumption")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("🕓 Hourly Gas Consumption Pattern")
    hourly_gas = df_gas.groupby(['hour'])['consumption'].mean()
    fig4 = px.line(hourly_gas, x=hourly_gas.index, y='consumption', title="Average Hourly Gas Consumption")
    fig4.update_layout(xaxis_title="Hour", yaxis_title="Gas Consumption")
    st.plotly_chart(fig4, use_container_width=True)

st.subheader("⏰ Peak vs Off-Peak Consumption Comparison")

peak_hours = list(range(6, 10)) + list(range(17, 22))

peak_data = df_gas[df_gas['hour'].isin(peak_hours)]
off_peak_data = df_gas[~df_gas['hour'].isin(peak_hours)]

daily_peak = peak_data.groupby('day')['consumption'].sum()
daily_off_peak = off_peak_data.groupby('day')['consumption'].sum()

comparison_df = pd.DataFrame({
    "Peak Consumption": daily_peak,
    "Off-Peak Consumption": daily_off_peak
}).fillna(0)

fig5 = px.line(comparison_df, x=comparison_df.index, y=["Peak Consumption", "Off-Peak Consumption"],
               labels={"value": "Consumption (Units)", "variable": "Consumption Type"},
               title="Peak vs Off-Peak Consumption Comparison")
st.plotly_chart(fig5, use_container_width=True)

peak_vs_off_peak_ratio = daily_peak.sum() / daily_off_peak.sum()
st.markdown("### Summary: Peak vs Off-Peak Consumption")
st.markdown(f"**Total Peak Consumption:** {daily_peak.sum():,.2f} units")
st.markdown(f"**Total Off-Peak Consumption:** {daily_off_peak.sum():,.2f} units")
st.markdown(f"**Peak to Off-Peak Ratio:** {peak_vs_off_peak_ratio:.2f}")


#st.markdown("<br><br><hr><p style='text-align:left;'>Developed by Ismail Sadouki ❤️</p>", unsafe_allow_html=True)
