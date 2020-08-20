import os
import flask from Flask
from communicator import Communicator
from games.game import Game



if __name__ == '__main__':
    path = os.getcwd()
    communicator = Communicator(path=path)
    game = Game(path, communicator)
    game.play()
