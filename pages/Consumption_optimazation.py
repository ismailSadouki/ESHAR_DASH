import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
from statsmodels.tsa.arima.model import ARIMA
import warnings
from scipy.optimize import linprog
from utils import DataManager



warnings.filterwarnings("ignore")

st.set_page_config(page_title="🛢️ Gas Consumption Optimization", layout="wide")
st.title("🛢️ Gas Consumption Optimization")


# Load Data
dm = DataManager()
data = dm.load_gas()
@st.cache_data
def detect_anomalies(df, contamination=0.05):
    iso = IsolationForest(contamination=contamination, random_state=42)
    df['anomaly'] = iso.fit_predict(df[['consumption']])
    df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)
    return df

def arima_forecasting(df, order=(5, 1, 0)):
    model = ARIMA(df['consumption'], order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=48)  # Forecast next 48 hours (or any suitable time period)
    return forecast

def optimize_consumption(df, peak_hours=[17, 18, 19, 20]):
    consumption_peak = df[df['hour'].isin(peak_hours)]['consumption'].values
    consumption_off_peak = df[~df['hour'].isin(peak_hours)]['consumption'].values
    
    c = np.ones(len(consumption_peak))  # Objective function: minimize total peak consumption
    A = [np.ones(len(consumption_peak))]  # Constraint: peak consumption <= limit
    b = [500]  # Max peak consumption (arbitrary value)
    
    result = linprog(c, A_ub=A, b_ub=b, method='highs')
    optimized_peak_consumption = result.x  # Optimized consumption distribution during peak hours
    return optimized_peak_consumption


st.sidebar.header("🔧 Configuration")
optimization_method = st.sidebar.selectbox("Select Optimization Method", ["Energy Savings", "Cost Reduction", "Peak Consumption", "Smart Optimization"])
contamination = st.sidebar.slider("Anomaly Sensitivity (0 = strict)", 0.01, 0.15, 0.05, step=0.01)
arima_order = st.sidebar.slider("ARIMA Model Order (p)", 1, 10, 5)
arima_d = st.sidebar.slider("ARIMA Model Differencing (d)", 0, 3, 1)
arima_q = st.sidebar.slider("ARIMA Model Order (q)", 0, 10, 0)

data = detect_anomalies(data, contamination)

if optimization_method == "Energy Savings":

    st.subheader("🛢️ Estimated Energy Savings")
    total_consumption = data['consumption'].sum()
    anomaly_consumption = data[data['anomaly'] == 1]['consumption'].sum()
    energy_savings = total_consumption - anomaly_consumption
    st.metric("🛢️ Estimated Savings", f"{energy_savings:,.2f} m³")
    
    st.write("### Anomalies in Gas Consumption")
    st.write(f"Anomalies detected in consumption account for **{energy_savings:,.2f} m³** of gas. This is an opportunity to optimize operations by investigating and addressing these irregularities.")
    
    st.subheader("📊 Gas Consumption with Anomalies")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=data['timestamp'], y=data['consumption'], name='Gas Consumption', line=dict(color='skyblue')))
    fig1.add_trace(go.Scatter(x=data[data['anomaly'] == 1]['timestamp'], 
                              y=data[data['anomaly'] == 1]['consumption'], 
                              mode='markers', name='Anomalies', 
                              marker=dict(color='red', size=9, symbol='x')))
    fig1.update_layout(title="Gas Consumption with Detected Anomalies", xaxis_title="Timestamp", yaxis_title="Gas Consumption (m³)")
    st.plotly_chart(fig1, use_container_width=True)

elif optimization_method == "Cost Reduction":
    st.subheader("💰 Estimated Cost Reduction")
    average_cost_per_m3 = 0.06  # Example cost (change as needed, assuming cost per cubic meter of gas)
    data['estimated_cost'] = data['consumption'] * average_cost_per_m3
    total_cost = data['estimated_cost'].sum()
    anomaly_cost = data[data['anomaly'] == 1]['estimated_cost'].sum()
    cost_savings = total_cost - anomaly_cost
    st.metric("💰 Estimated Savings", f"${cost_savings:,.2f}")
    
    st.write("### Cost Implications of Anomalies")
    st.write(f"By addressing anomalies, an estimated **${cost_savings:,.2f}** can be saved annually. Focus on areas with high anomaly rates for the most cost-effective adjustments.")
    
    st.subheader("📊 Cost Breakdown")
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=['Total Cost', 'Anomaly Cost', 'Savings'], 
                         y=[total_cost, anomaly_cost, cost_savings], 
                         marker_color=['blue', 'red', 'green']))
    fig2.update_layout(title="Cost Reduction Breakdown", xaxis_title="Category", yaxis_title="Cost ($)")
    st.plotly_chart(fig2, use_container_width=True)

elif optimization_method == "Peak Consumption":
    st.subheader("⏰ Peak Consumption Analysis")
    peak_consumption = data.groupby('hour')['consumption'].mean().sort_values(ascending=False).head(5)
    st.write("Top 5 Peak Consumption Hours:")
    st.write(peak_consumption)

    st.write(f"Peak consumption is highest during **{', '.join(map(str, peak_consumption.index))}** hours. Adjusting usage during these hours can significantly reduce costs and improve energy efficiency.")
    
    st.subheader("📊 Peak Consumption Visualization")
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(x=peak_consumption.index, y=peak_consumption.values, 
                         marker=dict(color='orange')))
    fig3.update_layout(title="Peak Hour Gas Consumption", xaxis_title="Hour", yaxis_title="Average Consumption (m³)")
    st.plotly_chart(fig3, use_container_width=True)

elif optimization_method == "Smart Optimization":
    st.subheader("🔧 Smart Optimization (Peak Consumption Minimization)")
    optimized_peak_consumption = optimize_consumption(data)
    st.write("Optimized Peak Consumption Distribution:")
    st.write(optimized_peak_consumption)

    st.write(f"By distributing consumption more evenly across non-peak hours, peak consumption can be reduced by **{np.sum(optimized_peak_consumption):.2f} m³**. This approach minimizes energy costs while still meeting needs.")
    
    st.subheader("📊 Optimized Peak Consumption Visualization")
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=data[data['hour'].isin([17, 18, 19, 20])]['timestamp'], 
                             y=optimized_peak_consumption, 
                             mode='lines', name='Optimized Consumption', 
                             line=dict(color='green')))
    fig4.update_layout(title="Optimized Gas Consumption During Peak Hours", xaxis_title="Timestamp", yaxis_title="Gas Consumption (m³)")
    st.plotly_chart(fig4, use_container_width=True)

st.subheader("📊 Forecasted Gas Consumption with ARIMA")
forecast = arima_forecasting(data, order=(arima_order, arima_d, arima_q))
fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=np.arange(len(forecast)), y=forecast, name='Forecasted Consumption', line=dict(color='blue')))
fig5.update_layout(title="Gas Consumption Forecast with ARIMA", xaxis_title="Time", yaxis_title="Gas Consumption (m³)")
st.plotly_chart(fig5, use_container_width=True)

# Footer Section

#st.markdown("<br><br><hr><p style='text-align:left;'>Developed by Ismail Sadouki ❤️</p>", unsafe_allow_html=True)

