import motionSensor
import servo
import waterSensor
import drive
# Here goes the main robot while loop, the more specific stuff can branch off from here
docking = False

def main():
    while True:
        if docking:
            pass
        else:
            motionSensor.periodic()
            servo.periodic()
            waterSensor.periodic()
            drive.periodic()

if __name__ == "__main__":
    main()