import streamlit as st
import pandas as pd
import psycopg2
import time
import requests

st.set_page_config(page_title="IoT Dashboard", layout="wide")

st.title(" IoT Monitoring Dashboard")

# Auto-refresh
placeholder = st.empty()
  
st.subheader("Live Sensor Data")

# API URL
API_URL = "http://127.0.0.1:8000/data"

# Fetch data from API
response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["timestamp"] = df["timestamp"].dt.tz_localize("UTC").dt.tz_convert("Europe/Dublin")
    # Show latest values
    latest = df.iloc[0]

    st.metric("Temperature (°C)", latest["temperature"])
    st.metric("Humidity (%)", latest["humidity"])

    # Plot graph
    st.line_chart(df.set_index("timestamp")[["temperature", "humidity"]])

    # Show table
    st.dataframe(df)

else:
    st.error("Failed to fetch data from API")