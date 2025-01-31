from machine import Pin, I2C
import time
import vl53l0x  # Import the fixed VL53L0X driver

# Initialize I2C (SDA=GP20, SCL=GP21)
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Scan for I2C devices
devices = i2c.scan()
if 0x29 not in devices:
    print("VL53L0X not found! Check wiring.")
else:
    print("VL53L0X found at address 0x29.")

# Initialize the sensor
tof = vl53l0x.VL53L0X(i2c)
tof.start()  # Start continuous measurement

def read_distance():
    while True:
        distance = tof.read()
        if distance == 255:  # Sensor error signal
            print("Warning: Invalid distance reading (255 mm). Check wiring.")
        elif distance > 2000:  # VL53L0X has a max range of ~2m
            print(f"Warning: Distance out of range! Got {distance} mm")
        else:
            print(f"Distance: {distance} mm")
        time.sleep(0.5)

if __name__ == "__main__":
    read_distance()
