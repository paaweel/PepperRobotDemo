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

# @inject
@app.route('/listen', methods=['GET'])
def listen(service):
    print("Start listen")
    data = service.listen(2)
    print(str(data))
    return str(data)

if __name__ == '__main__':
    # FlaskInjector(app=app, modules=[configure])
    app.run(debug=True, port=6000, use_reloader=False)
