import requests
from scipy.io import wavfile
import soundfile as sf
import json

from flask import Flask, request, Response
import qi
from pepper_audio import PepperAudioProvider

app = Flask('listening_service')

PepperAudioProvider = PepperAudioProvider()
PepperAudioProvider.connect()

@app.route('/listen', methods=['GET'])
def listen():
    data = PepperAudioProvider.listen(2)
    return str(data)

if __name__ == '__main__':
    test = False
    if not test:
        PepperAudioProvider.connect()
    app.run(debug=True, port=6000, use_reloader=False)
