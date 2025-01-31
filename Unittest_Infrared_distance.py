import unittest
from machine import Pin, I2C

class TestI2CConnection(unittest.TestCase):
    def setUp(self):
        # Define I2C bus (default SDA=GP20, SCL=GP21 for Pico W)
        self.i2c = I2C(0, scl=Pin(21), sda=Pin(20))
    
    def test_i2c_device_detection(self):
        devices = self.i2c.scan()
        self.assertGreater(len(devices), 0, "No I2C devices found. Check wiring!")
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
