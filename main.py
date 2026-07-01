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
    waterSensor.init()
    switch.init()

def main():
    while True:
        if docking:
            pass
        else:
            motionSensor.periodic()
            servoMotor.periodic()
            waterSensor.periodic()
            drivetrain.periodic()
            switch.periodic()

if __name__ == "__main__":
    drivetrain.driveCommand = drivetrain.turnLeft
    init()
    main()