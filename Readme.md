# 🏢 AI-Powered Sustainability Dashboard

> Developed under the supervision of **Prof. H. Beldjillali**  
> ENSSEA – École Nationale Supérieure de Statistique et d'Économie Appliquée

A **modular, AI-enhanced Streamlit dashboard** for tracking, analyzing, and optimizing sustainability metrics across smart buildings.

It integrates **energy, gas, and water consumption data** and leverages **machine learning, anomaly detection, and policy simulation** to help organizations:

- 💧🔌🔥 Reduce resource consumption  
- 🔍 Detect inefficiencies and anomalies  
- 📊 Simulate sustainability policies  
- 📈 Forecast demand and environmental impact  

---

## 📚 Table of Contents

- [🧩 Key Modules](#-key-modules)  
- [📁 Data](#-data)  
- [📊 Consumption Forecast](#-consumption-forecast)  
- [🛢️ Gas Consumption Optimization](#️-gas-consumption-optimization)  
- [🔌 Energy Consumption](#-energy-consumption)  
- [🔥 Gas Consumption](#-gas-consumption)  
- [💧 Water Consumption](#-water-consumption)  
- [🌍 Sustainability Impact](#-sustainability-impact)  
- [🔍 Anomaly Detection](#-anomaly-detection)  
- [🚀 Quick Start](#-quick-start)  
- [🐳 Docker Support](#-docker-support)  
- [📌 Folder Structure](#-folder-structure)  
- [📸 Screenshots](#-screenshots)  
- [🧠 Credits](#-credits)  
- [📄 License](#-license)

---

## 🧩 Key Modules

Each page in this dashboard focuses on a specific task:

1. **📉 Consumption Forecast** – Predict future usage  
2. **🔧 Consumption Optimization** – Improve resource efficiency  
3. **⚠️ Anomaly Detection** – Flag abnormal consumption  
4. **📜 Policy Simulation** – Test custom policy scenarios  
5. **🌍 Sustainability Impact** – Measure emissions and benchmarks  
6. **🔌 Energy**, **🔥 Gas**, and **💧 Water** – Explore utility usage in depth

> Built for **clarity**, **interactivity**, and **actionable insights**.

---

## 📁 Data

Supports `.csv`, `.parquet`, and `.zip` datasets:

- `building_consumption.*`  
- `gas_consumption.*`  
- `water_consumption.*`  

Users can also upload their own datasets for real-time analysis.

---

## 📊 Consumption Forecast

Forecast utility usage with ML:

- 🔮 **SARIMAX, ARIMA, Linear Regression, Exponential Smoothing**  
- 🚨 **Anomaly Detection** with dynamic thresholds  
- 🎛️ Sidebar model selector and parameters

---

## 🛢️ Gas Consumption Optimization

Optimize gas consumption via:

- 💡 **Energy Savings** – Isolation Forest anomaly reduction  
- 💰 **Cost Reduction** – Estimate financial impact  
- ⏰ **Peak Consumption** – Identify and reduce spikes  
- 🧠 **Smart Optimization** – Linear programming for load balancing  
- 📈 Includes ARIMA forecasting & interactive controls

---

## 🔌 Energy Consumption

Visualize electricity usage:

- 🔮 Forecast (Next 30 Days)  
- 📊 Daily, Monthly, Hourly analysis by building  
- 📅 Last 7-day summary

---

## 🔥 Gas Consumption

Explore gas consumption patterns:

- 📈 Daily totals  
- 🏢 Building-level breakdown  
- 📆 Monthly trends  
- 🕓 Hourly usage  
- ⏰ Peak vs Off-Peak comparison

---

## 💧 Water Consumption

Monitor and analyze water usage:

- 📈 Daily trends  
- ⏰ Peak/Off-peak usage  
- 🕒 Hourly and weekly breakdown  
- 🚨 High usage detection

---

## 🌍 Sustainability Impact

Simulate and visualize environmental policies:

- 📊 Building benchmarking (Efficiency Score)  
- 🌿 Real vs simulated CO₂ emissions  
- ⚙️ Policy controls (Heating, Solar, Water, Hours)  
- 🎲 Monte Carlo Simulation (Years, Variability, CO₂ Factors)

---

## 🔍 Anomaly Detection

Utility-specific anomaly detectors:

- ⚡ **Energy** – Z-score spikes  
- 🔥 **Gas** – Rolling average deviation  
- 💧 **Water** – Off-peak surges  
- 🧾 Summary tables and visual alerts

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/sustainability-dashboard.git
cd sustainability-dashboard

# 2. (Optional) Create a virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run Home.py

