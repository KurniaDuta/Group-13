#include <IRremoteESP8266.h>
#include <IRrecv.h>


IRrecv irrecv(14);
decode_results results;

void setup() {
  irrecv.enableIRIn();
  Serial.begin(115200);
  
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    delay(4000);
    irrecv.resume();
  }
}