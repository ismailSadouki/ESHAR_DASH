import pandas as pd
import streamlit as st




class DataManager:

    @st.cache_data
    def load_gas(_self):
        if "gas_data" not in st.session_state:

            df_gas = pd.read_parquet("gas_consumption.parquet")
            df_gas['timestamp'] = pd.to_datetime(df_gas['timestamp'])
            df_gas['year'] = df_gas['timestamp'].dt.year
            df_gas['month'] = df_gas['timestamp'].dt.to_period("M").dt.to_timestamp()
            df_gas['hour'] = df_gas['timestamp'].dt.hour
            df_gas['day'] = df_gas['timestamp'].dt.date
            df_gas['weekday'] = df_gas['timestamp'].dt.day_name()
            df_gas['utility_type'] = 'gas'


            st.session_state["gas_data"] = df_gas
        return st.session_state["gas_data"]
    
    def load_energy(_self):
        if "energy_data" not in st.session_state:
            df =  pd.read_parquet("building_consumption.parquet")
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['year'] = df['timestamp'].dt.year
            df['month'] = df['timestamp'].dt.to_period("M").dt.to_timestamp()
            df['hour'] = df['timestamp'].dt.hour
            df['day'] = df['timestamp'].dt.date
            df['weekday'] = df['timestamp'].dt.day_name()
            df['utility_type'] = 'electricity'
            st.session_state["energy_data"] = df
        return st.session_state["energy_data"]

    
    @st.cache_data
    def load_water(_self):
        if "water_data" not in st.session_state:

            df = pd.read_parquet("water_consumption.parquet")
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['year'] = df['timestamp'].dt.year
            df['month'] = df['timestamp'].dt.to_period("M").dt.to_timestamp()
            df['hour'] = df['timestamp'].dt.hour
            df['day'] = df['timestamp'].dt.date
            df['weekday'] = df['timestamp'].dt.day_name()

            st.session_state["water_data"] = df
        return st.session_state["water_data"]



#df = pd.read_csv("building_consumption.csv", parse_dates=["timestamp"])

#df.to_feather("building_consumption.feather")  # Save once

#df_water = pd.read_csv("water_consumption.csv", parse_dates=["timestamp"])
#df_gas = pd.read_csv("gas_consumption.csv", parse_dates=["timestamp"])

#df.to_parquet("building_consumption.parquet", compression="snappy")
#df_water.to_parquet("water_consumption.parquet", compression="snappy")
#df_gas.to_parquet("gas_consumption.parquet", compression="snappy")

