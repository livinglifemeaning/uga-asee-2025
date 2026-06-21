import time
import board
import busio
from adafruit_pca9685 import PCA9685

from subsystems.drivetrain import Drivetrain
from subsystems.startup import StartupSystem
from utils.motor import Motor


i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

drivetrain = Drivetrain(i2c, pca)
startup = StartupSystem()

while startup.state != StartupSystem.RUNNING:
    startup.update()
    time.sleep(0.1)

drivetrain.go_forward(0.5, 5.0)
