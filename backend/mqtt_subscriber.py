import paho.mqtt.client as mqtt
import json
from datetime import datetime

# MQTT config
BROKER = "192.168.1.22"   # your laptop IP
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

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        with open("data.csv", "a") as f:
            f.write(f"{timestamp},{temperature},{humidity}\n")

    except Exception as e:
        print("Error:", e)

# Setup client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Run loop
client.loop_forever()