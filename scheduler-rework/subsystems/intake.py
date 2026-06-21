import time

from utils.motor import Motor

class IntakeSystem:
    """Subsystem for the intake system"""
    def __init__(self, channel_id, i2c, pca):
        self.i2c = i2c
        self.pca = pca
        self.intake = Motor(channel_id=channel_id, i2c=i2c, pca=pca)

    def on(self):
        self.intake.set_velocity(0.8)
        self.intake.update()

    def off(self):
        self.intake.set_velocity(0.0)
        self.intake.update()

    def on_timed(self, duration):
        self.on()
        now = time.monotonic()
        end_time = now + duration

        while time.monotonic() <= end_time:
            self.intake.update()

        self.off()

    def update(self):
        self.intake.update()