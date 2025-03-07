from machine import Pin, PWM
import time


speed=100
r2 = 1
r1 = 0.97
r1r = 1
r2r = 1

class Motor: 
    def __init__(self): 
        self.m1Dir = Pin(4 , Pin.OUT)         # set pin left wheel 
        self.pwm1 = PWM(Pin(5))           
        self.pwm1.freq(1000) 
        self.pwm1.duty_u16(0)
        
        self.m2Dir = Pin(7 , Pin.OUT)         # set pin left wheel 
        self.pwm2 = PWM(Pin(6))           
        self.pwm2.freq(1000) 
        self.pwm2.duty_u16(0)
        
        self.m3Dir = Pin(0 , Pin.OUT)         # actuator
        self.pwm3 = PWM(Pin(1))           
        self.pwm3.freq(1000) 
        self.pwm3.duty_u16(0)           
        
        self.led = Pin(10, Pin.OUT)            #variable to control LED
        
    def off(self):                       #stop both wheels
        self.pwm1.duty_u16(0)
        self.pwm2.duty_u16(0)
        self.led.value(0)
        
    def Reverse(self, speed=40): 
    """Moves the robot in reverse at the given speed (default 40%)."""
    self.m1Dir.value(0)  # Motor 1 reverse
    self.pwm1.duty_u16(int(65535 * speed * r1r / 100))
    self.m2Dir.value(0)  # Motor 2 reverse
    self.pwm2.duty_u16(int(65535 * speed * r2r / 100))
    self.led.value(1)  

    def Forward(self, speed=100): 
        """Moves the robot forward at the given speed (default 100%)."""
        self.m1Dir.value(1)  
        self.pwm1.duty_u16(int(65535 * speed * r1 / 100))
        self.m2Dir.value(1)  
        self.pwm2.duty_u16(int(65535 * speed * r2 / 100))
        self.led.value(1)  

    def acw_spin(self, speed): 
        """Spins the robot anti-clockwise (left)."""
        self.m1Dir.value(1)  
        self.pwm1.duty_u16(int(65535 * speed * r1 / 100))
        self.m2Dir.value(0)  
        self.pwm2.duty_u16(int(65535 * speed * r2 / 100))
        self.led.value(1)  

    def cw_spin(self, speed): 
        """Spins the robot clockwise (right)."""
        self.m1Dir.value(0)  
        self.pwm1.duty_u16(int(65535 * speed * r1 / 100))
        self.m2Dir.value(1)  
        self.pwm2.duty_u16(int(65535 * speed * r2 / 100))
        self.led.value(1)  

    def Actuator_up(self, speed, duration=2.3):
        """Moves an actuator up for a set duration."""
        self.m3Dir.value(1)  
        self.pwm3.duty_u16(int(65535 * speed / 100))
        time.sleep(duration)
        self.pwm3.duty_u16(0)
        self.led.value(1)  

    def Actuator_down(self, speed, duration=2.2):
        """Moves an actuator down for a set duration."""
        self.m3Dir.value(0)  
        self.pwm3.duty_u16(int(65535 * speed / 100))
        time.sleep(duration)
        self.pwm3.duty_u16(0)
        self.led.value(1)  

    def adjust_direction(self, turn, speed=100):
        """Adjusts movement direction: 'left', 'right', or 'none' (straight)."""
        self.led.value(1)  

        if turn == "left":
            self.m1Dir.value(1)  
            self.pwm1.duty_u16(int(65535 * speed * r1 / 100))
            self.m2Dir.value(1)  
            self.pwm2.duty_u16(int(65535 * (speed * r2 * 0.75) / 100))

        elif turn == "right":
            self.m1Dir.value(1)  
            self.pwm1.duty_u16(int(65535 * (speed * r1 * 0.75) / 100))
            self.m2Dir.value(1)  
            self.pwm2.duty_u16(int(65535 * speed * r2 / 100))

        elif turn == "none":
            self.m1Dir.value(1)  
            self.pwm1.duty_u16(int(65535 * speed * r1 / 100))
            self.m2Dir.value(1)  
            self.pwm2.duty_u16(int(65535 * speed * r2 / 100))
            
    """
    def rev_adjust_direction(self, turn):
        if turn == "right":
            self.m1Dir.value(1) 
            self.pwm1.duty_u16(int(65535*(r1*40*1)/100))
            self.m2Dir.value(1) 
            self.pwm2.duty_u16(int(65535*(r2*40*0.9)/100))
        elif turn == "left":
            self.m1Dir.value(1)
            self.pwm1.duty_u16(int(65535*(r1*40*0.9)/100))
            self.m2Dir.value(1)
            self.pwm2.duty_u16(int(65535*(r2*40*1)/100))
    """