import requests
from scipy.io import wavfile
import soundfile as sf

from flask import Flask, request, Response
import qi
from microphone import Microphone

app = Flask('listenservice')
text = ""
session = None
emotion_service = None


def connect(ip="192.168.1.123", port="9559", language="English"):
    # type: (str, str, str) -> None
    global session, emotion_service
    session = qi.Session()
    try:
        session.connect("tcp://" + ip + ":" + port)
        print("Robot connected to LISTEN module.")
    except RuntimeError:
        print("Can't connect to Pepper at ip \""
              + ip + "\" on port " + port + ".\n"
              + "Please check your script arguments. "
              + "Run with -h option for help.")


# TODO accumulate the answer and redirect from console into API response
@app.route('/listen', methods=['GET'])
def listen():
    try:
        with Microphone(session) as stream:
            audio_generator = stream.generator()
            content = [content.tobytes() for content in audio_generator]
            print(content)
            return "content"
    except Exception as ex:
        return str(ex)


@app.route('/start', methods=['POST'])
def start():
    connect()
    return "LISTEN service is running."


if __name__ == '__main__':
    test = False
    if not test:
        connect()
    app.run(debug=True, port=6000, use_reloader=False)
