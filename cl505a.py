class books:
    def __init__(self, name, b):
        self.name = name
        self.b = b
        self.points = 0
    def point(self):
        if self.b <= 3:
