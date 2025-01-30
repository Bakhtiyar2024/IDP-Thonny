from machine import ADC
import time

# Initialize ADC on GPIO 26 (ADC0)
adc = ADC(26)  # GPIO 26 = ADC0

def read_distance():
    """
    Reads the distance from URM09 Ultrasonic Sensor in Analog Mode.
    :return: Distance in centimeters.
    """
    raw_value = adc.read_u16()  # Read 16-bit ADC value (0-65535)
    voltage = raw_value * 3.3 / 65535  # Convert ADC value to voltage (0-3.3V)

    # URM09 Analog Mode: 0.4V to 2.8V range corresponds to 4cm - 500cm
    if voltage < 0.4:
        return -1  # Out of range (too close)
    elif voltage > 2.8:
        return -1  # Out of range (too far)

    # Distance calculation (based on URM09 specs)
    distance_cm = (voltage - 0.4) * (500 - 4) / (2.8 - 0.4) + 4

    return round(distance_cm, 2)

# Main loop
while True:
    distance = read_distance()
    if distance == -1:
        print("Sensor error or out of range")
    else:
        print(f"Distance: {distance} cm")
    time.sleep(1)  # Read every second
