import os
import unittest
from games.game import Game
from pepper import Pepper


class GameTest(unittest.TestCase):
    def setUp(self):
        test_path = os.getcwd()
        main_path = os.path.dirname(test_path)
        pepper = Pepper(main_path, "192.168.1.123", "9559", 'English', True)
        self.sut = Game(main_path, pepper, "ultimatum_standard")

    def test_image_capture(self):
        self.sut.play(True)


if __name__ == '__main__':
    unittest.main()
