import machine
import time

# Define the GPIO pin for the button
BUTTON_PIN = 11
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)  # Pull-up resistor enabled



def restart_script(pin):
    """Immediately resets the Raspberry Pi Pico when the button is pressed."""
    #print("Button pressed! Restarting now...")
    time.sleep(0.2)  # Small delay to avoid bouncing
    machine.reset()  # Hard reset the board


#print("Waiting for button press to start...")

# Wait for the first button press to start

