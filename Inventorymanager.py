# Inventory Manager: Keep track of stock levels, sales, and reorders.
def restock(item, amt, tcount, titems):
    loc = titems.index(item)
    tcount[loc] = tcount[loc] + int(amt)
    return tcount


def inventory(l1, l2):
    for l in range(0, len(l1)):
        print("Item: ", l1[l], " count: ", l2[l])


def main():
    count = []
    items = []
    solds = []
    while input != "quit":

        task = input("'Add' to put into inventory tracking or "
                     "'sales' to input a purchase from a customer or "
                     "'inventory' to print out the inventory or 'restock' "
                     "to increase amount in inventory, 'remove' to get rid of something in inventory "
                     "'done' to end task and 'quit' to end inventory management: ").lower()
        if task == "quit":
            break

        while task == "add":

            item = input("Enter the item to be kept track of: ").lower().capitalize()

            if item == "Done":
                task = ""
                break
            items.append(item)
            num = int(input("Enter the amount of the item to be kept: "))
            count.append(num)
        while task == "remove":

            rItem = input("Enter the item to be removed: ").lower().capitalize()
            if rItem == "Done":
                task = ""
                break
            if items.index(rItem) == -1:
                print("item not found")
            else:
                loc = items.index(rItem)
                items.remove(rItem)
                count.remove(count[loc])
        while task == "sales":
            sale = input("Enter the item: ").lower().capitalize()

            if sale == "Done":
                task = ""
                break
            if items.__contains__(sale):
                loc = items.index(sale)
                sold = int(input("Enter the amount of the item to be sold: "))

                if count[loc] - sold < 0:
                    print("Sale cannot be completed not enough stock")

                else:
                    count[loc] = count[loc] - sold
                    solds.append(items[loc] + " " + str(sale))
            else:
                print("Item not contained in inventory please try again: ")

        if task == "inventory":
            inventory(items, count)

        while task == "restock":

            Titem = input("Enter the item to be restocked: ").lower().capitalize()
            if Titem == "Done": break
            if items.__contains__(Titem):
                s = input("Enter the amount being added: ")
                bcount = restock(Titem, s, count, items)
            else:
                print("Item not contained in inventory try again: ")


if __name__ == "__main__":
    main()
