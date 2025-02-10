from machine import Pin, PWM
from time import sleep


speed = 100

class LinearActuator: 
    def __init__(self): 
        self.m1Dir = Pin(0 , Pin.OUT)         # set pin left wheel 
        self.pwm1 = PWM(Pin(1))           
        self.pwm1.freq(1000) 
        self.pwm1.duty_u16(0)
        
    def Extend(self): 
        self.m1Dir.value(1)                     # forward = 0 reverse = 1 motor 1 
        self.pwm1.duty_u16(int(65535*100/100))
        #sleep(1)
        #self.pwm1.duty_u16(int(65535*0/100))
        
    def Retract(self ): 
        self.m1Dir.value(0)                     # forward = 0 reverse = 1 motor 1 
        self.pwm1.duty_u16(int(65535*100/100))
        #sleep(1)
        #self.pwm1.duty_u16(int(65535*0/100))
