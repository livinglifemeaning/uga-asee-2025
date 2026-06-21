import RPi.GPIO as GPIO
import time


class StartupSystem:
    """Subsystem for the startup system"""
    WAITING = 0 # IDLE -> WAITING when gpio input detected
    RUNNING = 1 # when light is detected

    def __init__(self, pin):
        self.pin = pin
        self.state = StartupSystem.WAITING # starts as WAITING

        GPIO.setmode(GPIO.BCM) # GPIO num instead of actual pin num
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # waiting for input
        
    def _is_high(self) -> bool:
        pin_state = GPIO.input(self.pin)

        return pin_state == GPIO.HIGH

    def update(self):
        if self.state == StartupSystem.WAITING and self._is_high(): # is high + waiting -> running
            self.state = StartupSystem.RUNNING
        else:
            pass

    def stop(self):
        GPIO.cleanup(self.pin)
        self.light_sensor.stop()
