from machine import Pin
import time

# Define GPIO pins for the line sensors
left_sensor = Pin(14, Pin.IN)  # Adjust GPIO pin if needed
right_sensor = Pin(15, Pin.IN)  # Adjust GPIO pin if needed

DEBOUNCE_TIME = 50  # Delay in milliseconds to confirm sensor reading
T_JUNCTION_DELAY = 100  # Time to wait before deciding if it's a T-junction

def check_sensors():
    while True:
        left_detected = left_sensor.value()
        right_detected = right_sensor.value()

        if left_detected and not right_detected:  # Left sensor detects first
            time.sleep_ms(T_JUNCTION_DELAY)  # Wait to check for a T-junction
            if right_sensor.value():  # If right sensor also detects, it's a T-junction
                return "T-junction"
            return "left"

        elif right_detected and not left_detected:  # Right sensor detects first
            time.sleep_ms(T_JUNCTION_DELAY)
            if left_sensor.value():  # If left sensor also detects, it's a T-junction
                return "T-junction"
            return "right"

        elif left_detected and right_detected:  # Both sensors detect at the same time
            time.sleep_ms(DEBOUNCE_TIME)
            if left_sensor.value() and right_sensor.value():
                return "T-junction"

        time.sleep_ms(10)  # Small delay to prevent excessive looping

# Example usage
while True:
    result = check_sensors()
    if result:
        print(result)  # Replace with motor control logic if needed
