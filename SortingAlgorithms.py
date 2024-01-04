class Sort:
    def __init__(self, other):
        self.other = other

    def bubble(self) -> object:
        for i in range(0, len(self.other) - 1):
            for j in range(0, len(self.other) - i - 1):
                if self.other[j] > self.other[j + 1]:
                    temp = self.other[j]
                    self.other[j] = self.other[j + 1]
                    self.other[j + 1] = temp
        return self.other

    def SelectionSort(A):
        for i in range (0,len(A) - 1):
            min_index = i
        for j in range(i,len(A)):
            if A[j] < A[min_index]:
                min_index = j
            Swap
            A[i] and A[min
            index]
            end
            for
                end
                procedure