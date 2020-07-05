import json
import os
import string
from pepper import Pepper
from games.ultimatum_standard import UltimatumStandard


class Game:
    def __init__(self, path, pepper_player, game_type="ultimatum_standard"):
        # type: (Game, str, Pepper, str) -> None
        self.path = path
        self.pepper_player = pepper_player
        self.language = pepper_player.language
        with open(os.path.join(path, 'games/game_schematics.json'))as f:
            data = json.load(f)
        self.game_schematic = data[game_type]

        with open(os.path.join(path, 'games/games_vocabulary.json'))as f:
            games_vocabulary = json.load(f)
        self.games_vocabulary = games_vocabulary[string.lower(self.language)]

        available_games = {
            "ultimatum_standard": UltimatumStandard,
            "ultimatum_test": UltimatumStandard
        }
        self.game_type = available_games[game_type](self.language, self.pepper_player, self.games_vocabulary)

    def play(self, test_mode=False):
        for step in self.game_schematic:
            finish = getattr(self.game_type, step)(test_mode)
            if finish:
                getattr(self.game_type, 'finish_game')(test_mode)
                break
