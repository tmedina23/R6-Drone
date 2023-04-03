import os
from adafruit_servokit import *
from time import *

kit = ServoKit(channels=16)

leftsv = kit.continuous_servo[1]
rightsv = kit.continuous_servo[0]

leftsv.throttle = 0
rightsv.throttle = 0

clockwise = 0.5
counterclockwise = -0.5

def test(servo_num):
    kit.continuous_servo[servo_num].throttle = counterclockwise
    sleep(1)
    kit.continuous_servo[servo_num].throttle = clockwise
    sleep(1)
    kit.continuous_servo[servo_num].throttle = 0

def stopAll():
    leftsv.throttle = 0
    rightsv.throttle = 0


def forward():
    leftsv.throttle = -0.5
    rightsv.throttle = 0.5

def backward():
    leftsv.throttle = 0.5
    rightsv.throttle = -0.5

def left():
    leftsv.throttle = 0.5
    rightsv.throttle = 0.5

def right():
    leftsv.throttle = -0.5
    rightsv.throttle = -0.5