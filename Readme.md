# 🏢 AI-Powered Sustainability Dashboard

> Developed under the supervision of **Professor H. Beldjillali**  
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

---

## 📁 Data

Supports `.csv`, `.parquet`, and `.zip` datasets:

- `building_consumption.*`  
- `gas_consumption.*`  
- `water_consumption.*`  

> **First**, unzip all the `.zip` files in your project directory:

```bash
unzip '*.zip'
```

---

## 📊 Consumption Forecast

Forecast utility usage with ML:

- 🔮 **SARIMAX, ARIMA, Linear Regression, Exponential Smoothing**  
- 🚨 **Anomaly Detection** with dynamic thresholds  
- 🎛️ Sidebar model selector and parameters

---

## 🛢️ Gas Consumption Optimization

Optimize gas consumption via:

- 💡 **Energy Savings**  
- 💰 **Cost Reduction**  
- ⏰ **Peak Consumption**  
- 🧠 **Smart Optimization** (linear programming)  
- 📈 Forecasting + interactive controls

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

If you prefer **not to use Docker**, follow these steps:

### ✅ Create virtual environment

```bash
python3 -m venv env
```

### ✅ Activate the environment (Linux/macOS)

```bash
source env/bin/activate
```

### ✅ If on Windows, run this instead:

```bash
.\env\Scripts\activate
```

### ✅ Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Run the Streamlit app

```bash
streamlit run Home.py
```

---

## 🐳 Docker Support

If you prefer Docker:

### 📦 Prerequisites

- Docker installed and running  
- *(Optional)* Docker Compose installed

### 🏗️ Build the Docker image:

```bash
docker build -t streamlit-app .
```

### ▶️ Run the Docker container:

```bash
docker run -p 8501:8501 streamlit-app
```

Open your browser and go to:  
👉 [http://localhost:8501](http://localhost:8501)

---

### 🧩 (Optional) Run with Docker Compose

#### ▶️ Start the app:

```bash
docker-compose up --build
```

#### ⏹️ Stop the app:

```bash
docker-compose down
```

---

## 📌 Folder Structure

```bash
├── Home.py
├── pages/
│   ├── Consumption_Forcast.py
│   ├── Consumption_optimazation.py
│   ├── Anomalies_Detection.py
│   ├── Policy_simulation.py
│   ├── Sustainability_Impact.py
│   ├── energy_consumption.py
│   ├── gas_consumption.py
│   └── water_consumption.py
├── utils.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── *.csv / *.parquet / *.zip
└── README.md
```

---

## 📸 Screenshots

> *(Optional: add `/assets/` images here)*  
Examples:  
- Forecast graph  
- CO₂ simulation  
- Peak consumption heatmap  

---

## 🧠 Credits

- Built by **Ismail Sadouki**  
- Supervised by **Professor H. Beldjillali**  
- ENSSEA – Higher National School of Statistics

---

## 📄 License

This repository is licensed under the  
**Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**

🔒 **You may not use this code for commercial purposes.**  
📘 [Read the full license](https://creativecommons.org/licenses/by-nc/4.0/)

> ESHRA DASHBOARD © 2025 by Ismail Sadouki is licensed under CC BY-NC 4.0

