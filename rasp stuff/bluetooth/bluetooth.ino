#include <SoftwareSerial.h>

SoftwareSerial bluetooth(2, 3);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  bluetooth.begin(9600);
  Serial.println("started");

}

void loop() {
  // put your main code here, to run repeatedly:
  if (bluetooth.available()>0){
    //Serial.println("got");
    char c = bluetooth.read();
    Serial.println(c);
    bluetooth.print("got");
    bluetooth.println();
  }
  //Serial.println("vittu");
}
