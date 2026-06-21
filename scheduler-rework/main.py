import time
import board
import busio
from adafruit_pca9685 import PCA9685

from subsystems.drivetrain import Drivetrain
from subsystems.startup import StartupSystem
from subsystems.outtake import OuttakeSystem
from subsystems.intake import IntakeSystem

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

intake = IntakeSystem(channel_id=4, i2c=i2c, pca=pca)

drivetrain = Drivetrain(i2c=i2c, pca=pca, intake=intake)
outtake = OuttakeSystem(i2c=i2c, pca=pca)
startup = StartupSystem()

while startup.state != StartupSystem.RUNNING:
    startup.update()
    time.sleep(0.1)

drivetrain.go_forward(0.5, 3.0)
drivetrain.turn_right(0.5, 2.0)
drivetrain.turn_left(0.5, 2.0)  
drivetrain.go_backward(0.5, 3.0)

outtake.on_double(2.0)
outtake.on_single(2.0)