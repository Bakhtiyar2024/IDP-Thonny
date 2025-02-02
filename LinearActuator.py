from machine import Pin
import time

# Define actuator control pins
EXTEND_PIN = Pin(20, Pin.OUT)
RETRACT_PIN = Pin(21, Pin.OUT)

def move_actuator(action, duration=2):
    """
    Controls the linear actuator.
    
    :param action: "extend" to push out, "retract" to pull in, "stop" to halt movement.
    :param duration: Time in seconds to move (adjust based on stroke length).
    """
    if action == "extend":
        EXTEND_PIN.value(1)
        RETRACT_PIN.value(0)
        time.sleep(duration)
        EXTEND_PIN.value(0)  # Stop actuator

    elif action == "retract":
        EXTEND_PIN.value(0)
        RETRACT_PIN.value(1)
        time.sleep(duration)
        RETRACT_PIN.value(0)  # Stop actuator

    elif action == "stop":
        EXTEND_PIN.value(0)
        RETRACT_PIN.value(0)

    else:
        print("Invalid action. Use 'extend', 'retract', or 'stop'.")

# Example usage in main.py:
# move_actuator("extend", 2)  # Extend for 2 seconds
# move_actuator("retract", 2)  # Retract for 2 seconds
