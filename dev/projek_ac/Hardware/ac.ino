#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>
#include <DHT.h>

const char* ssid = "Grayhouse";
const char* password = "pinturumah";
const char* getAPIPerson = "http://192.168.1.10:5000/person ";
const char* getAPIData = "http://192.168.1.10:5000/temp";// data dari data base
const char* postAPITemp = "http://192.168.1.10:5000/temperature";
const char* postAPIVer = "http://192.168.1.10:5000/information";
String verifiction = "";

HTTPClient http;
DHT dht(33, DHT11);
IRsend irsend(4);

void setupWifi(){
  delay(10);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
}

void setup(){
  Serial.begin(115200);
  irsend.begin();
  dht.begin();
  setupWifi();
}

void get(){
  http.begin(getAPIPerson);
  http.GET();
  String person = http.getString();
  http.end();
  http.begin(getAPIData);
  http.GET();
  String data = http.getString();
  http.end();
  if(person != "0"){
    //menunggu kode ir
    irsend.sendRaw(rawData, 73, 38);
    verifiction = "";// dipindah di post
  } else {
    irsend.sendRaw(rawData, 73, 38);
    //menunggu kode ir
    verifiction = "";// dipindah di post
  }
}

void post(){
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  http.begin(postAPITemp);
  http.addHeader("Content-Type", "application/json");
  String postTemp = "{\"temp\":\"" + String(t) + "\", \"hum\":\"" + String(h) + "\"}";
  http.POST(postTemp);
  http.end();

  http.begin(postAPIVer);
  http.addHeader("Content-Type", "application/json");
  String postVer = "{\"info\": \"" + verifiction + "\"}";
  http.POST(postVer);
  http.end();
}
void loop(){
  // if(WiFi.status() != WL_CONNECTED){
  //   setupWifi();
  // }
  get();
  delay(100000);
  post();
}