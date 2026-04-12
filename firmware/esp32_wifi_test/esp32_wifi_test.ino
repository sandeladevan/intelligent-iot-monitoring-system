#include <WiFi.h>
#include "secrets.h" //wifi credentials
#include "DHT.h"
#include <PubSubClient.h> // MQTT library

// wifi config
const char* ssid = WIFI_SSID;
const char* password = WIFI_PASSWORD;

// sensor config
#define DHTPIN 4 // GPIO connected data pin
#define DHTTYPE DHT11 //using DHT11 sensor

DHT dht(DHTPIN, DHTTYPE);

//MQTT setup
const char* mqtt_server = "192.168.1.22"; //ip

WiFiClient espClient;
PubSubClient client(espClient);

// MQTT reconnect function
void reconnect() {
  //loop until connected
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");

    //attempt to connect
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

// set up
void setup() {
  Serial.begin(115200);

 //connect wifi
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // start sensor
 dht.begin();

  // mqtt set up
 client.setServer(mqtt_server, 1883);

}

void loop() {
  //ensure mqtt connection
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  //read sensor data
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // check if reading failed
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

 // CREATE JSON PAYLOAD
  String payload = String("{\"temperature\":") + temperature + ",\"humidity\":" + humidity + "}";

  // PUBLISH TO MQTT
  client.publish("iot/sensor", payload.c_str());

  // PRINT TO SERIAL
  Serial.print("Published: ");
  Serial.println(payload);

  //wait
  delay(5000);  // DHT11 needs delay
}