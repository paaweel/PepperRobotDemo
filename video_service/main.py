from flask import Flask
from videoWrapper import VideoWrapper

app = Flask('video_service')

videoWrapper = VideoWrapper()


@app.route('/video', methods=['GET'])
def watch():
    try:
        frames = videoWrapper.getLastFrames()
        return "Success"
    except Exception as ex:
        return str(ex)


@app.route('/start', methods=['POST'])
def startwatch():
    try:
        videoWrapper.stopThread()
    finally:
        try:
            videoWrapper.startThread()
            return "Success"
        except Exception as ex:
            return str(ex)


@app.route('/stop', methods=['POST'])
def stopwatch():
    try:
        videoWrapper.stopThread()
        return "Success"
    except Exception as ex:
        return str(ex)


if __name__ == '__main__':
    app.run(debug=True, port=9000, use_reloader=False)
