from machine import Pin
from time import sleep,ticks_ms
from MOTOR import Motor



Motor = Motor()
class LineFollowing:
    
    def __init__(self):
        self.left_sensor = Pin(10, Pin.IN)
        self.right_sensor = Pin(11, Pin.IN)
        self.junction1 = Pin(28, Pin.IN)
        self.junction2 = Pin(27, Pin.IN)
        
        self.on_line = False
        self.start_time = 0
        self.end_time = 100
        self.theta = 0
        
       
        self.line_width = 25 #in mm
        self.sensor_spacing = 15
        self.forward_velocity = 100 #mm/s
                     


    def adjust(self, timer, turn): #takes in how long we have been on white line, calculates a reduced speed to send to one of the motors
        theta = 1000*(self.line_width - self.sensor_spacing)/(timer*self.forward_velocity)
        while self.left_sensor.value()!=1 or self.right_sensor.value() !=1:
            Motor.adjust_direction(turn)
            
        #print(theta*180/3.14)
        #Motor.damping(theta, turn)
        #sleep(0.5)
            
        
    def Follow_line(self, not_turning = True):
        following = True
        while following == True:
            left_value = self.left_sensor.value()
            right_value = self.right_sensor.value()
            junction1 = self.junction1.value()
            junction2 = self.junction2.value()


            if left_value == 1 and right_value == 1: #Both sensors detect line
               
                if self.on_line == False:
                    self.start_time = ticks_ms()
                self.on_line = True
                Motor.Forward()
                
            elif left_value == 1 and right_value == 0: #therefore off to the right of the line
                if self.on_line == True:
                    self.end_time = ticks_ms()
                self.on_line = False
                
                self.adjust(self.end_time - self.start_time + 1, turn="left")
                
            elif left_value == 0 and right_value == 1:
                if self.on_line == True:
                    self.end_time = ticks_ms()
                self.on_line = False
                self.adjust(self.end_time - self.start_time, turn="right")
                
            if (junction1 or junction2) == 1 and not_turning == True:
                following = False
                Motor.off
                
            sleep(0.1)
        
            
    def turn(self, direction, angle):#
        done = False
        if done ==False:
            
            if direction == "cw":
                Motor.cw_spin(50)
                sleep(0.005 * angle)
                left_value = self.left_sensor.value()
                right_value = self.right_sensor.value()
                if left_value == 1 or right_value == 1: #Both sensors detect line
                    done = True
                sleep(0.05)
            elif direction == "acw":
                Motor.acw_spin(50)
                sleep(0.005 * angle)
                left_value = self.left_sensor.value()
                right_value = self.right_sensor.value()
                if left_value == 1 or right_value == 1: #Both sensors detect line
                    done = True
                sleep(0.05)
        else:
            self.Follow_line(not_turning = False)
            sleep(2)
        Motor.off()
        
        
    
        