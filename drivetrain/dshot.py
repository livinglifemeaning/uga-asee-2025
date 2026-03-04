#include <stdio.h>
#include <unistd.h>
#include "dshot.h"  // or your header that includes motorImplementation* functions

int main() {
    int motorPins[] = {21}; // single motor
    int motorMax = 1;
    double throttle[1];

    printf("Initializing motor on GPIO21...\n");
    motorImplementationInitialize(motorPins, motorMax);

    printf("== Test 1: Normal spin direction forward ==\n");
    motorImplementationSet3dModeAndSpinDirection(motorPins, motorMax, 0, 0); // 3D off, normal
    throttle[0] = 0.2;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    printf("== Test 2: Normal spin direction reversed ==\n");
    motorImplementationSet3dModeAndSpinDirection(motorPins, motorMax, 0, 1); // 3D off, reversed
    throttle[0] = 0.2;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    printf("== Test 3: 3D mode forward (positive throttle) ==\n");
    motorImplementationSet3dModeAndSpinDirection(motorPins, motorMax, 1, 0); // 3D on, normal
    throttle[0] = 0.2; // positive = forward
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    printf("== Test 4: 3D mode backward (negative throttle) ==\n");
    throttle[0] = -0.2; // negative = backward
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    printf("== Test 5: 3D mode + reversed flag forward ==\n");
    motorImplementationSet3dModeAndSpinDirection(motorPins, motorMax, 1, 1); // 3D on, reversed
    throttle[0] = 0.2;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    printf("== Test 6: 3D mode + reversed flag backward ==\n");
    throttle[0] = -0.2;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);
    sleep(2);

    printf("== Test Complete. Stopping motor ==\n");
    throttle[0] = 0;
    motorImplementationSendThrottles(motorPins, motorMax, throttle);

    motorImplementationFinalize(motorPins, motorMax);
    return 0;
}
