import os
from adafruit_servokit import *
from time import *

kit = ServoKit(channels=16)

def test(servo_num):
        kit.continuous_servo[servo_num].throttle = -0.5
        sleep(1)
        kit.continuous_servo[servo_num].throttle = 0.5
        sleep(1)
        kit.continuous_servo[servo_num].throttle = 0

def stopAll():
        kit.continuous_servo[2].throttle = 0
        kit.continuous_servo[1].throttle = 0

def left1(servo_num):
        kit.continuous_servo[servo_num].throttle = 0.5

left1(1)
sleep(5)
stopAll()
