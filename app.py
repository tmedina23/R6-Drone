import os
from flask import Flask, render_template, Response, request
from time import *
import cv2
from adafruit_servokit import *



kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 0

frontleft = kit.continuous_servo[1]
frontright = kit.continuous_servo[0]
rearleft = kit.continuous_servo[2]
rearright = kit.continuous_servo[3]

def test(servo_num):
        kit.continuous_servo[servo_num].throttle = -0.5
        sleep(1)
        kit.continuous_servo[servo_num].throttle = 0.5
        sleep(1)
        kit.continuous_servo[servo_num].throttle = 0

def stopAll():
        frontleft.throttle = 0
        frontright.throttle = 0
        rearleft.throttle = 0
        rearright.throttle = 0

def left():
        frontleft.throttle = -0.5
        rearleft.throttel = -0.5
        frontright.throttle = 0.5
        frontleft.throttle = 0.5

def get_frame():
    #set video capture device with device number, variables above
    camera = cv2.VideoCapture(0)
    #camera width
    w=854
    #camera height
    h=480
    camera.set(3,w)
    camera.set(4,h)
    camera.set(cv2.CAP_PROP_FPS, 20)

    while True:
        ret, frame = camera.read()
        if not ret:
            break
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes() + b'\r\n\r\n')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/video_feed')
def video_feed0():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_all')
def stop():
        stopAll()
        return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def testroute():
        test(0)
        return render_template('index.html')

@app.route('/left', methods=['GET', 'POST'])
def l():
	left()
	return render_template('index.html')

@app.route('/right', methods=['GET', 'POST'])
def r():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
