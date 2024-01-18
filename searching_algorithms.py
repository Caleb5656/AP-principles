# class search:
#     def __init__(self, array, item):
#         self.item = item
#         self.array = array

def LinearSearch(data, key):
    for i in range(0, len(data) - 1):

        if data[i] == key:
            return i

    return -1


def BinarySearch(data, key):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if data[mid] == key:
            return mid
        elif data[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
