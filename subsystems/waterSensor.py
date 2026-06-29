#from gpiozero import Button
import smbus
import PCF8591 as ADC 

#
DEVICE_BUS = 1
DEVICE_ADDR = 0x40
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x40, 0x48)
# idk ^^^
ADC.setup(0x48)

#sensor = Button(17, pull_up=True)


detected = False
def detectWater():
    global detected
    if ADC.read(0) > 84:
        detected = True
    else:
        detected = False

def init():
    pass

def getValue():
    return detected

def periodic():
    print(ADC.read(0))
    detectWater()
    if detected:
        print("water detected!")

# any output above 200 milivolts = rain