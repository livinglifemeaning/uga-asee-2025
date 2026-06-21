import time

from utils.motor import Motor

class Drivetrain:
    def __init__(self, i2c, pca):
        # in order of front left, front right, back left, back right

        
        front_left = Motor(channel_id=0, i2c=i2c, pca=pca)
        front_right = Motor(channel_id=1, i2c=i2c, pca=pca)
        back_left = Motor(channel_id=2, i2c=i2c, pca=pca)
        back_right = Motor(channel_id=3, i2c=i2c, pca=pca)
        time.sleep(4)

        print("drivetrain ready")
        self.motors = [front_left, front_right, back_left, back_right]

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
        
    def go_backward(self, velocity, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].set_velocity(-velocity)
        self.motors[1].set_velocity(-velocity)
        self.motors[2].set_velocity(-velocity)
        self.motors[3].set_velocity(-velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()

        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()

    def turn_left(self, velocity, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].set_velocity(-velocity)
        self.motors[1].set_velocity(velocity)
        self.motors[2].set_velocity(-velocity)
        self.motors[3].set_velocity(velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()

        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()
    
    def turn_right(self, velocity, duration):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].set_velocity(velocity)
        self.motors[1].set_velocity(-velocity)
        self.motors[2].set_velocity(velocity)
        self.motors[3].set_velocity(-velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()

        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()