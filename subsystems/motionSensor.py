import subsystems.drivetrain as drivetrain 
import time
#import machine
#pir_pin = machine.pin(6, machine.Pin.IN)
from gpiozero import MotionSensor


# Initialize the sensor connected to GPIO 4 (Physical Pin 7)
pir = MotionSensor(6)
detected = False
"""
dir = True // true = left, right = false
timer = 0
def motiondect():
    global detected
    if pir.motion_detected:
        detected = True
        drivetrain.driveCommand = drivetrain.driveForward
    else:
        detected = False
        if timer >= 2000 or timer = 0:
            if dir:
                drivetrain.driveCommand = drivetrain.turnLeft
            else:
                drivetrain.driveCommand = drivetrain.turnRight

        if timer >= 2000:
            dir = not dir
            timer = 0
        
        timer += 1
    
"""

dir = True #True = left, right = False 
timer = 0 
def motiondect():
    global detected
    global timer
    global dir
    if pir.motion_detected:
        detected = True
        drivetrain.drivecommand = drivetrain.driveForward()
#drive forward then check surrroundings  
    else:
        detected = False 
        if timer >= 2000 or timer == 0:
            if dir:
                drivetrain.drivecommand = drivetrain.turnLeft()
            else:
                drivetrain.drivecommand = drivetrain.turnRight()
        if timer >= 2000:
            dir = not dir 
            timer = 0
        timer += 1 
       
"""while True:
    should_B = motiondect()
    if should_B: 
        break
    time.sleep(0.1)
"""

#recall the function 
        

def followMotion():
    pass
# to tell drivetrain to do something, 
# use drivetrain.driveCommand = drivetrain.driveForward (etc. - check the functions in drivetrain.py)

def init():
    pass

def periodic():
    motiondect()
    
    