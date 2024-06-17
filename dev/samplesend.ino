#include <Arduino.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>

IRsend irsend(14);

void setup() {
  irsend.begin();
  Serial.begin(115200);
}

void loop() {
  irsend.sendNEC(0x00FFE01FUL);// diubah setelah mendapatkan kode dari recv
  delay(2000);
}