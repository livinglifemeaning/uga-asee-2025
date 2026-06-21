import time
import board
import busio
from adafruit_pca9685 import PCA9685

from subsystems.drivetrain import Drivetrain
from utils.motor import Motor

def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = PCA9685(i2c)
    pca.frequency = 50

    front_left = Motor(channel_id=0, i2c=i2c, pca=pca)
    front_right = Motor(channel_id=1, i2c=i2c, pca=pca)
    back_left = Motor(channel_id=2, i2c=i2c, pca=pca)
    back_right = Motor(channel_id=3, i2c=i2c, pca=pca)

    drivetrain = Drivetrain([front_left, front_right, back_left, back_right])

    drivetrain.go_forward(1.0, 5.0)

if __name__ == "__main__":
    main()