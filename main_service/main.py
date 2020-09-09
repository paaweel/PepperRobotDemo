# from communicator import Communicator
# from games.game import Game

from pepper import Pepper
import time

# import os
# from flask import Flask

#
# from communicator import Communicator
# from games.game import Game

# app = Flask('main_service')

if __name__ == '__main__':
    # app.run(debug=True, port=5000, use_reloader=False)
    print("MAIN SERVICE PRINT")
    p = Pepper()
    data = p.get_raw_audio()
    print(data.text)
    p.get_audio_emotion(data.text)
    # p.save_audio_as_wav()
