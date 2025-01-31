from machine import Pin, I2C
import time
import vl53l0x  # Ensure you have a VL53L0X MicroPython library installed

# Define I2C bus (Pico default I2C pins: SDA=GP20, SCL=GP21)
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

tof = vl53l0x.VL53L0X(i2c)

def read_distance():
    while True:
        distance = tof.read()
        print('Distance: {} mm'.format(distance))
        time.sleep(0.5)  # Adjust delay as needed

if __name__ == "__main__":
    read_distance()
