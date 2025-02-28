#define PIN_LED 2
void setup() {
  // put your setup code here, to run once:

  // set GPIO 
  pinMode(PIN_LED, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  // will blink on and off
  digitalWrite(PIN_LED, HIGH);
  delay(1000);
  digitalWrite(PIN_LED, LOW);
  delay(10000);


}
