import time
import board
import busio
from adafruit_pca9685 import PCA9685
from smbus2 import SMBus

from subsystems.drivetrain import Drivetrain
from subsystems.startup import StartupSystem
from subsystems.outtake import OuttakeSystem
from subsystems.intake import IntakeSystem
from subsystems.sorter import SorterSystem

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
bus = SMBus(1)

bus.write_word_data(SorterSystem.sensor_address, SorterSystem.command_register, 0x00)
pca.frequency = 50

intake = IntakeSystem(channel_id=4, i2c=i2c, pca=pca)
sorter = SorterSystem(i2c=i2c, pca=pca, bus=bus, channel_ids=[5, 6, 7])

drivetrain = Drivetrain(i2c=i2c, pca=pca, intake=intake, sorter=sorter, channel_ids=[0, 1, 2, 3])
outtake = OuttakeSystem(pin=1, channel_id=8, i2c=i2c, pca=pca)
startup = StartupSystem()

while startup.state != StartupSystem.RUNNING:
    startup.update()
    time.sleep(0.05)

intake.on_timed(4.0)

time.sleep(1)

drivetrain.go_forward(0.5, 3.0)
drivetrain.go_forward(0.5, 3.0, intake=True) 
drivetrain.turn_right(0.5, 2.0)
drivetrain.turn_left(0.5, 8.0, sorter=True)
drivetrain.go_backward(0.5, 3.0)

time.sleep(1)

outtake.on_double(2.0)
outtake.on_single(2.0)