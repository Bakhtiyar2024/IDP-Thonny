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
        # Attach interrupt to button press (falling edge, active-low)
        sleep(1)
        Start_Button.button.irq(trigger=machine.Pin.IRQ_FALLING, handler=Start_Button.restart_script)
        LinearActuatorSetup()
        Motor.Forward()
        sleep(2)
        navigation(location_routes_from_start["Depot1"])
        depot1 = True
        boxes_from1 = 0

        while depot1 == True:
            next1 = box_pickup(boxes_from1)
            navigation(location_routes_from_depot_1[next1])
            sleep(0.5)
            box_drop_off()
            navigation(location_routes_to_depot_1[next1])
            boxes_from1 += 1
            if boxes_from1 > 3:
                LF.turn("cw", 90)
                Motor.Forward()
                LF.Follow_line2(2, 100)
                navigation(["lf"])
                LF.Follow_line2(4, 100)
                depot1 = False
            
        navigation(location_routes_to_start[next1])  
        Motor.off()
    sleep(0.1)





        
    

