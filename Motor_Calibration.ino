#include <Servo.h>

Servo motor3;

void setup() {    
  Serial.begin(115200);
  motor3.attach(9);              // ESC signal wire
  motor3.writeMicroseconds(2000); // Minimum throttle
  delay(10000); 
  for (int pulse = 2000; pulse >= 1050; pulse -= 50) { // increase by 5 µs each step
    Serial.println(pulse);
    motor3.writeMicroseconds(pulse);
    delay(50);  // wait 50 ms between steps
  }     
  delay(10000);

}

void loop() {

}
