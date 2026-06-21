class Motor:

    IDLE = 0
    RUNNING = 1

    def __init__(self, channel_id, i2c, pca):

        self._channel_id = channel_id
        self._command_velocity = 0.0
        self.state = Motor.IDLE

        self.i2c = i2c
        self.pca = pca

        self.NEUTRAL_US = 1550   # your measured stop point
        self.RANGE = 100  # range of pulse width for full forward/reverse

        print("motor ready")

    def set_velocity(self, velocity):
        if velocity < -1.0 or velocity > 1.0:
            raise ValueError("Velocity must be between -1.0 and 1.0")

        self._command_velocity = velocity

    def set_pulse_us(self, pulse_us):
        # 20,000 us frame at 50 Hz, 4096 counts
        counts = round((pulse_us / 20000.0) * 4096)
        counts = max(0, min(4095, counts))

        # Scale 12-bit count to library's 16-bit duty_cycle
        self.pca.channels[self._channel_id].duty_cycle = counts << 4

    def update(self):
        if self._command_velocity == 0.0:
            self.state = Motor.IDLE
        else:
            self.state = Motor.RUNNING

        pulse_us = self.NEUTRAL_US + (self._command_velocity * self.RANGE)  # Scale velocity to pulse width
        self.set_pulse_us(pulse_us)