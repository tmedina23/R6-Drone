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
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_all')
def stop():
        sv.stopAll()
        return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def testroute():
        sv.test(0)
        return render_template('index.html')

@app.route('/left', methods=['GET', 'POST'])
def l():
	sv.left()
	return render_template('index.html')

@app.route('/right', methods=['GET', 'POST'])
def r():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
