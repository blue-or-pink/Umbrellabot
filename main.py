import subsystems.motionSensor as motionSensor
import subsystems.servo as servo
import subsystems.waterSensor as waterSensor
import subsystems.drivetrain as drivetrain
import subsystems.switch as switch
# Here goes the main robot while loop, the more specific stuff can branch off from here
docking = False

def init():
    drivetrain.init()
    motionSensor.init()
    servo.init()
    waterSensor.init()
    switch.init

def main():
    while True:
        if docking:
            pass
        else:
            motionSensor.periodic()
            servo.periodic()
            waterSensor.periodic()
            drivetrain.periodic()
            switch.periodic()

if __name__ == "__main__":
    init()
    main()