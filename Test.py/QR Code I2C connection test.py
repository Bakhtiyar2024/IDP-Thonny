from machine import Pin, I2C
import time

# Initialize I2C bus on Pico W (SDA=GP20, SCL=GP21)
i2c = I2C(1, scl=Pin(19), sda=Pin(18))

# Wait a bit for the bus to stabilize
time.sleep(1)

# Scan for I2C devices
devices = i2c.scan()

# Check and print results
"""
if devices:
    print("I2C devices found at addresses:", [hex(device) for device in devices])
else:
    print("No I2C devices found. Check wiring!")
"""