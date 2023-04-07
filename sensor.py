####################################################################
# This program takes input from a PIR sensor and determines if the 
# room the sensor is placed in is occupied or not. The program will
# send a signal to the main system every 5 minutes to dertermine if
# the room is occupied.
####################################################################

# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(2, GPIO.IN)

# def status():
#     stat = False
#     while True:
#         start_time = time.time()
#         while time.time() < start_time + 600:
#             if status:
#                 return True # This is reached when the sensor detects motion
#             time.sleep(1)
#         return False # This is reached when the room is empty for 10 minutes

from gpiozero import MotionSensor

pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    print("You moved")
    pir.wait_for_no_motion()
    


    