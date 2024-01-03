class sort:
    def __init__(self, other):
        self.other = other
    def bubble(self):
        for i in range(0, len(self.other) - 1):
            for j in range(0, len(self.other) - i - 1):
                if self.other[j] > self.other[j + 1]:
                    temp = self.other[j]
                    self.other[j] = self.other[j + 1]
                    self.other[j + 1] = temp
        return self.other
