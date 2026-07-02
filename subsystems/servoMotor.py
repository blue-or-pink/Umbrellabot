# Name: servoMotor.py
# Author: Jay
# Purpose: to get the value of the water sensor, and extend the umbrella if water is detected
# by changing the PWM signal given to the servo
import time
import subsystems.waterSensor as waterSensor
from pca9685 import PCA9685

# Servo class copied from Freenove github, defines the servo communication & signal sending
class Servo:
    def __init__(self):
        self.pwm_frequency = 50
        self.initial_pulse = 1500
        self.pwm_channel_map = {
            '0': 8,
            '1': 9,
            '2': 10,
            '3': 11,
            '4': 12,
            '5': 13,
            '6': 14,
            '7': 15
        }
        self.pwm_servo = PCA9685(0x40, debug=True)
        self.pwm_servo.set_pwm_freq(self.pwm_frequency)
        for channel in self.pwm_channel_map.values():
            self.pwm_servo.set_servo_pulse(channel, self.initial_pulse)

    def set_servo_pwm(self, channel: str, angle: int, error: int = 10) -> None:
        angle = int(angle)
        if channel not in self.pwm_channel_map:
            raise ValueError(f"Invalid channel: {channel}. Valid channels are {list(self.pwm_channel_map.keys())}.")
        pulse = 2500 - int((angle + error) / 0.09) if channel == '0' else 500 + int((angle + error) / 0.09)
        self.pwm_servo.set_servo_pulse(self.pwm_channel_map[channel], pulse)

pwm_servo = Servo()

def init():
    pass

# NOTE: maybe it's better to only send signal to servo
# when the value changes rather than constantly?
# consider later
def periodic():
    if waterSensor.getValue():
        pwm_servo.set_servo_pwm('2', 90)
        #print("90")
    else:
        pwm_servo.set_servo_pwm('2', 0)
        #print("0")
