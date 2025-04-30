import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings
from utils import DataManager

warnings.filterwarnings("ignore")

st.set_page_config(page_title="🔮 Forecast Energy Consumption", layout="wide")
st.title("📈 Forecast Energy Consumption")

# Load Data
dm = DataManager()
df_energy = dm.load_energy()
data = df_energy.groupby('day')['consumption'].sum().reset_index()
data.columns = ['date', 'consumption']
data.set_index('date', inplace=True)

st.sidebar.header("🔧 Configuration")
model_choice = st.sidebar.selectbox("Choose Forecasting Model", ["SARIMAX", "Holt-Winters"])
horizon = st.sidebar.slider("Forecast Days", 7, 90, 30)
contamination = st.sidebar.slider("Anomaly Sensitivity (0 = strict)", 0.01, 0.15, 0.05, step=0.01)

iso = IsolationForest(contamination=contamination, random_state=42)
data['anomaly'] = iso.fit_predict(data[['consumption']])
data['anomaly'] = data['anomaly'].apply(lambda x: 1 if x == -1 else 0)

train = data.iloc[:-horizon]
test = data.iloc[-horizon:]

# Caching model training
@st.cache_resource
def train_sarimax_model(train_data):
    model = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
    return model.fit(disp=False)

@st.cache_resource
def train_holt_winters_model(train_data):
    model = ExponentialSmoothing(train_data, trend="add", seasonal="add", seasonal_periods=7)
    return model.fit()

if model_choice == "SARIMAX":
    results = train_sarimax_model(train['consumption'])
    forecast_obj = results.get_forecast(steps=horizon)
    forecast = forecast_obj.predicted_mean
    conf_int = forecast_obj.conf_int()
    forecast.index = test.index
    conf_int.index = test.index
else:
    results = train_holt_winters_model(train['consumption'])
    forecast = results.forecast(horizon)
    forecast.index = test.index
    conf_int = pd.DataFrame({
        'lower consumption': forecast * 0.95,
        'upper consumption': forecast * 1.05
    }, index=test.index)

st.subheader(f"📊 Forecast Using {model_choice}")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=train.index, y=train['consumption'], name='Train', line=dict(color='royalblue')))
fig1.add_trace(go.Scatter(x=test.index, y=test['consumption'], name='Test (Actual)', line=dict(color='green')))
fig1.add_trace(go.Scatter(x=forecast.index, y=forecast, name='Forecast', line=dict(color='orange', dash='dash')))
fig1.add_trace(go.Scatter(x=conf_int.index, y=conf_int.iloc[:, 0], name='Lower Bound', line=dict(color='orange', width=0.5), showlegend=False))
fig1.add_trace(go.Scatter(x=conf_int.index, y=conf_int.iloc[:, 1], fill='tonexty', mode='lines', name='Confidence Interval', line=dict(color='orange', width=0.5), showlegend=False))
fig1.update_layout(title='Forecast vs Actual', xaxis_title='Date', yaxis_title='Consumption', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
st.plotly_chart(fig1, use_container_width=True)

mae = mean_absolute_error(test['consumption'], forecast)
rmse = np.sqrt(mean_squared_error(test['consumption'], forecast))
col1, col2, col3 = st.columns(3)
col1.metric("📉 MAE", f"{mae:.2f}")
col2.metric("📈 RMSE", f"{rmse:.2f}")
col3.metric("📌 Anomaly Ratio", f"{(data['anomaly'].mean() * 100):.2f}%")

st.subheader("🚨 Anomaly Detection")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data.index, y=data['consumption'], name='Consumption', line=dict(color='skyblue')))
fig2.add_trace(go.Scatter(x=data[data['anomaly'] == 1].index, y=data[data['anomaly'] == 1]['consumption'], mode='markers', name='Anomalies', marker=dict(color='red', size=9, symbol='x')))
fig2.update_layout(title="Detected Anomalies", xaxis_title="Date", yaxis_title="Consumption")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📤 Export Anomalies")
anomalies = data[data['anomaly'] == 1].copy()
anomalies.reset_index(inplace=True)
st.dataframe(anomalies[['date', 'consumption']])
csv = anomalies.to_csv(index=False).encode('utf-8')
st.download_button(label="Download Anomalies CSV", data=csv, file_name="anomalies.csv", mime='text/csv')

st.subheader("🧩 Trend & Seasonality Decomposition")
decomp = seasonal_decompose(data['consumption'], model='additive', period=7)
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=decomp.trend.index, y=decomp.trend, name='Trend', line=dict(color='blue')))
fig3.add_trace(go.Scatter(x=decomp.seasonal.index, y=decomp.seasonal, name='Seasonal', line=dict(color='orange')))
fig3.add_trace(go.Scatter(x=decomp.resid.index, y=decomp.resid, name='Residuals', line=dict(color='gray')))
fig3.update_layout(title='Time Series Decomposition', xaxis_title='Date', yaxis_title='Value')
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
# st.markdown("<br><br><hr><p style='text-align:left;'>Developed by Ismail Sadouki ❤️</p>", unsafe_allow_html=True)

