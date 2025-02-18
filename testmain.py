import machine
import time

# Define the GPIO pin for the button
BUTTON_PIN = 11  # Change this to your actual pin
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)  # Enable internal pull-up resistor

print("Press the button to test... (Press Ctrl+C to stop)")

try:
    while True:
        if button.value() == 1:  # Button pressed (active-low)
            print("Button Pressed!")
            time.sleep(0.2)  # Debounce delay
        elif button.value() == 0:
            print("Button Released")
            time.sleep(0.1)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    print("\nExiting...")
