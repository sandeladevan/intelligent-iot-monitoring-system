import streamlit as st
import pandas as pd
import psycopg2
import time

st.set_page_config(page_title="IoT Dashboard", layout="wide")

st.title(" IoT Monitoring Dashboard")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="iot_db",
    user="postgres",
    password="1234"
)

# Auto-refresh
placeholder = st.empty()

while True:
    try:
        # Read data from PostgreSQL
        query = "SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 50;"
        df = pd.read_sql(query, conn)

        # Reverse order for proper plotting
        df = df.sort_values(by="timestamp")

        with placeholder.container():
            st.subheader("Live Sensor Data")
            
            # Show latest values
            if not df.empty:
                latest = df.iloc[-1]
                st.metric("Temperature (°C)", round(latest["temperature"], 2))
                st.metric("Humidity (%)", round(latest["humidity"], 2))
                
            # graph
            st.line_chart(df[["temperature", "humidity"]])
            
            #table
            st.dataframe(df.tail(10))

    except Exception as e:
        st.error(f"Error: {e}")

    time.sleep(2)