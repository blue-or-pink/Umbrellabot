"""import subsystems.drivetrain as drivetrain 
import time 
import machine
pir_pin = machine.pin(6, machine.Pin.IN)

def motiondect():
    try:
        while True:
            if pir_pin.value() == 1:
                print("Motion Detected")
                time.sleep(1)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\Program. stopped.")
"""



# to tell drivetrain to do something, 
# use drivetrain.driveCommand = drivetrain.driveForward (etc. - check the functions in drivetrain.py)

def init():
    pass

def periodic():
    pass

