numbers = []
third_largest = []
for i in range(1,10):
    n = float(input(f"Enter the {i}# out of 10: "))
    numbers.append(n)
    if len(numbers) >= 3:
        numbers.sort()
        third_largest.append(numbers[len(numbers)-3])
for i in third_largest:
    print(i)