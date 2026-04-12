#include <WiFi.h>
#include "secrets.h"
#include "DHT.h"

// wifi config
const char* ssid = WIFI_SSID;
const char* password = WIFI_PASSWORD;

// sensor config
#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);

// start sensor
dht.begin();

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
}

void loop() {
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  // check if reading failed
  if (isnan(temp) || isnan(hum)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.print(" °C | Humidity: ");
  Serial.println(hum);

  delay(2000);  // DHT11 needs delay
}