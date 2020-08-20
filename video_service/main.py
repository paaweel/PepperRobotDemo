from flask import Flask
from videoWrapper import VideoWrapper

app = Flask('video_service')

videoWrapper = VideoWrapper()


@app.route('/watch', methods=['GET'])
def watch():
    global videoWrapper
    try:
        frames = videoWrapper.getLastFrames()
        return frames
    except Exception as ex:
        return str(ex)


@app.route('/start', methods=['POST'])
def startwatch():
    global videoWrapper
    try:
        print "Start watching."
        videoWrapper.startThread()
        return "Success"
    except Exception as ex:
        return str(ex)


@app.route('/stop', methods=['POST'])
def stopwatch():
    global videoWrapper
    try:
        print "Stop watching."
        videoWrapper.stopThread()
        return "Success"
    except Exception as ex:
        return str(ex)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=False)
