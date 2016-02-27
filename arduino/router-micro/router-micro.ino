
// define the leds
int bar_led_1 = 2;
int bar_led_2 = 3;
int bar_led_3 = 4;
int bar_led_4 = 5;
int bar_led_5 = 6;

// string to store the incoming serial data
String serial_in;

void setup() {
  // set the led pins to output
  pinMode(bar_led_1, OUTPUT);
  pinMode(bar_led_2, OUTPUT);
  pinMode(bar_led_3, OUTPUT);
  pinMode(bar_led_4, OUTPUT);
  pinMode(bar_led_5, OUTPUT);

  // start the serial port
  Serial.begin(9600);

}

void loop() {

  //always set led1 on
  digitalWrite(bar_led_1, HIGH);
  
  // wait for  data on serial
  if (Serial.available() > 0) {
    serial_in = Serial.readStringUntil('\n');

    // turn a led on
    if (serial_in == "led1_on")
      digitalWrite(bar_led_1, HIGH);
    if (serial_in == "led2_on")
      digitalWrite(bar_led_2, HIGH);
    if (serial_in == "led3_on")
      digitalWrite(bar_led_3, HIGH);
    if (serial_in == "led4_on")
      digitalWrite(bar_led_4, HIGH);
    if (serial_in == "led5_on")
      digitalWrite(bar_led_5, HIGH);

    // turn a led off
    if (serial_in == "led1_off")
      digitalWrite(bar_led_1, LOW);
    if (serial_in == "led2_off")
      digitalWrite(bar_led_2, LOW);
    if (serial_in == "led3_off")
      digitalWrite(bar_led_3, LOW);
    if (serial_in == "led4_off")
      digitalWrite(bar_led_4, LOW);
    if (serial_in == "led5_off")
      digitalWrite(bar_led_5, LOW);


   // Enable to debug
   // Serial.print("serial in : ");
   // Serial.println(serial_in);

  }
}
