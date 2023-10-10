from random import randint
from random import seed


def fillArray():
    theNums = randint(20, 90)

    return theNums


def main():
    nums = []
    for i in range(1, 20):
        nums.append(fillArray())
    print(nums)

    print()
    for num in nums:
        print(num, end=" ")
    print()
    print()
    middle = round(len(nums) / 2) - 1

    print(nums[middle])

    min = 100
    max = 0
    for num in nums:
        if num < min: min = num
        if num > max: max = num
    temp = nums.index(max)
    nums[nums.index(min)] = max
    nums[temp] = min
    print()
    print(nums)


if __name__ == "__main__":
    main()
