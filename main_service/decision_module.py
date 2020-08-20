class DecisionModule:
    def __init__(self, games_vocabulary):
        self.games_vocabulary = games_vocabulary
        self.offers = []
        self.decisions = []

    def push_answer_int(self, str_num):
        try:
            int_num = int(str_num)
            self.offers.append(int_num)
        except ValueError:
            return

    def get_last_int(self):
        if self.offers:
            return self.offers[-1]

    def push_answer_bool(self, str_bool):
        try:
            if any(option == str_bool for option in self.games_vocabulary["yes"]):
                self.decisions.append(True)
                return
            if any(option == str_bool for option in self.games_vocabulary["no"]):
                self.decisions.append(False)
                return
        except ValueError:
            return

    def get_last_bool(self):
        if self.decisions:
            return self.decisions[-1]
