from time import sleep
from machine import Pin

led = Pin(10, Pin.OUT)
button = Pin(11, Pin.IN, Pin.PULL_DOWN)

# Store button state globally
button_pressed = False

def check_button():
    global button_pressed  # Access global variable

    if button.value() == 1:
        led.value(1)  # Turn LED on
        sleep(0.5)  # Debounce delay
        button_pressed = True  # Latch the button state

    return 1 if button_pressed else 0  # Keep value at 1 after press
