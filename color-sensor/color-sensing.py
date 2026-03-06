from smbus2 import SMBus
import time


bus = SMBus(1)
sensor_address = 0x10
command_register= 0x00
red_register = 0x08
green_register = 0x09
blue_register = 0x0A
white_register = 0x0B

# Sets command code to values of zero
# Shutdown (bit 0) = 0 enables device, = 1 disables device
# Auto force mode (bit 1) = 0 continuously measures color, = 1 measures color once 
bus.write_word_data(sensor_address, command_register, 0x00)
time.sleep(0.1)

### Every second, reads RGB and white values
while True: 
    try: 
        red_data = bus.read_word_data(sensor_address, red_register)
        green_data = bus.read_word_data(sensor_address, green_register)
        blue_data = bus.read_word_data(sensor_address, blue_register)
        white_data = bus.read_word_data(sensor_address, white_register)
        
        print(f"Red Value={red_data} Green Value={green_data} Blue Value={blue_data} White Value ={white_data}")

        ## Determines color of ball, using a hacky method, needs tweaking
        if red_data > 200 and white_data < 500: 
            print("this is a red ball")
        elif white_data > 500:
            print("this is a white ball")
        else: 
            print("this is a blue ball")
    except Exception as e: 
        print("Error Reading Data", e)

    time.sleep(1)