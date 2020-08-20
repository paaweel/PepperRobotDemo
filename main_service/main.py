
# from communicator import Communicator
# from games.game import Game

from pepper import Pepper


p = Pepper()

p.say_something()


# if __name__ == '__main__':
#     path = os.getcwd()
#     communicator = Communicator(path=path)
#     game = Game(path, communicator)
#     game.play()
# 
# import os
# from flask import Flask
#
# from communicator import Communicator
# from games.game import Game
#
# app = Flask('main_service')
#
# if __name__ == '__main__':
#     # app.run(debug=True, port=7000, use_reloader=False)
#     path = os.getcwd()
#     communicator = Communicator(path=path)
#     game = Game(path, communicator)
#     game.play()
