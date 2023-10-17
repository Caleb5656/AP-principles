


def calcp(book):


def main():
    try:

        with open("data/prog505a", 'r') as f:
            for line in f:
                ldata = line.split(" ")
                name = ldata[0] + " " + ldata[1]
                books = 





    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()