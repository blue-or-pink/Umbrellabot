# Name: waterSensor.py
# Author: Jay
# Purpose: To detect water (rain) and update its detected value

import smbus
import PCF8591 as ADC 
import time
#
DEVICE_BUS = 1
DEVICE_ADDR = 0x40
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x40, 0x48)
# idk ^^^
ADC.setup(0x48)

#sensor = Button(17, pull_up=True)
#read first few numbers to determine the in and out values
detected = False
def detectWater():
    global detected
    if ADC.read(0) < 27: #63.5:
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
    #time.sleep(0.5)
    #if detected:
       #print("water detected!")

# any output above 200 milivolts = rain
# min = 48
# max = 79
# it goes down when in water!!!

# 3 cold and 63.5 room temp
# lower temp = lower number range
#in water - 40
#out water - 35