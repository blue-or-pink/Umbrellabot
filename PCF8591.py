# Name: PCF8591.py
# Author: Freenove (github)
# Purpose: to read and write data from and to the ADC for the water sensor
#!/usr/bin/env python3
import smbus
import time

# Standard PCF8591 Module Driver for Starter Kits
class PCF8591:
    def __init__(self, address=0x48):
        self.bus = smbus.SMBus(1)
        self.address = address

    def read(self, channal):
        try:
            if channal == 0:
                self.bus.write_byte(self.address, 0x40)
            elif channal == 1:
                self.bus.write_byte(self.address, 0x41)
            elif channal == 2:
                self.bus.write_byte(self.address, 0x42)
            elif channal == 3:
                self.bus.write_byte(self.address, 0x43)
            self.bus.read_byte(self.address) # Dummy read to clear old data
            return self.bus.read_byte(self.address)
        except Exception as e:
            print(f"Address: {hex(self.address)} Error: {e}")
            return 0

    def write(self, val):
        try:
            self.bus.write_byte_data(self.address, 0x40, int(val))
        except Exception as e:
            print(f"Write Error: {e}")

# Global fallback functions for older kit scripts
def setup(addr):
    global global_pcf
    global_pcf = PCF8591(addr)

def read(chn):
    return global_pcf.read(chn)

def write(val):
    global_pcf.write(val)
