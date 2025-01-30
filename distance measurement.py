from machine import Pin, time_pulse_us
import time

def measure_distance(trigger_pin=2, echo_pin=3):
    """
    Measures distance using an HC-SR04 ultrasonic sensor.
    :param trigger_pin: GPIO pin connected to the TRIG pin of the sensor.
    :param echo_pin: GPIO pin connected to the ECHO pin of the sensor.
    :return: Distance in centimeters.
    """
    trig = Pin(trigger_pin, Pin.OUT)
    echo = Pin(echo_pin, Pin.IN)
    
    # Ensure trigger is low
    trig.low()
    time.sleep_us(2)
    
    # Send a 10us pulse to trigger
    trig.high()
    time.sleep_us(10)
    trig.low()
    
    # Measure the echo pulse duration (in microseconds)
    duration = time_pulse_us(echo, 1, 30000)  # 30ms timeout (max range ~5m)
    
    if duration < 0:
        return -1  # Indicate timeout error
    
    # Convert time to distance (speed of sound is ~343m/s or 0.0343 cm/us)
    distance = (duration * 0.0343) / 2  # Divide by 2 to account for round-trip
    
    return round(distance, 2)  # Return rounded value

# Example usage
if __name__ == "__main__":
    while True:
        dist = measure_distance()
        if dist == -1:
            print("Out of range or sensor error")
        else:
            print(f"Distance: {dist} cm")
        time.sleep(1)
