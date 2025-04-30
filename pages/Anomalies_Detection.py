import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

from utils import DataManager

st.set_page_config(page_title="Anomaly Detection", layout="wide")
st.title("🔍 Anomaly Detection")

# Load Data
dm = DataManager()
df_energy = dm.load_energy()
df_gas = dm.load_gas()
df_water = dm.load_water()




summary = df_energy.groupby('timestamp')['consumption'].sum().reset_index()
summary['rolling_mean'] = summary['consumption'].rolling(10).mean()
summary['z_score'] = (summary['consumption'] - summary['rolling_mean']) / summary['consumption'].std()

anomalies = summary[np.abs(summary['z_score']) > 2]

fig = px.line(summary, x='timestamp', y='consumption', title='Building Consumption Over Time',
              labels={'timestamp': 'Date', 'consumption': 'Consumption'})

fig.add_scatter(x=anomalies['timestamp'], y=anomalies['consumption'],
                mode='markers', name='Anomalies',
                marker=dict(color='red', size=8, symbol='x'))

st.plotly_chart(fig, use_container_width=True)

st.subheader("📋 Detected Anomalies")
st.dataframe(anomalies[['timestamp', 'consumption', 'z_score']], use_container_width=True)





st.markdown("---")
st.subheader("🚨Gas Abnormal Consumption Detection")




rolling_window = 7
threshold_factor = 1.5

df_gas['rolling_avg'] = df_gas['consumption'].rolling(window=rolling_window).mean()
df_gas['abnormal'] = df_gas['consumption'] > (df_gas['rolling_avg'] * threshold_factor)
abnormal_instances = df_gas[df_gas['abnormal']]

if not abnormal_instances.empty:
    st.warning(
        f"⚠️ Abnormal gas consumption detected! **{len(abnormal_instances)}** instances where consumption exceeded **{threshold_factor}×** the 7-day rolling average."
    )

    # Side-by-side layout
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("#### 📋 Abnormal Consumption Table")
        st.dataframe(
            abnormal_instances[['timestamp', 'campus_id', 'consumption', 'rolling_avg']],
            use_container_width=True
        )

    with col2:
        fig = px.scatter(
            abnormal_instances,
            x='timestamp',
            y='consumption',
            color='campus_id',
            title='Abnormal Gas Consumption Instances',
            labels={'consumption': 'Gas Consumption (Units)', 'timestamp': 'Date'}
        )
        st.plotly_chart(fig, use_container_width=True)

else:
    st.success("✅ No abnormal gas consumption detected.")










st.markdown("---")









st.subheader("💧 Abnormal Water Consumption")

rolling_avg = df_water["consumption"].rolling(window=7).mean()
abnormal_threshold = 1.5
abnormal = df_water[df_water["consumption"] > abnormal_threshold * rolling_avg]

if not abnormal.empty:
    st.warning(
        f"🚱 Abnormal water consumption detected! **{len(abnormal)}** instances where consumption exceeded **{abnormal_threshold}×** the 7-day rolling average."
    )

    # Display table and chart side by side
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("#### 📋 Abnormal Consumption Instances")
        st.dataframe(
            abnormal[["campus_id", "timestamp", "consumption"]].reset_index(drop=True),
            use_container_width=True
        )

    with col2:
        fig_abnormal = px.scatter(
            abnormal,
            x="timestamp",
            y="consumption",
            color="campus_id",
            title="Abnormal Water Consumption Over Time",
            labels={"timestamp": "Time", "consumption": "Units"}
        )
        st.plotly_chart(fig_abnormal, use_container_width=True)

else:
    st.success("✅ No abnormal water consumption detected.")


st.markdown("##### 💡 Off-Peak Hour Alerts")

off_peak_hours = list(range(0, 7))  # Midnight to 6 AM
off_peak_data = df_water[df_water["hour"].isin(off_peak_hours)]
threshold = df_water["consumption"].quantile(0.75)
high_off_peak = off_peak_data[off_peak_data["consumption"] > threshold]

if not high_off_peak.empty:
    st.warning(f"🚱 **{len(high_off_peak)} instances** of high usage during off-peak hours.")

    alert_summary = high_off_peak.groupby("hour")["consumption"].mean().reset_index()

    col3, col4 = st.columns([1, 1.5])

    with col3:
        st.markdown("#### 🧾 Table of Concern")
        st.dataframe(alert_summary.rename(columns={"hour": "Hour", "consumption": "Avg High Usage (Units)"}))

    with col4:
        fig_alert = px.bar(
            alert_summary,
            x="hour",
            y="consumption",
            color="consumption",
            color_continuous_scale="teal",
            title="High Usage During Off-Peak",
            labels={"hour": "Hour", "consumption": "Avg Usage"},
        )
        st.plotly_chart(fig_alert, use_container_width=True)

    st.markdown("##### Recommendations for water optimasation")
    for _, row in alert_summary.iterrows():
        st.markdown(
            f"- 🔍 Check water systems around **{int(row['hour'])}:00** — avg usage `{row['consumption']:.1f}` units. Possible leak or inefficiency."
        )
else:
    st.success("🎉 No unusual off-peak water usage found. You're efficient!")


#st.markdown("<br><br><hr><p style='text-align:left;'>Developed by Ismail Sadouki ❤️</p>", unsafe_allow_html=True)
