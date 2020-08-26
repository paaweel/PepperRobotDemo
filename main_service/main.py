import os
from flask import Flask

from communicator import Communicator
from games.game import Game

# app = Flask('main_service')

if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=False)
    communicator = Communicator()
    path = os.getcwd()
    game = Game(path, communicator)
    game.play()
