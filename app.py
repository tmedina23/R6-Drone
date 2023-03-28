import os
from flask import Flask, render_template, Response, request
import cv2
import servos as sv

def get_frame():
    #set video capture device with device number, variables above
    camera = cv2.VideoCapture(0)
    #camera width
    w=640
    #camera height
    h=360
    camera.set(3,w)
    camera.set(4,h)
    camera.set(cv2.CAP_PROP_FPS, 20)

    alpha = 0.3
    beta = 50

    while True:
        ret, frame = camera.read()
        if not ret:
            break
        newFrame = cv2.convertScaleAbs(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), alpha=alpha, beta=beta)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', newFrame)[1].tobytes() + b'\r\n\r\n')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stopall', methods=['GET', 'POST'])
def sa():
        sv.stopAll()
        return render_template('index.html')



@app.route('/forward', methods=['GET', 'POST'])
def f():
	sv.forward()
	return render_template('index.html')

@app.route('/backward', methods=['GET', 'POST'])
def b():
	sv.backward()
	return render_template('index.html')

@app.route('/left', methods=['GET', 'POST'])
def l():
	sv.left()
	return render_template('index.html')

@app.route('/right', methods=['GET', 'POST'])
def r():
        sv.right()
        return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
