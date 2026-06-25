from gpiozero import Button
#
sensor = Button(16, pull_up=True)
detected = False
def waterDetected():
    detected = True
def waterNotDetected():
    detected = False

def init():
    pass

def getValue():
    return detected

def periodic():
    sensor.when_pressed = waterDetected
    sensor.when_released = waterNotDetected
    if detected:
        print("water detected!")