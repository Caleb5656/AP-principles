
#Inventory Manager: Keep track of stock levels, sales, and reorders.
def main():
    count = []
    items = []
    while input != "quit":
        task = input("'Add' to put into inventory tracking or 'sales' to input a purchase from a customer or 'inventory' to print out the inventory 'done' to end task: ").lower()
        if task == "add":
            while input() != "done":
                item = input("Enter the item to be kept track of: ")
                items.append(item)
                num = int(input("Enter the amount of the item to be kept: "))
                count.append(num)
        if task == "sales":
            while input != "done":
                print()
        if task == "inventory":
            for l in range (0, len(items)):
                print("Item: ", items[l], " count: ", count[l])

if __name__ == "__main__":
    main()