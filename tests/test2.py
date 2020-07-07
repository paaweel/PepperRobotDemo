import os
from pepper import Pepper
import time


if __name__ == '__main__':
    test_path = os.getcwd()
    main_path = os.path.dirname(test_path)
    pepper = Pepper(main_path, "192.168.1.123", "9559", 'English', True)
    pepper.connect()
    pepper.say("Welcome")
    time.sleep(2000)
