class search:
    def __init__(self, array, item):
        self.item = item
        self.array = array

    def LinearSearch(self):
        for i in range(0, len(self.array) - 1):

            if self.array[i] == self.item:
                return i

        return -1

    def BinarySearch(self, key):

        low = 0
        high = len(self.array) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if self.array[mid] == key:
                return mid
            elif self.array[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

        return -1
