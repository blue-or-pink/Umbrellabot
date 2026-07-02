# Name: drivetrain.py
# Authors: Jay & Lizz
# Purpose: to contain the commands for running the drivetrain
from motor import MotorController
import time
#=== vars vvv
driveCommand = None



drive = MotorController()
#===
def init():
        global driveCommand
        driveCommand = stop
        drive.set_motor_direction(front_left=0.3,rear_left=0.3,front_right=0.3,rear_right=0.3)
#===
def stop():
      drive.set_motors(front_left=0,rear_left=0,front_right=0,rear_right=0)
#
# add scalar param? vvv

def driveForward():
      drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def driveBackward():
      drive.set_motors(front_left=-1000,rear_left=-1000,front_right=-1000,rear_right=-1000)

def turnRight():
      drive.set_motors(front_left=1000,rear_left=1000,front_right=-1000,rear_right=-1000)

def turnLeft():
     drive.set_motors(front_left=-1000,rear_left=-1000,front_right=1000,rear_right=1000)

def strafeRight():
      drive.set_motors(front_left=-1000,rear_left=1000,front_right=1000,rear_right=-1000)

def strafeLeft():
      drive.set_motors(front_left=1000,rear_left=-1000,front_right=-1000,rear_right=1000)

def driveCustom(fl,rl,fr,rr):
      drive.set_motors(front_left=fl,rear_left=rl,front_right=fr,rear_right=rr)

def getDriveCommand():
      return driveCommand

#

#
def periodic():
    driveCommand()
      