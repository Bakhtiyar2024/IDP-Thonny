from machine import Pin, I2C
import time

# Initialize I2C for VL53L0X
i2c = I2C(id=0, sda=Pin(0), scl=Pin(1))  # Adjust pins based on your wiring
print("I2C devices found:", [hex(addr) for addr in i2c.scan()])

# VL53L0X setup
class VL53L0X:
    def __init__(self, i2c, address=0x29):
        self.i2c = i2c
        self.address = address
        self.init_sensor()

    def init_sensor(self):
        # Initialize the sensor
        self.write_reg(0x88, 0x00)
        self.write_reg(0x80, 0x01)
        self.write_reg(0xFF, 0x01)
        self.write_reg(0x00, 0x00)
        self.stop_variable = self.read_reg(0x91)
        self.write_reg(0x00, 0x01)
        self.write_reg(0xFF, 0x00)
        self.write_reg(0x80, 0x00)

        # Set timing budget and VCSEL periods
        self.set_measurement_timing_budget(200000)  # 200ms timing budget
        self.set_vcsel_pulse_period(0, 12)  # Pre-range period
        self.set_vcsel_pulse_period(1, 8)   # Final-range period

    def write_reg(self, reg, value):
        self.i2c.writeto_mem(self.address, reg, bytearray([value]))

    def read_reg(self, reg):
        return self.i2c.readfrom_mem(self.address, reg, 1)[0]

    def set_measurement_timing_budget(self, budget_us):
        # Set the measurement timing budget in microseconds
        self.write_reg(0xFF, 0x01)
        self.write_reg(0x0D, 0x01)
        self.write_reg(0xFF, 0x00)
        self.write_reg(0x80, 0x00)
        self.write_reg(0xFF, 0x01)
        self.write_reg(0x0D, 0x00)
        self.write_reg(0xFF, 0x00)

    def set_vcsel_pulse_period(self, type_, period):
        # Set VCSEL pulse period (type 0: pre-range, type 1: final-range)
        vcsel_period_reg = 0x00 if type_ == 0 else 0x01
        self.write_reg(0xFF, 0x01)
        self.write_reg(vcsel_period_reg, period)
        self.write_reg(0xFF, 0x00)

    def ping(self):
        # Start ranging
        self.write_reg(0x80, 0x01)
        self.write_reg(0xFF, 0x01)
        self.write_reg(0x00, 0x00)
        self.write_reg(0x91, self.stop_variable)
        self.write_reg(0x00, 0x01)
        self.write_reg(0xFF, 0x00)
        self.write_reg(0x80, 0x00)

        # Wait for measurement
        start_time = time.ticks_ms()
        while (self.read_reg(0x13) & 0x07) == 0:
            if time.ticks_diff(time.ticks_ms(), start_time) > 1000:
                return -1  # Timeout

        # Read distance
        distance = self.read_reg(0x1E) << 8 | self.read_reg(0x1F)
        self.write_reg(0x0B, 0x01)  # Clear interrupt

        return distance

# Create VL53L0X object
tof = VL53L0X(i2c)

# Main loop
while True:
    distance = tof.ping()
    if distance == -1:
        print("Error: Sensor timeout or not responding.")
    else:
        print(f"Distance: {distance} mm")
    time.sleep(0.1)