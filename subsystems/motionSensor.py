# Name: motionSensor.py
# Authors: Lizz & Jay
# Purpose: to detect motion using heat sensing & to follow it by 
# requesting different commands of the drivetrain
import subsystems.drivetrain as drivetrain 
#import time
#import machine
#pir_pin = machine.pin(6, machine.Pin.IN)
from gpiozero import MotionSensor

# Initialize the sensor connected to GPIO 4 (Physical Pin 7)
pir = MotionSensor(6)
detected = False
dir = True #True = left, right = False 
timer = 0 
def motiondect():
    global detected
    global timer
    global dir
    if pir.motion_detected:
        detected = True
        drivetrain.driveCommand = drivetrain.driveForward
#drive forward then check surrroundings  
    else:
        timer += 1
        #print(timer)
        # test change
        detected = False 
        if timer >= 85:
            print("timer reset")
            dir = not dir 
            timer = 0
        
        if timer == 0:
            if dir:
                drivetrain.driveCommand = drivetrain.turnLeft
            else:
                drivetrain.driveCommand = drivetrain.turnRight

# to tell drivetrain to do something, 
# use drivetrain.driveCommand = drivetrain.driveForward (etc. - check the functions in drivetrain.py)

def init():
    pass

def periodic():
    #pass
    motiondect()
    
    