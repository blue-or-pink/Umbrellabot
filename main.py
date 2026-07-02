import subsystems.motionSensor as motionSensor
import subsystems.servoMotor as servoMotor
import subsystems.waterSensor as waterSensor
import subsystems.drivetrain as drivetrain
import subsystems.switch as switch
# Here goes the main robot while loop, the more specific stuff can branch off from here
docking = False

def init():
    drivetrain.init()
    motionSensor.init()
    servoMotor.init()
    #waterSensor.init()
    switch.init()

def main():
    while True:
        if docking:
            drivetrain.stop()
            switch.periodic()
        else:
            #print("not docking")
            motionSensor.periodic()
            servoMotor.periodic()
            #waterSensor.periodic()
            drivetrain.periodic()
            switch.periodic()

if __name__ == "__main__":
    init()
    main()

# NOTE: get plastic cup & lid to made sure water doesnt get onto the board
# or for the showcase, just have a cup not on the robot that you can dip the water sensor into :)
# ^^^ i like that one because it gets rid of any way water could get on the robot

# TODO List:
# - cup problem
# - make new umbrella
# - mount new umbrella
# - test motion following more