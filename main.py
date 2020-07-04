import os
from games.game import Game
from pepper import Pepper

if __name__ == "__main__":
    path = os.getcwd()
    pepper = Pepper(path)
    pepper.connect()
    game = Game(path, pepper, "ultimatum_test")
    game.play()
