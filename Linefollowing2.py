from machine import Pin
from time import sleep,ticks_ms
from MOTOR import Motor



Motor = Motor()
class LineFollowing:
    
    def __init__(self):
        self.left_sensor = Pin(22, Pin.IN)
        self.right_sensor = Pin(28, Pin.IN)
        self.junction1 = Pin(27, Pin.IN)
        self.junction2 = Pin(26, Pin.IN)
        
        
            
        
    def Follow_line(self):
        
        junction1 = self.junction1.value()
        junction2 = self.junction2.value()
        
        while (junction1 or junction2) == 0 :
            junction1 = self.junction1.value()
            junction2 = self.junction2.value()
            left_value = self.left_sensor.value()
            right_value = self.right_sensor.value()
            
            if left_value == 1 and right_value == 1: #Both sensors detect line
                Motor.Forward()
                
            elif left_value == 1 and right_value == 0: #therefore off to the right of the line                
                Motor.adjust_direction("left")
                while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1) and ((self.junction1.value() or self.junction2.value()) ==0):
                    sleep(0.01)
                
            elif left_value == 0 and right_value == 1:
                Motor.adjust_direction("right")
                while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1) and ((self.junction1.value() or self.junction2.value()) ==0):
                    sleep(0.01)
                    
            sleep(0.01)
                        
        Motor.off()                                   
                
        sleep(0.01)
        #break
        
         
         
    def turn(self, direction, angle):#
        if direction == "cw":
            Motor.cw_spin(50)
            sleep(0.015 * angle)
                
        elif direction == "acw":
            Motor.acw_spin(50)
            sleep(0.015 * angle)
        
        done = False
        while done ==False:
            left_value = self.left_sensor.value()
            right_value = self.right_sensor.value()
            junction1 = self.junction1.value()
            junction2 = self.junction2.value()
            
            if left_value == 1 or right_value == 1: #Both sensors detect line
                done = True
                sleep(0.2)
            
            if junction1 == 1 or junction2 == 1:
                done = True
                sleep(0.1)
            
                
        
        Motor.Forward()
        sleep(0.5)
        Motor.off()
        #break
        
        
        
        
        
        
        
    def Rev_Follow_line(self):
        
        junction1 = self.junction1.value()
        junction2 = self.junction2.value()
        
        while (junction1 or junction2) == 0 :
            junction1 = self.junction1.value()
            junction2 = self.junction2.value()
            left_value = self.left_sensor.value()
            right_value = self.right_sensor.value()
            
            if left_value == 1 and right_value == 1: #Both sensors detect line
               
                Motor.Reverse(40)
                
            elif left_value == 1 and right_value == 0: #therefore off to the right of the line                
                Motor.rev_adjust_direction("right")
                while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1) and ((self.junction1.value() or self.junction2.value()) ==0):
                    sleep(0.01)
                
            elif left_value == 0 and right_value == 1:
                Motor.rev_adjust_direction("left")
                while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1) and ((self.junction1.value() or self.junction2.value()) ==0):
                    sleep(0.01)
                    
            sleep(0.01)
                        
        Motor.off()                
                            
                
        sleep(0.01)