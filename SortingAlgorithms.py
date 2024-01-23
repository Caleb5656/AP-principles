class Sort:
    def __init__(self, other):
        self.other = other

    def bubble(self):
        for i in range(0, len(self.other) - 1):
            for j in range(0, len(self.other) - i - 1):
                if self.other[j] > self.other[j + 1]:
                    temp = self.other[j]
                    self.other[j] = self.other[j + 1]
                    self.other[j + 1] = temp

    def selection_sort(self):
        for i in range(0, len(self.other) - 1):
            min_index = i
            for j in range(i, len(self.other)):
                if self.other[j] < self.other[min_index]:
                    min_index = j
            temp = self.other[min_index]
            self.other[min_index] = self.other[i]
            self.other[i] = temp

    def insertion_sort(self):
        for i in range(1, len(self.other)):

            key = self.other[i]
            j = i - 1
            while j >= 0 and self.other[j] > key:
                self.other[j + 1] = self.other[j]
                j = j - 1

            self.other[j + 1] = key

