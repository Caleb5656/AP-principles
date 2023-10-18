class books:
    def __init__(self, name, b):
        self.name = name
        self.b = b
        self.points = 0
    def point(self):
        if int(self.b) <= 3:
            self.points = self.b * 10
        elif int(self.b) <= 6:
            self.points = (self.b - 3)* 15 + 30
        elif int(self.b) > 6:
            self.points = (self.b-6)*20 + 75
            pass
        pass
