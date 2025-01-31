from machine import I2C
import time

class VL53L0X:
    def __init__(self, i2c, address=0x29):
        self.i2c = i2c
        self.address = address

    def read(self):
        self.i2c.writeto(self.address, b'\x00')
        time.sleep(0.1)
        data = self.i2c.readfrom(self.address, 2)
        return (data[0] << 8) | data[1]
