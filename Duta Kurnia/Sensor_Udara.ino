#include <HTTPClient.h>
#include <WiFi.h>

const char* ssid = "Indi Rumah";
const char* password = "password";
const char* serverUrl = "http://192.168.1.120:5000/api/data";

const int mq135Pin = 34;

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Menghubungkan ke WiFi...");
  }
  Serial.println("Terhubung ke WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    int sensorValue = analogRead(mq135Pin);
    Serial.print("MQ-135 value: ");
    Serial.println(sensorValue);

    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String httpRequestCode = "{\"value\":" + String(sensorValue) + "}";

    int httpResponseCode = http.POST(httpRequestCode);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  }

  delay(10000);
}
