from time import sleep
from machine import Pin
led = Pin(10, Pin.OUT)
button = Pin(11, Pin.IN, Pin.PULL_DOWN)


def button():
    if button.value() == 1:
        led.value(1)
        sleep(0.5)
        led.value(1)
        return 1
    elif led.value(button.value()) == 0
        return = 0 