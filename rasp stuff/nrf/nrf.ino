#include <SPI.h>
#include <RF24.h>

RF24 radio(A3, A0);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  const uint64_t pipe = 0xE0E0F1F1E0LL;
  radio.openReadingPipe(1, pipe);
  radio.powerUp(); 
  delay(200);
}

void loop() {
  radio.startListening();
  if(radio.available()){
    char receivedMessage[32]={0};
    radio.read(receivedMessage, sizeof(receivedMessage));
    Serial.println(receivedMessage);
    radio.stopListening();
    delay(100);
  }
  delay(100);
}
