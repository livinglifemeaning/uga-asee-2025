import time

from utils.motor import Motor

class SorterSystem:
    
    sensor_address = 0x10
    command_register= 0x00
    red_register = 0x08
    green_register = 0x09
    blue_register = 0x0A
    white_register = 0x0B

    EMPTY = 0
    RED = 1
    WHITE = 2
    BLUE = 3

    READY = 4
    SORTING = 5

    TIME_TO_DROP = 1.0

    def __init__(self, i2c, pca, bus, channel_ids=[5, 6, 7]):
        self.i2c = i2c
        self.pca = pca
        self.bus = bus

        self.red_data = None
        self.green_data = None
        self.blue_data = None
        self.white_data = None

        self.detect = SorterSystem.EMPTY

        self._endtime = time.monotonic()
        self._state = SorterSystem.READY

        self.sorter_motor_1 = Motor(channel_id=channel_ids[0], i2c=i2c, pca=pca)
        self.sorter_motor_2 = Motor(channel_id=channel_ids[1], i2c=i2c, pca=pca)
        self.sorter_motor_3 = Motor(channel_id=channel_ids[2], i2c=i2c, pca=pca)

    def read_data(self):
        try:
            
            self.red_data = self.bus.read_word_data(SorterSystem.sensor_address, SorterSystem.red_register)
            self.green_data = self.bus.read_word_data(SorterSystem.sensor_address, SorterSystem.green_register)
            self.blue_data = self.bus.read_word_data(SorterSystem.sensor_address, SorterSystem.blue_register)
            self.white_data = self.bus.read_word_data(SorterSystem.sensor_address, SorterSystem.white_register)

            # TODO: tune values here
            if self.red_data > 200 and self.white_data < 500: 
                self.detect = SorterSystem.RED
            elif self.white_data > 500:
                self.detect = SorterSystem.WHITE
            elif self.blue_data > 200: 
                self.detect = SorterSystem.BLUE
            else:
                self.detect = SorterSystem.EMPTY

        except Exception as e: 
            print("Error Reading Data", e)

    def update(self):
        # read bus rgb value
        # if color is detected, spin appropriate motors for 1 second (so until end time)

        self.read_data()

        if self._state == SorterSystem.READY and self.detect != SorterSystem.EMPTY:
            self._state = SorterSystem.SORTING

            if self.detect == SorterSystem.RED:
                self.sorter_motor_1.set_velocity(0.8)
                self.sorter_motor_1.update()
                self._endtime = time.monotonic() + self.TIME_TO_DROP

            elif self.detect == SorterSystem.WHITE:
                self.sorter_motor_2.set_velocity(0.8)
                self.sorter_motor_2.update()
                self._endtime = time.monotonic() + self.TIME_TO_DROP

            elif self.detect == SorterSystem.BLUE:
                self.sorter_motor_3.set_velocity(0.8)
                self.sorter_motor_3.update()
                self._endtime = time.monotonic() + self.TIME_TO_DROP

        elif self._state == SorterSystem.SORTING:
            if time.monotonic() >= self._endtime:
                if self.sorter_motor_1.state == Motor.RUNNING:
                    self.sorter_motor_1.set_velocity(0.0)

                if self.sorter_motor_2.state == Motor.RUNNING:
                    self.sorter_motor_2.set_velocity(0.0)

                if self.sorter_motor_3.state == Motor.RUNNING:
                    self.sorter_motor_3.set_velocity(0.0)
                
                self.sorter_motor_1.update()
                self.sorter_motor_2.update()
                self.sorter_motor_3.update()

                self._state = SorterSystem.READY
    
            else:
                if self.sorter_motor_1.state == Motor.RUNNING:
                    self.sorter_motor_1.update()

                if self.sorter_motor_2.state == Motor.RUNNING:
                    self.sorter_motor_2.update()

                if self.sorter_motor_3.state == Motor.RUNNING:
                    self.sorter_motor_3.update()