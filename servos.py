import os
from adafruit_servokit import *
from time import *

kit = ServoKit(channels=16)

left = kit.continuous_servo[1]
right = kit.continuous_servo[0]

left.throttle = 0
right.throttle = 0

def test(servo_num):
        kit.continuous_servo[servo_num].throttle = -0.5
        sleep(1)
        kit.continuous_servo[servo_num].throttle = 0.5
        sleep(1)
        kit.continuous_servo[servo_num].throttle = 0

def stopAll():
        left.throttle = 0
        right.throttle = 0

def left1():
        left.throttle = 0.5

left1()
sleep(3)
stopAll()