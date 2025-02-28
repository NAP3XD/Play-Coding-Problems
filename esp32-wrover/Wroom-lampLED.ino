// code for a push button that turns a LED on and off

#define PIN_LED 2
#define PIN_BUTTON 13


void setup() {
  // put your setup code here, to run once:
  
  // initialize input and output
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_BUTTON, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  if (digitalRead(PIN_BUTTON) == LOW {
    delay(13);
    if (digitalRead(PIN_BUTTON) == LOW {
      reverseGPIO(PIN_LED);
    }
    while (digitalRead(PIN_BUTTON) == LOW);
    delay(13);
    while (digitalRead(PIN_BUTTON) == LOW);
  }

}


VOID reverseGPIO(int pin) {
  digitalWrite(pin, ! digitalRead(pin));
}