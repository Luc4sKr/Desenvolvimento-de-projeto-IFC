class Score:
    def __init__(self):
        self.__score = 0

    def add_score(self, score=1):
        self.__score += score

    def get_score(self):
        return self.__score

