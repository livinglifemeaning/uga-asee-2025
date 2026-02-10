#include <Servo.h>

Servo motor3;

void setup() {
  Serial.begin(115200);
  motor3.attach(9);                // ESC signal wire
  motor3.writeMicroseconds(1050);  // Minimum throttle
  delay(10000);                    // Hold 10s to let ESC arm
}

void loop() {
  // Gradually increase speed

  for (int pulse = 1050; pulse <= 2000; pulse += 5) {  // increase by 5 µs each step
    Serial.println(pulse);
    motor3.writeMicroseconds(pulse);
    delay(50);  // wait 50 ms between steps
  }

  delay(2000);  // Hold at max speed

  // Gradually decrease speed then stops at 1050
  for (int pulse = 2000; pulse >= 1050; pulse -= 5) {
    Serial.println(pulse);
    motor3.writeMicroseconds(pulse);
    delay(100);
  }

  delay(2000);  // Hold at minimum
}
