import os
import keyboard
from multiprocessing import Process
from games.game import Game
from pepper_modules.pepper import Pepper

if __name__ == "__main__":
    path = os.getcwd()
    # Connect Pepper and start independent processes for listening and watching.
    pepper = Pepper(path)
    pepper.connect()
    pepper_listen_process = Process(target=pepper.open_listen)
    pepper_watch_process = Process(target=pepper.open_watch)
    pepper_listen_process.start()
    pepper_watch_process.start()

    # Choose game type and start independent process with it. The game will trigger Pepper's utterance activity.
    game = Game(path, pepper, "ultimatum_test")
    game_process = Process(target=game.play)
    game_process.start()

    # Switch off the game.
    keyboard.wait('esc')
    pepper.close_listen()
    pepper.close_watch()
    game_process.join()
    pepper_watch_process.join()
    pepper_listen_process.join()
