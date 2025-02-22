from time import sleep
from machine import Pin
from Box_pick_up import box_pickup
from Box_drop_off import box_drop_off
#from Start_Button import check_button()
from Navigation2 import navigation
from Location_Routes import location_routes_from_start, reverse_route, location_routes_from_depot_1, location_routes_from_depot_2, location_routes_to_depot_1
from MOTOR import Motor
from Linefollowing import LineFollowing
from LinearActuatorSetup import LinearActuatorSetup
import Start_Button

LF = LineFollowing()
Motor = Motor()

while True:
    if Start_Button.button.value() == True:  
        # Wait 1 second before setting up the interrupt
        sleep(1)
        
        # Attach an interrupt to restart the script on button press (falling edge)
        Start_Button.button.irq(trigger=machine.Pin.IRQ_FALLING, handler=Start_Button.restart_script)
        
        # Initialize the linear actuator
        LinearActuatorSetup()
        
        # Move forward for 2 seconds before starting navigation
        Motor.Forward()
        sleep(2)

        # Navigate from start location to Depot1
        navigation(location_routes_from_start["Depot1"])

        depot1 = True  
        boxes_from1 = 0  

        # Main loop for picking up and dropping off boxes at Depot1
        while depot1:
            # Pick up a box and determine its next destination
            next1 = box_pickup(boxes_from1)
            
            # Navigate to the drop-off location
            navigation(location_routes_from_depot_1[next1])
            sleep(0.5)
            
            # Drop off the box
            box_drop_off()
            
            # Return to Depot1
            navigation(location_routes_to_depot_1[next1])
            
            boxes_from1 += 1
            
            # After 4 boxes, return to start location
            if boxes_from1 > 3:
                LF.turn("cw", 90)
                Motor.Forward()
                LF.Follow_line2(2, 100)
                
                # Perform a left turn and move forward before stopping
                navigation(["lf"])
                LF.Follow_line2(4, 100)
                depot1 = False
        
        # Navigate back to the starting point
        navigation(location_routes_to_start[next1])
        
        # Stop the motor after completing the task
        Motor.off()
    
    sleep(0.1)





        
    

