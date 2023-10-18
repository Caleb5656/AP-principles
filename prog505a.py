import cl505a
from cl505a import books

def win(arr):
    arr = []
    win = ""
    w = 0
    for b in arr:
        if b.points > w:
            win = b.name
            w = b.point
            pass
        pass
    return win


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
            for b in book:
                b.point()
                avg += b.points

            avg /= len(book)
            winner = win(book)
            print()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()