import paho.mqtt.client as mqtt
import json
from datetime import datetime
import psycopg2
import time

# Connect to PostgreSQL
def connect_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database="iot_data",
                user="postgres",
                password="1234"
            )
            print("Connected to DB")
            return conn
        except Exception as e:
            print("DB not ready, retrying...")
            time.sleep(3)

conn = connect_db()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT
)
""")
conn.commit()

# MQTT config
BROKER = "mqtt"   # laptop IP
PORT = 1883
TOPIC = "iot/sensor"

# Callback when connected
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    client.subscribe(TOPIC)

# Callback when message received
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Received: {payload}")

    try:
        data = json.loads(payload)
        temperature = data.get("temperature")
        humidity = data.get("humidity")

        # Defined normal ranges
        TEMP_MIN = 18
        TEMP_MAX = 30
        HUM_MIN = 30
        HUM_MAX = 80

        # Checks anomalies
        if temperature is not None and humidity is not None:
            if temperature < TEMP_MIN or temperature > TEMP_MAX:
                print(f" ALERT: Temperature anomaly detected: {temperature} °C")

            if humidity < HUM_MIN or humidity > HUM_MAX:
                print(f" ALERT: Humidity anomaly detected: {humidity} %")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        
        cursor.execute(
            "INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)",
            (temperature, humidity)
        )
        conn.commit()

    except Exception as e:
        print("Error:", e)

# Setup client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Run loop
client.loop_forever()