from machine import I2C
import time

VL53L0X_I2C_ADDR = 0x29

class VL53L0X:
    def __init__(self, i2c, address=VL53L0X_I2C_ADDR):
        self.i2c = i2c
        self.address = address
        self.init_sensor()

    def write_register(self, register, value):
        """Write a single byte to a register."""
        self.i2c.writeto(self.address, bytes([register, value]))

    def read_register(self, register, length=1):
        """Read one or more bytes from a register."""
        self.i2c.writeto(self.address, bytes([register]))  # No 'stop=False' in MicroPython
        return self.i2c.readfrom(self.address, length)  # No keyword arguments

    def init_sensor(self):
        """Initialize the VL53L0X sensor."""
        try:
            self.write_register(0x88, 0x00)  # Stop Mode
            time.sleep(0.005)

            self.write_register(0x80, 0x01)
            self.write_register(0xFF, 0x01)
            self.write_register(0x00, 0x00)
            self.address = VL53L0X_I2C_ADDR  # Reset I2C address
            self.write_register(0x91, 0x3C)
            self.write_register(0x00, 0x01)
            self.write_register(0xFF, 0x00)
            self.write_register(0x80, 0x00)

            self.write_register(0x60, 0x01)  # Set timing budget
            time.sleep(0.05)
        except Exception as e:
            print("VL53L0X Initialization Failed:", e)

    def start(self):
        """Start continuous measurement."""
        self.write_register(0x80, 0x01)
        self.write_register(0xFF, 0x01)
        self.write_register(0x00, 0x00)
        self.write_register(0x91, 0x3C)
        self.write_register(0x00, 0x01)
        self.write_register(0xFF, 0x00)
        self.write_register(0x80, 0x00)
        self.write_register(0x00, 0x02)  # Start continuous measurement

    def stop(self):
        """Stop measurement."""
        self.write_register(0x00, 0x01)  # Enter single-shot mode

    def read(self):
        """Read the distance measurement (in mm)."""
        try:
            data = self.read_register(0x14, 2)  # Read 2 bytes
            if len(data) < 2:
                return 255  # Return error if read failed

            distance = (data[0] << 8) | data[1]
            if distance == 65535:
                return 255  # Invalid reading
            return distance
        except Exception as e:
            print("VL53L0X Read Error:", str(e))
            return 255  # Return max distance if an error occurs
