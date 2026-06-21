import time

from utils.motor import Motor

class Drivetrain:
    def __init__(self, motors: list[Motor]):
        # in order of front left, front right, back left, back right
        self.motors = motors

    def go_forward(self, velocity, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].set_velocity(velocity)
        self.motors[1].set_velocity(velocity)
        self.motors[2].set_velocity(velocity)
        self.motors[3].set_velocity(velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()

        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()
        