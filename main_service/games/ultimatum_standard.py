from communicator import Communicator


class UltimatumStandard:
    def __init__(self, language, communicator, games_vocabulary):
        # type: (str, Communicator, [str]) -> None
        self.language = language
        self.communicator = communicator
        self.vocabulary = games_vocabulary

    def greeting(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["welcome_game"])
        else:
            self.communicator.say(self.vocabulary["welcome_game"])

    def game_description(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["standard_ultimatum_rules"])
        else:
            self.communicator.say(self.vocabulary["standard_ultimatum_rules"])

    def ask_to_play(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["ask_to_play"])
        else:
            self.communicator.say(self.vocabulary["ask_to_play"])

    def finish_game(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["finish_game"])
        else:
            self.communicator.say(self.vocabulary["finish_game"])
