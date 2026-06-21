import time

from utils.motor import Motor

class Drivetrain:

    TICK = 0.014925

    def __init__(self, i2c, pca, intake, sorter, channel_ids=[0, 1, 2, 3]):
        # in order of front left, front right, back left, back right

        front_left = Motor(channel_id=channel_ids[0], i2c=i2c, pca=pca)
        front_right = Motor(channel_id=channel_ids[1], i2c=i2c, pca=pca)
        back_left = Motor(channel_id=channel_ids[2], i2c=i2c, pca=pca)
        back_right = Motor(channel_id=channel_ids[3], i2c=i2c, pca=pca)

        time.sleep(4)

        self.intake = intake
        self.sorter = sorter
        self.motors = [front_left, front_right, back_left, back_right]

        print("drivetrain ready")

    def go_forward(self, velocity, duration, intake=False, sorter=False):
        now = time.monotonic()
        end_time = now + duration

        if intake:
            self.intake.on()

        self.motors[0].set_velocity(velocity)
        self.motors[1].set_velocity(velocity)
        self.motors[2].set_velocity(velocity)
        self.motors[3].set_velocity(velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()

            if intake:
                self.intake.update()
            
            if sorter:
                self.sorter.update()

            time.sleep(self.TICK)

        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()

        if intake:
            self.intake.off()
        
    def go_backward(self, velocity, duration, sorter=False):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].set_velocity(-velocity)
        self.motors[1].set_velocity(-velocity)
        self.motors[2].set_velocity(-velocity)
        self.motors[3].set_velocity(-velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()
            
            if sorter:
                self.sorter.update()
            
            time.sleep(self.TICK)

        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()

    def turn_left(self, velocity, duration, sorter=False):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].set_velocity(-velocity)
        self.motors[1].set_velocity(velocity)
        self.motors[2].set_velocity(-velocity)
        self.motors[3].set_velocity(velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()
            
            if sorter:
                self.sorter.update()

            time.sleep(self.TICK)
        
        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()
    
    def turn_right(self, velocity, duration,sorter=False):
        now = time.monotonic()
        end_time = now + duration

        self.motors[0].set_velocity(velocity)
        self.motors[1].set_velocity(-velocity)
        self.motors[2].set_velocity(velocity)
        self.motors[3].set_velocity(-velocity)

        while time.monotonic() <= end_time:
            for motor in self.motors:
                motor.update()
            
            if sorter:
                self.sorter.update()

            time.sleep(self.TICK)

        for motor in self.motors:
            motor.set_velocity(0.0)
            motor.update()