import subsystems.drivetrain as drivetrain 
import time 
#import machine
#pir_pin = machine.pin(6, machine.Pin.IN)
from gpiozero import MotionSensor
import subsystems.waterSensor as waterSensor

# Initialize the sensor connected to GPIO 4 (Physical Pin 7)
pir = MotionSensor(6)
detected = False

def motiondect():
    global detected
    if pir.motion_detected:
        detected = True
        drivetrain.driveForward()
            
#drive forward then check surrroundings  
    else:
        detected = False
        drivetrain.turnLeft()
        drivetrain.turnRight()
motiondect()    
#recall the function 
        

def followMotion():
    pass
# to tell drivetrain to do something, 
# use drivetrain.driveCommand = drivetrain.driveForward (etc. - check the functions in drivetrain.py)

def init():
    pass

def periodic():
    motiondect()
    
    