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

LF = LineFollowing()
Motor = Motor()

"""
while True:
    left_value = 0
    right_value = 0
    
    Motor.cw_spin(50)
    sleep(1)
    
    
    done = False
    while done ==False:
        left_value = LF.left_sensor.value()
        right_value = LF.right_sensor.value()
        
        if left_value == 1 and right_value == 1: #Both sensors detect line
            #sleep(0.6)
            done = True
    Motor.off()
    sleep(2)"""
 #   Motor.Reverse()
  #  sleep(0.65)
  #  Motor.off()
   # sleep(2)

LinearActuatorSetup()
#Motor.Forward()
sleep(2)
navigation(location_routes_from_start["Depot1"])
depot1 = True
boxes_from1 = 0
while depot1 == True:
    next1 = box_pickup(boxes_from1)
    navigation(location_routes_from_depot_1[next1])
    sleep(1)
    box_drop_off()
    navigation(location_routes_to_depot_1[next1])
    boxes_from1 += 1
    if boxes_from1 > 3:
        depot1 = False
        
navigation(location_routes_to_depot_2[next1])
depot2 = True
boxes_from2 = 0
while depot2 == True:
    next1 = box_pickup(boxes_from2)
    navigation(location_routes_from_depot_2[next1])
    sleep(1)
    box_drop_off()
    navigation(location_routes_to_depot_1[next1])
    boxes_from1 += 1
    if boxes_from2 > 3:
        depot2 = False

Motor.off()
        
    
