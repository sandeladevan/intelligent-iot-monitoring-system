# intelligent-iot-monitoring-system

## Overview
This project is a real-time IoT monitoring system using ESP32, DHT11 sensor, and MQTT protocol.

It collects environmental data (temperature & humidity) and transmits it over a network using MQTT.

## features
- ESP32 WiFi connectivity
- Secure credential handling using `secrets.h`
- Real-time temperature & humidity monitoring
- MQTT-based communication
- JSON data publishing
- Modular and scalable architecture

## system architecture
ESP32 + DHT11 → WiFi → MQTT Broker (Mosquitto) → Subscriber

## Hardware Used
- ESP32 Dev Module
- DHT11 Temperature & Humidity Sensor
- Breadboard & Jumper Wires

## Software Used
- Arduino IDE
- MQTT (Mosquitto Broker)
- PubSubClient Library
- DHT Sensor Library

## MQTT Configuration
- Broker: Local Mosquitto
- Port: 1883
- Topic: `iot/sensor`

## Sample Data

```json
{"temp":19.5,"hum":64}
```
## Security
- WiFi credentials stored in secrets.h
- secrets.h excluded using .gitignore

## Progress
- WiFi connection established
- Sensor data acquisition (DHT11)
- MQTT local broker setup
- ESP32 publishing data via MQTT

## Next Steps
- Backend (Python MQTT subscriber)
- Data storage (database)
- Dashboard (visualization)
- AI integration