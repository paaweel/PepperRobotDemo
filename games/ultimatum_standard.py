from pepper import Pepper


class UltimatumStandard:
    def __init__(self, language, pepper_player, games_vocabulary):
        # type: (str, Pepper, [str]) -> None
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

    def get_answer_ask_to_play(self, test_mode=False):
        if test_mode:
            answer = raw_input("Answer by typing and hit ENTER to confirm.")
        else:
            answer = self.pepper_player.listen_buf.pop(-1)
        if answer in self.vocabulary['yes']:
            print('Start the game.')
        else:
            if answer in self.vocabulary['no']:
                print('Thank and finish the game.')
                return True
            else:
                if test_mode:
                    print(self.vocabulary['unrecognised_speech'])
                else:
                    self.pepper_player.say(self.vocabulary['unrecognised_speech'])

    def finish_game(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["finish_game"])
        else:
            self.pepper_player.say(self.vocabulary["finish_game"])
