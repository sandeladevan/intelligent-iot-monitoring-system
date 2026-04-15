import paho.mqtt.client as mqtt
import json
from datetime import datetime
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="iot_db",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()

# MQTT config
BROKER = "192.168.1.22"   # laptop IP
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