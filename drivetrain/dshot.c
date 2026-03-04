#include <stdio.h>
#include <unistd.h>
#include "dshot-pio.c"   // your Pi 5 PIO implementation from the repo

int main() {
    int motorPins[] = {21};
    int motorMax = 1;
    double throttle[1];

    // Initialize motor
    motorImplementationInitialize(motorPins, motorMax);

    // Forward
    motorImplementationSet3dModeAndSpinDirection(motorPins, motorMax, 0, 0);
    throttle[0] = 0.2;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    // Reverse
    motorImplementationSet3dModeAndSpinDirection(motorPins, motorMax, 0, 1);
    throttle[0] = 0.2;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    // Stop motor
    throttle[0] = 0;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);

    motorImplementationFinalize(motorPins, motorMax);
    return 0;
}
