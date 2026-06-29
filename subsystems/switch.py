from gpiozero import Button
from signal import pause

button = Button(5)
# Assign the function to the button

print("Waiting for switch press...")
pause()

value = False

def pressed():
    global value
    value = not value
    print("switch pressed!")
    
def init():
    pass
#

def getValue():
    return value

#
def periodic():
    button.when_pressed = pressed
