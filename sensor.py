####################################################################
# This program takes input from a PIR sensor and determines if the 
# room the sensor is placed in is occupied or not. 
####################################################################

from gpiozero import MotionSensor

pir = MotionSensor(4)
while True:
    if pir.is_active:
        print("working")
    


    