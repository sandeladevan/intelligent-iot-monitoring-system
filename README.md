# Intelligent-IoT-Monitoring-System

## Overview
This project is a real-time IoT monitoring system using:
- ESP32, DHT11 sensor (data collection)
- MQTT protocol (communication)
- Python backend (processing)
- PostgreSQL (storage)
- FastAPI (REST API)
- Streamlit (visualization)

It captures temperature & humidity data, processes it, detects anomalies, stores it in a database, exposes it via APIs and visualizes it in real-time.


## Dashboard Preview: Real-time visualization of temperature and humidity data:
<p>
  <img src="assets/dashboard1.png" width="400" height="250" style="margin-right:10px;" />
  <img src="assets/dashboard3.png" width="400" height="250" />
</p>

## FastAPI Response (Live Data API)
#### API Endpoint Output (/data)
 <img src="assets/FastAPI1.png" width="400" height="250" />

## Database Preview (PostgreSQL)
<img src="assets/postgresql.png" width="400" height="250" />

## Anomaly Detection Output

Real-time anomaly detection using backend logic:

<img src="assets/anomaly_output.png" width="400" height="250"/>

---
## Features
- ESP32 WiFi connectivity
- Secure credential handling using `secrets.h`
- Real-time temperature & humidity monitoring
- MQTT-based communication (publish/subscribe)
- Python backend for data ingestion
- PostgreSQL database integration
- REST API using FastAPI
- Live dashboard using Streamlit
- Real-time anomaly detection (AI logic)
- JSON data pipeline
- Modular and scalable architecture

---

## System Architecture
```
DHT11 Sensor
↓
ESP32 (Firmware)
↓ WiFi
MQTT Broker (Mosquitto)
↓
Python Backend (Subscriber)
↓
PostgreSQL Database
↓
FastAPI (REST API)
↓
Streamlit Dashboard (Live Visualization)
```

## Hardware Used
- ESP32 Dev Module
- DHT11 Temperature & Humidity Sensor
- Breadboard & Jumper Wires

## Software Used
- Arduino IDE
- Python 3
- MQTT (Mosquitto Broker)
- PubSubClient Library (ESP32)
- DHT Sensor Library
- paho-mqtt (Python)
- PostgreSQL
- FastAPI
- psycopg2
- Streamlit (Dashboard)
- Pandas (Data processing)
- Git & GitHub


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
- Prevents exposure of sensitive data on GitHub

## AI / Smart Logic

 The system includes real-time anomaly detection:
  - Detects abnormal temperature/humidity values
  - Generates alerts when values exceed normal range

## Testing Approach

Anomaly detection was validated using controlled testing:
- External heat sources (e.g., lighter) were used to simulate high temperature conditions
- Environmental variations were introduced to test humidity thresholds
- This ensured the system correctly detects and flags abnormal readings in real-time

Example output:
```
ALERT: Temperature anomaly detected: 45.8 °C  
ALERT: Humidity anomaly detected: 99.0 %
```

## Progress
- WiFi connection established (ESP32)
- Sensor data acquisition (DHT11)
- MQTT local broker setup (Mosquitto)
- ESP32 publishing data via MQTT
- Python backend subscriber implemented
- Data stored in PostgreSQL
- FastAPI backend developed
- REST APIs for IoT data (/data, /latest)
- Real-time dashboard using Streamlit
- Anomaly detection implemented and tested

## How to Run
### 1. Clone Repository

```
git clone https://github.com/sandeladevan/intelligent-iot-monitoring-system.git
cd intelligent-iot-monitoring-system
```
### 2. Install Requirements (Python Backend)

```
pip install paho-mqtt streamlit pandas psycopg2-binary
```

### 3. Install MQTT Broker (Mosquitto)

Download and install:

```
https://mosquitto.org/download/
```

### 4. Start MQTT Broker
 
```
mosquitto -v
```
### 5. Setup PostgreSQL
- Create database:
```
CREATE DATABASE iot_db;
```
- create table:
```
CREATE TABLE sensor_data (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, temperature FLOAT, humidity FLOAT);

insert into sensor_data (temperature, humidity) values (25.5, 60.0);

SELECT * FROM sensor_data;

```
### 6. Run Backend Subscriber

```
cd backend
python mqtt_subscriber.py
```

### 7. Run FastAPI Server
```
uvicorn api:app --reload
```
Open:
```
http://127.0.0.1:8000/docs
```

### 7. Run Dashboard
```
streamlit run dashboard.py
```
Open in browser:
```
http://localhost:8501
```

### 8. Setup ESP32 Firmware
- Open Arduino IDE
- Install libraries: DHT sensor library (Adafruit), PubSubClient (Nick O’Leary)
- Update: WiFi credentials in secrets.h, MQTT server IP (laptop IP)

### 9. Upload Code to ESP32
- Select board: ESP32 Dev Module
- Upload code
- Open Serial Monitor (115200 baud)

### 10. Output
- Live sensor data streaming
- Real-time dashboard updates
- Data stored in PostgreSQL
- API endpoints serving data
- Alerts triggered on anomalies

## Key Learnings
- IoT system design (end-to-end pipeline)
- MQTT protocol (publish/subscribe model)
- Embedded systems (ESP32 + sensors)
- Backend development (Python subscriber)
- Database integration (PostgreSQL)
- Backend API development (FastAPI)
- Real-time visualization with streamlit
- Debugging networking & system issues
- AI-based anomaly detection
- Handling production-style architecture

## Next Steps
- Dockerize entire system
- Deploy to cloud

### Author
Devan Sandela