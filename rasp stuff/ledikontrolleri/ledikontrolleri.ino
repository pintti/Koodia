int pred=5, pblue=7, pgreen=3;

void setup() {
  pinMode(pred, OUTPUT);
  pinMode(pblue, OUTPUT);
  pinMode(pgreen, OUTPUT);
}

void loop() {
  analogWrite(pred, 255);
  analogWrite(pblue, 170);
  analogWrite(pgreen, 100);

  delay(200);
}
