from gpiozero import Button
from signal import pause

button = Button(5)
# Assign the function to the button

value = False
# maybe define one as "on" and one as "off"
# but unimportant rn

def pressed():
    global value
    value = not value
    print("switch pressed!")
    
def released():
    global value
    value = not value
    print("switch released!")
    
def init():
    pass
#

def getValue():
    return value

#
def periodic():
    button.when_pressed = pressed
    button.when_released = released
