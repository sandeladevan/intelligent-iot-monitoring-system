import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="IoT Dashboard", layout="wide")

st.title(" IoT Monitoring Dashboard")

# Auto-refresh
placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("data.csv", names=["timestamp", "temperature", "humidity"])

        with placeholder.container():
            st.subheader("Live Sensor Data")

            st.line_chart(df[["temperature", "humidity"]])

            st.dataframe(df.tail(10))

    except Exception as e:
        st.error(f"Error: {e}")

    time.sleep(2)