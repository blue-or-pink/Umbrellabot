import time
import subsystems.waterSensor as waterSensor
from gpiozero import Servo

pwm = Servo()  # default is 0? so no param

def init():
    pass
# problem: the second it doesnt detect water it'll go down,
# TODO: deal w that later
def periodic():
    if True:#waterSensor.getValue():
        pwm.setServoAngle(0, 90)
    else:
        pwm.setServoAngle(0, 0) 