import enum
import json
import os
from communicator import Communicator
from games.ultimatum_standard import UltimatumStandard


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
        self.game_type = available_games[game_type](self.language,
                                                    self.communicator,
                                                    self.games_vocabulary,
                                                    self.decisionModule)

    def play(self, test_mode=False):
        for generalStep, iterations in self.game_schematic["structure"]:
            for i in range(iterations):
                for step in self.game_schematic[generalStep]:
                    finish = getattr(self.game_type, step)(test_mode)
                    if step=="ask_to_play" and finish:
                        getattr(self.game_type, 'finish_game')(test_mode)
                        return
