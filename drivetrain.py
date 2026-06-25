from motor import MotorController
import time

drive = MotorController()

drive.set_motor_direction(front_left=1,rear_left=1,front_right=1,rear_right=1)

for i in range (0,4) :
        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)
        time.sleep(1.5)
        drive.set_motors(front_left=1000,rear_left=1000,front_right=-1000,rear_right=-1000)
        time.sleep(0.4)
drive.set_motors(front_left=0,rear_left=0,front_right=0,rear_right=0)

def driveForward():
      drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def driveBackward():
      drive.set_motors(front_left=-1000,rear_left=-1000,front_right=-1000,rear_right=-1000)

def driveBackward():
      drive.set_motors(front_left=-1000,rear_left=-1000,front_right=-1000,rear_right=-1000)

def periodic():
    pass