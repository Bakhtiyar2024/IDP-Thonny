from machine import Pin, PWM


speed=100
r2 = 1
r1 = 0.9

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
        
    def off(self): 
        self.pwm1.duty_u16(0)
        self.pwm2.duty_u16(0)
        
    def Reverse(self): 
        self.m1Dir.value(1)                     # forward = 0 reverse = 1 motor 1 
        self.pwm1.duty_u16(int(65535*40*r1/100))
        self.m2Dir.value(1)                     # forward = 0 reverse = 1 motor 1 
        self.pwm2.duty_u16(int(65535*40*r2/100))
        # speed range 0-100 motor 1
        
    def Forward(self): 
        self.m1Dir.value(0) 
        self.pwm1.duty_u16(int(65535*speed*r1/100))
        self.m2Dir.value(0) 			
        self.pwm2.duty_u16(int(65535*speed*r2/100))
        
    def acw_spin(self, speed): 
        self.m1Dir.value(0) 
        self.pwm1.duty_u16(int(65535*speed*r1/100))
        self.m2Dir.value(1) 
        self.pwm2.duty_u16(int(65535*speed*r2/100))
        
    def cw_spin(self, speed): 
        self.m1Dir.value(1) 
        self.pwm1.duty_u16(int(65535*speed*r1/100))
        self.m2Dir.value(0) 
        self.pwm2.duty_u16(int(65535*speed*r2/100))
        
    
    def adjust_direction(self, turn):
        if turn == "left":
            self.m1Dir.value(0) 
            self.pwm1.duty_u16(int(65535*speed*r1/100))
            self.m2Dir.value(0) 			
            self.pwm2.duty_u16(int(65535*(speed*r2*0.85)/100))
        elif turn == "right":
            self.m1Dir.value(0)
            self.pwm1.duty_u16(int(65535*(speed*r1*0.85)/100))
            self.m2Dir.value(0)
            self.pwm2.duty_u16(int(65535*speed*r2/100))
            
    
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