#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "DHT.h"

#define DHT11PIN 33

const char* ssid = "Rizka";
const char* password = "pojok123";
DHT dht(DHT11PIN, DHT11);
WiFiClient client;
HTTPClient http;
const char* serverName = "http://192.168.4.17:5000/sendf";

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password); 

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  dht.begin();
}

void loop() {
  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  String post = "{\"temp\":\"" + String(t) + "\", \"hum\":\"" + String(h) + "\"}";
  int httpResponseCode = http.POST(post);
  http.end();
  delay(10000);
}

