import os

from pepper import Pepper

if __name__ == "__main__":
    pepper = Pepper(os.getcwd())
    pepper.connect()
    pepper.say("Hello")
