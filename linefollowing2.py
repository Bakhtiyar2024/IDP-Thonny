from machine import Pin
from time import sleep, ticks_ms
from MOTOR import Motor

# Initialize Sensors
left_sensor = Pin(10, Pin.IN)
right_sensor = Pin(11, Pin.IN)

# Initialize Motor Control
motor = Motor()

# Line Following Variables
on_line = False
start_time = 0
end_time = 0

line_width = 30  # mm
sensor_spacing = 20  # mm
forward_velocity = 20  # mm/s


def adjust(timer, turn):
    """Adjusts motor speed based on how long the sensor was off the line."""
    theta = min(0.5, (line_width - sensor_spacing) / max(timer * forward_velocity, 1))
    
    while not (left_sensor.value() and right_sensor.value()):
        if turn == "left":
            motor.left_turn(speed=int(50 * theta))  # Reduce speed for smoother correction
        elif turn == "right":
            motor.right_turn(speed=int(50 * theta))
    
    motor.Forward()  # Resume forward motion
    sleep(0.1)  # Brief delay to stabilize


def entry():
    """Ensure the robot smoothly transitions back to the line."""
    motor.Forward()
    sleep(0.2)


while True:
    left_value = left_sensor.value()
    right_value = right_sensor.value()
    
    if left_value == 1 and right_value == 1:  # Both sensors detect line
        if not on_line:
            start_time = ticks_ms()
        on_line = True
        motor.Forward()
    
    elif left_value == 1 and right_value == 0:  # Off to the right
        print("Adjust Left")
        if on_line:
            end_time = ticks_ms()
            adjust(end_time - start_time, turn="left")
        on_line = False
    
    elif left_value == 0 and right_value == 1:  # Off to the left
        print("Adjust Right")
        if on_line:
            end_time = ticks_ms()
            adjust(end_time - start_time, turn="right")
        on_line = False
    
    sleep(0.05)  # Reduce delay for quicker reaction
