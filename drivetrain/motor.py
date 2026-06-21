import time
import board
import busio
from adafruit_pca9685 import PCA9685

# ----------------------------
# Setup
# ----------------------------
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

NEUTRAL_US = 1550   # your measured stop point

def set_pulse_us(channel, pulse_us):
    # 20,000 us frame at 50 Hz, 4096 counts
    counts = round((pulse_us / 20000.0) * 4096)
    counts = max(0, min(4095, counts))

    # Scale 12-bit count to library's 16-bit duty_cycle
    pca.channels[channel].duty_cycle = counts << 4
    print(f"channel={channel}, pulse_us={pulse_us}, counts={counts}")

try:
    print("Arm at neutral")
    set_pulse_us(0, NEUTRAL_US)
    time.sleep(5)

    print("\nForward check")
    for us in [1570, 1580]:
        print(f"Trying {us} us")
        set_pulse_us(0, us)
        time.sleep(2)
        set_pulse_us(0, NEUTRAL_US)
        time.sleep(2)

    print("\nReverse check")
    for us in [1490, 1480]:
        print(f"Trying {us} us")
        set_pulse_us(0, us)
        time.sleep(2)
        set_pulse_us(0, NEUTRAL_US)
        time.sleep(2)

finally:
    set_pulse_us(0, NEUTRAL_US)
    time.sleep(1)
    pca.deinit()