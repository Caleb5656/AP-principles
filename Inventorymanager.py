# Inventory Manager: Keep track of stock levels, sales, and reorders.
def restock(item, amt, tcount, titems):
    loc = titems.index(item)
    tcount[loc] = tcount[loc] + int(amt)
    return tcount


def main():
    count = []
    items = []
    prices = []
    profit = 0.0
    while input != "quit":

        task = input("'Add' to put into inventory tracking or "
                     "'sales' to input a purchase from a customer or "
                     "'inventory' to print out the inventory or 'restock' to increase amount in inventory "
                     "'done' to end task and 'quit' to end inventory management: ").lower()
        if task == "quit": break

        if task == "add":

            while task == "add":

                item = input("Enter the item to be kept track of: ").lower().capitalize()

                if item == "Done":
                    task = ""
                    break
                items.append(item)
                num = int(input("Enter the amount of the item to be kept: "))
                count.append(num)
                cost = float(input("Enter the cost of the item being added: "))
                prices.append(cost)

        if task == "sales":

            while input != "done":
                sale = input("Enter the item: ").lower().capitalize()

                if sale == "Done":
                    break
                if items.__contains__(sale):
                    loc = items.index(sale)
                    sold = int(input("Enter the amount of the item to be sold: "))

                    if count[loc] - sold < 0:
                        print("Sale cannot be completed not enough stock")

                    else:
                        count[loc] = count[loc] - sold
                        profit += prices[loc] * sold
                else:
                    print("Item not contained in inventory please try again: ")

        if task == "inventory":
            for l in range(0, len(items)):
                print("Item: ", items[l], " count: ", count[l])

        if task == "restock":
            while input != "done":

                Titem = input("Enter the item to be restocked: ").lower().capitalize()
                if Titem == "Done": break
                if items.__contains__(Titem):
                    s = input("Enter the amount being added: ")
                    bcount = restock(Titem, s, count, items)
                else:
                    print("Item not contained in inventory try again: ")


if __name__ == "__main__":
    main()
