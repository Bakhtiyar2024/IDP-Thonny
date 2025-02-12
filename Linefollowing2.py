from machine import Pin
from time import sleep,ticks_ms
from MOTOR import Motor
from Infrared_distance_final import get_distance



Motor = Motor()
class LineFollowing:
    
    def __init__(self):
        self.left_sensor = Pin(22, Pin.IN)
        self.right_sensor = Pin(28, Pin.IN)
        self.junction1 = Pin(27, Pin.IN)
        self.junction2 = Pin(26, Pin.IN)
        
        
            
        
    def Follow_line(self): #checks for junctions
        
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
    
    
    
    """
    def Follow_line2(self): #line following without junction detection to get out of depot
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
    """ 
        
        
         
         
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
            
        Motor.off()
        
        
        
        
        
        
    """
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
    """
        
        
        
    def Rev_Follow_line2(self, d):
        while get_distance() > d:
            left_value = self.left_sensor.value()
            right_value = self.right_sensor.value()
            
            if left_value and right_value == 1:
                Motor.Reverse()
                
            elif left_value == 1 and right_value == 0:
                    Motor.adjust_direction("right", speed = 80)
                    while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1):
                        sleep(0.01)
            
            elif right_value == 1 and right_value == 0:
                    Motor.adjust_direction("left", speed = 80)
                    while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1):
                        sleep(0.01)
            """
            else:
                adjustments = 0
                while adjustments < 3:
                    left_value = self.left_sensor.value()
                    right_value = self.right_sensor.value()
                
                    if left_value == 1 and right_value == 0:
                        Motor.adjust_direction("left")
                        while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1):
                            sleep(0.01)
                        adjustments += 1
                    
                    elif right_value == 1 and right_value == 0:
                        Motor.adjust_direction("right")
                        while (self.left_sensor.value()!=1 or self.right_sensor.value() !=1):
                            sleep(0.01)
                        adjustments += 1
            """
                
                
                