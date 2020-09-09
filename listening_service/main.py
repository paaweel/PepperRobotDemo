import requests
# from scipy.io import wavfile
# import soundfile as sf
import json

from flask import Flask, request, Response
# from flask_injector import FlaskInjector
# from injector import inject

import qi

from audio_service import AudioService
# from dependencies import configure

app = Flask('listening_service')

service = AudioService()

@app.route('/listen', methods=['GET'])
def listen():
    print("Start listen")
    data = service.listen(5)
    print(str(data))
    return str(data)

if __name__ == '__main__':
    # FlaskInjector(app=app, modules=[configure])
    app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=False)
