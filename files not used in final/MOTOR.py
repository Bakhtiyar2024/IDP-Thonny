from machine import Pin, PWM
import time


# M1=1 => Forward
# M2= => Backward

#Forward: M1=1, M2=0
#Backward: M2=0, M1=1
#Right turn: M1= , M2=
#Left turn: M1= , M2=

#wheel radius = 32mm
#at speed of 20, 1 rotation =5s
#therefore, velocity = 2 x 'speed' mm/s 

speed = 100

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
        
    def off(self): 
        self.pwm1.duty_u16(0)
        self.pwm2.duty_u16(0)
        
    def Reverse(self, speed = 100): 
        self.m1Dir.value(0)                     # forward = 0 reverse = 1 motor 1 
        self.pwm1.duty_u16(int(65535*speed/100))
        self.m2Dir.value(0)                     # forward = 0 reverse = 1 motor 1 
        self.pwm2.duty_u16(int(65535*speed/100))
        # speed range 0-100 motor 1
        
    def Forward(self, speed = 100): 
        self.m1Dir.value(0) 
        self.pwm1.duty_u16(int(65535*speed/100))
        self.m2Dir.value(0) 			
        self.pwm2.duty_u16(int(65535*speed/100))
        
    def acw_spin(self, speed = 100): 
        self.m1Dir.value(0) 
        self.pwm1.duty_u16(int(65535*speed/100))
        self.m2Dir.value(1) 
        self.pwm2.duty_u16(int(65535*speed/100))
        
    def cw_spin(self, speed = 100): 
        self.m1Dir.value(1) 
        self.pwm1.duty_u16(int(65535*speed/100))
        self.m2Dir.value(0) 
        self.pwm2.duty_u16(int(65535*speed/100))
        
    def Actuator_up(self, speed, duration = 1):
        self.m3Dir.value(0) 
        self.pwm3.duty_u16(int(65535*speed/100))
        time.sleep(duration)
        self.pwm3.duty_u16(0)
        
    def Actuator_down(self, speed, duration = 1):
        self.m3Dir.value(1) 
        self.pwm3.duty_u16(int(65535*speed/100))
        time.sleep(duration)
        self.pwm3.duty_u16(0)
        
        
    
    def adjust_direction(self, turn):
        if turn == "left":
            self.m1Dir.value(0) 
            self.pwm1.duty_u16(int(65535*speed/100))
            self.m2Dir.value(0) 			
            self.pwm2.duty_u16(int(65535*(speed*0.8)/100))
        elif turn == "right":
            self.m1Dir.value(0)
            self.pwm1.duty_u16(int(65535*(speed*0.8)/100))
            self.m2Dir.value(0)
            self.pwm2.duty_u16(int(65535*speed/100))
        
        
            
    def damping(self, theta, turn):
        kp=300
        speed2 = speed-kp*theta
        print(speed2)
        if turn == "left":
            self.m1Dir.value(0)
            self.pwm1.duty_u16(int(65535*speed2/100))
            self.m2Dir.value(0) 			
            self.pwm2.duty_u16(int(65535*speed/100))
        elif turn == "right":
            self.m1Dir.value(0)
            self.pwm1.duty_u16(int(65535*speed/100))
            self.m2Dir.value(0)
            self.pwm2.duty_u16(int(65535*speed2/100))
     
        
        