class UltimatumStandard:
    def __init__(self, language, pepper_player, games_vocabulary):
        self.language = language
        self.pepper_player = pepper_player
        self.vocabulary = games_vocabulary

    def greeting(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["welcome_game"])
        else:
            self.pepper_player.say(self.vocabulary["welcome_game"])

    def game_description(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["standard_ultimatum_rules"])
        else:
            self.pepper_player.say(self.vocabulary["standard_ultimatum_rules"])

    def ask_to_play(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["ask_to_play"])
        else:
            self.pepper_player.say(self.vocabulary["ask_to_play"])
