import machine
import time

# VL53L0 I2C Address
VL53L0_I2C_ADDRESS = 0x29  # Confirmed from I2C scan

# Initialize I2C on GPIO 8 (SDA) and GPIO 9 (SCL)
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=100000)

def read_distance():
    """
    Reads the distance from VL53L0 sensor via I2C.
    :return: Distance in millimeters, or -1 if no response.
    """
    try:
        i2c.writeto(VL53L0_I2C_ADDRESS, b'\x00')  # Send measurement command
        time.sleep(0.1)  # Allow time for sensor to process
        data = i2c.readfrom(VL53L0_I2C_ADDRESS, 2)  # Read 2 bytes from sensor
        
        if len(data) == 2:
            distance = (data[0] << 8) | data[1]  # Convert bytes to distance
            return round(distance / 10, 2)  # Convert mm to cm
        else:
            return -1  # Invalid response

    except OSError:
        return -1  # Communication error

# Main loop
while True:
    distance = read_distance()
    if distance == -1:
        print("Sensor error or out of range")
    else:
        print(f"Distance: {distance} cm")
    time.sleep(1)  # Read every second
