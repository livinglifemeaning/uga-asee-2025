import time

from utils.motor import Motor
from utils.servo import Servo

class OuttakeSystem:
    """Subsystem for the outtake system"""
    def __init__(self, i2c, pca):
        self.i2c = i2c
        self.pca = pca

        self.outtake = Motor(channel_id=2, i2c=i2c, pca=pca)
        self.gate = Servo(pin=17, initial_angle=0.0, full_rotation_time=1.3)

    def gate_down(self):
        self.gate.set_angle(300.0)
        while self.gate.state != Servo.IDLE:
            self.gate.update()

    def gate_up(self):
        self.gate.set_angle(0.0)
        while self.gate.state != Servo.IDLE:
            self.gate.update()

    def on_double(self, duration):
        self.gate_down()

        now = time.monotonic()
        end_time = now + duration

        self.outtake.set_velocity(duration)
        while time.monotonic() <= end_time:
            self.outtake.update()

        self.outtake.set_velocity(0.0)
        self.outtake.update()

    def on_single(self, duration):
        self.gate_up()
        
        now = time.monotonic()
        end_time = now + duration

        self.outtake.set_velocity(duration)
        while time.monotonic() <= end_time:
            self.outtake.update()

        self.outtake.set_velocity(0.0)
        self.outtake.update()
