import enum
import json
import os
from communicator import Communicator
from games.ultimatum_standard import UltimatumStandard


class GameTypes(enum.Enum):
    UltimatumStandard = 1
    UltimatumTest = 2


# change to abstract class which is implemented by Ultimatum*
# and use Enums only when you are sure they will not create bugs
class Game:
    def __init__(self, path, communicator, game_type="ultimatum_standard"):
        # type: (Game, str, Communicator, str) -> None
        self.path = path
        self.communicator = communicator
        self.language = communicator.language
        with open(os.path.join(path, 'games/game_schematics.json'))as f:
            data = json.load(f)
        self.game_schematic = data[game_type]

        with open(os.path.join(path, 'games/games_vocabulary.json'))as f:
            games_vocabulary = json.load(f)
        self.games_vocabulary = games_vocabulary[self.language.lower()]

        available_games = {
            "ultimatum_standard": UltimatumStandard,
            "ultimatum_test": UltimatumStandard
        }
        self.game_type = available_games[game_type](self.language, self.communicator, self.games_vocabulary)

    def play(self, test_mode=False):
        for step in self.game_schematic:
            finish = getattr(self.game_type, step)(test_mode)
            if finish:
                getattr(self.game_type, 'finish_game')(test_mode)
                break
