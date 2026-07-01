from gpiozero import Button
from signal import pause
import main
import time
button = Button(5)
# Assign the function to the button

value = False
# maybe define one as "on" and one as "off"
# but unimportant rn

def pressed():
    global value
    value = not value
    print("switch pressed!")
    main.docking = not main.docking

    
def released():
    global value
    value = not value
    print("switch released!")
    main.docking = not main.docking
    
def init():
    pass
#

def getValue():
    return value

#
def periodic():
    button.when_pressed = pressed
    button.when_released = released
