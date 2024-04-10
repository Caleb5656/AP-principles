reservoir = int(input("Enter the number of ounces of water in the reservoir: "))
cups = []
num = 0
while num!=-1:
    num = int(input("Enter the number of ounces in the cup -1 to end: "))
    if num == -1:
        break
    cups.append(num)
count = 0
oz_used = 0
for i in cups:
    oz_used += 1 + i
    if oz_used > reservoir:
        break
    count += 1
print("The number of cups made before refilling the reservoir was: ", count)

