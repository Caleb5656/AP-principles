class allsort:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def get_id(self):
        return self.id

    def get_score(self):
        return self.score
