####################################################################
# This program takes input from a PIR sensor and determines if the 
# room the sensor is placed in is occupied or not. If the sensor does 
# not detect motion in 5 minutes it will mark the room as availible.
####################################################################

import RPi.GPIO as GPIO
import time
from requests import post
import socket

# set up the GPIO pins
GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 4
CHECK_TIME = 300
DEBUG = False
GPIO.setup(SENSOR_PIN, GPIO.IN)
HOST = f"{socket.gethostname()}"

# set the room status
occupied = False

# A function that will check if the sensor was triggered
def motion_detected():
    return GPIO.input(SENSOR_PIN) == GPIO.HIGH

# a function that updates the room status
def update_room_status():
    global occupied
    if motion_detected():
        occupied = True
        if DEBUG:
            print("Room occupied")
    else:
        occupied = False
        if DEBUG:
            print("Room available")
    post("http://study-room-status.local:5000/update-room", json={"room": HOST, "status":occupied})

# Loop forever, checking the sensor every second
def runProgram():
    global occupied
    try:
        while True:
            update_room_status()
            time.sleep(1)

            # If the room was occupied and motion was not detected for 5 minutes, mark it was available
            if not motion_detected() and occupied:
                time_since_motion = 0
                while time_since_motion < CHECK_TIME:
                    time.sleep(1)
                    time_since_motion += 1
                    if DEBUG:
                        print(time_since_motion)
                    if motion_detected():
                        break
                else:
                    occupied = False
                    if DEBUG:
                        print("Room available")    

    except ConnectionRefusedError:
        pass

while True:
    runProgram()