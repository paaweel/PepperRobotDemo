from communicator import Communicator


class UltimatumStandard:
    def __init__(self, language, communicator, games_vocabulary, decisionModule):
        # type: (str, Communicator, [str]) -> None
        self.language = language
        self.communicator = communicator
        self.vocabulary = games_vocabulary
        self.decisionModule = decisionModule

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

    def get_answer_int(self, test_mode=False):
        if test_mode:
            num = input("Answer and hit ENTER:")
        else:
            num = self.communicator.listen()
        self.decisionModule.push_answer_int(num)

    def get_answer_bool(self, test_mode=False):
        if test_mode:
            yesno = input("Answer and hit ENTER:")
        else:
            yesno = self.communicator.listen()
        self.decisionModule.push_answer_bool(yesno)
        return self.decisionModule.get_last_bool()

    def finish_game(self, test_mode=False):
        if test_mode:
            print(self.vocabulary["finish_game"])
        else:
            self.communicator.say(self.vocabulary["finish_game"])
        return False
