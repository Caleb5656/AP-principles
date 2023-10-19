import cl505a
from cl505a import books
import numpy as np

def win(arr):

    arr.sort()
    return arr[len(arr) - 1]


def main():
    try:
        book = []
        with open("data/prog505a", 'r') as f:
            for line in f:
                ldata = line.split(" ")
                name = ldata[0] + " " + ldata[1]
                books = int(ldata[2])
                hi = cl505a.books(name, books)
                book.append(hi)
            avg = 0
            nums = []
            for b in book:
                b.point()
                avg += b.points
                nums.insert(0, b.points)

            avg /= len(book)

            winner = win(nums)
            for b in book:
                if b.points == winner:
                    winner = b.name
            for b in book:
                print(f"{b.name}   books read: {b.b}   points earned: {b.points}")
            print("The average amount of points earned was: ", avg)
            print("The winner was: ", winner)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
# Sam Summer   books read: 4   points earned: 45
# Linda Lazy   books read: 2   points earned: 20
# Paul Prodder   books read: 5   points earned: 60
# K.C. Master   books read: 8   points earned: 115
# Richie Reader   books read: 6   points earned: 75
# The average amount of points earned was:  63.0
# The winner was:  K.C. Master