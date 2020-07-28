import requests
from scipy.io import wavfile
import soundfile as sf
import json

from flask import Flask, request, Response
import qi
from pepper_audio import PepperAudioProvider

app = Flask('listenservice')
text = ""
emotion_service = None

PepperAudioProvider = PepperAudioProvider()
PepperAudioProvider.connect()

# TODO accumulate the answer and redirect from console into API response
@app.route('/listen', methods=['GET'])
def listen():
    data = PepperAudioProvider.listen(2)
    return str(data)

if __name__ == '__main__':
    test = False
    if not test:
        PepperAudioProvider.connect()
    app.run(debug=True, port=6000, use_reloader=False)
