import os
import unittest
from games.game import Game
from pepper import Pepper


class GameTest(unittest.TestCase):
    def setUp(self):
        test_path = os.getcwd()
        main_path = os.path.dirname(test_path)
        pepper = Pepper(main_path)
        self.sut = Game(main_path, pepper, "ultimatum_test")

    def test_image_capture(self):
        self.sut.play(True)


if __name__ == '__main__':
    unittest.main()
