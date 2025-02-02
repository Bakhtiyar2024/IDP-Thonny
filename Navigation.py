from motor import Motor
from line_sensor import check_sensors
from qr_reader import QRCodeReader
from actuator import move_actuator
from distance_sensor import VL53L0X
import time

# Initialize components
motor = Motor()
qr_reader = QRCodeReader()
distance_sensor = VL53L0X()

# Constants
DISTANCE_THRESHOLD_APPROACH = 100  # 10 cm
DISTANCE_THRESHOLD_PICKUP = 10  # 1 cm
SPEED = 100

# Path storage for reverse navigation
path_taken = []

def drive_forward(distance_cm):
    """Drive forward for a specific distance in cm."""
    motor.Forward()
    time.sleep(distance_cm / 10)  # Adjust timing based on speed
    motor.off()

def approach_slowly(threshold):
    """Approach slowly until the distance sensor reads less than the threshold."""
    while True:
        distance = distance_sensor.ping()
        if distance == -1:
            print("Error: Distance sensor not responding.")
            break
        elif distance < threshold:
            motor.off()
            break
        else:
            motor.Forward(speed=SPEED // 2)  # Slow speed
        time.sleep(0.1)

def pick_up_box():
    """Pick up the box using the actuator."""
    move_actuator("extend", duration=2)  # Extend actuator
    time.sleep(1)
    move_actuator("retract", duration=2)  # Retract actuator

def navigate_to_destination(destination):
    """Navigate to the destination based on QR code instructions."""
    print(f"Navigating to {destination}...")
    while True:
        result = check_sensors()
        if result == "T-junction":
            print("T-junction detected. Executing command...")
            # Store the turn direction in the path_taken list
            if destination == "left":
                motor.left_turn()
                path_taken.append("right")  # Reverse turn for return path
            elif destination == "right":
                motor.right_turn()
                path_taken.append("left")  # Reverse turn for return path
            else:
                motor.Forward()  # Default to forward if no specific turn
            time.sleep(1)  # Allow time for the turn to complete
            break
        time.sleep(0.1)

def reverse_navigation():
    """Reverse the path taken to return to the starting position."""
    print("Reversing path to return to start...")
    for turn in reversed(path_taken):
        print(f"Executing reverse turn: {turn}")
        if turn == "left":
            motor.left_turn()
        elif turn == "right":
            motor.right_turn()
        time.sleep(1)  # Allow time for the turn to complete
    # Drive forward to return to the starting position
    motor.Forward()
    time.sleep(2)  # Adjust timing based on distance
    motor.off()

def main():
    # Start at the starting position
    print("Starting navigation...")

    # Drive forward 10 cm
    drive_forward(10)

    # Navigate to Depot A
    navigate_to_destination("Depot A")

    # Approach slowly until 10 cm from the box
    approach_slowly(DISTANCE_THRESHOLD_APPROACH)

    # Read QR code
    qr_data = qr_reader.read_qr_code()
    if qr_data:
        next_destination = qr_data[0]  # First letter of QR code
        print(f"Next destination: {next_destination}")
    else:
        print("Error: No QR code detected.")
        return

    # Approach the box until 1 cm away
    approach_slowly(DISTANCE_THRESHOLD_PICKUP)

    # Pick up the box
    pick_up_box()

    # Navigate to the next destination
    navigate_to_destination(next_destination)

    # Reverse path to return to the starting position
    reverse_navigation()

    # Repeat the process four more times
    for _ in range(4):
        print("Starting next iteration...")
        # Drive forward 10 cm
        drive_forward(10)

        # Navigate to Depot A
        navigate_to_destination("Depot A")

        # Approach slowly until 10 cm from the box
        approach_slowly(DISTANCE_THRESHOLD_APPROACH)

        # Read QR code
        qr_data = qr_reader.read_qr_code()
        if qr_data:
            next_destination = qr_data[0]  # First letter of QR code
            print(f"Next destination: {next_destination}")
        else:
            print("Error: No QR code detected.")
            return

        # Approach the box until 1 cm away
        approach_slowly(DISTANCE_THRESHOLD_PICKUP)

        # Pick up the box
        pick_up_box()

        # Navigate to the next destination
        navigate_to_destination(next_destination)

        # Reverse path to return to the starting position
        reverse_navigation()

if __name__ == "__main__":
    main()