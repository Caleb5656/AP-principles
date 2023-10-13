from random import randint
from random import seed


def fillArray():
    theNums = randint(20, 90)

    return theNums


def main():
    nums = []
    for i in range(1, 20):
        nums.append(fillArray())
    print("The original list is: ",nums, "\n")

    print("List with a for each loop is: ")

    for num in nums:
        print(num, end=" ")
    
    
    middle = round(len(nums) / 2) - 1

    print("\n\nThe middle number is: ",nums[middle], "\n")

    avg = (nums[0]+nums[middle]+nums[len(nums) - 1])/3

    print("The average of the first middle and last is: ", avg, "\n")

    min = 100
    max = 0
    for num in nums:
        if num < min: min = num
        if num > max: max = num
    temp = nums.index(max)
    nums[nums.index(min)] = max
    nums[temp] = min
    
    print("min and max switched: ",nums, "\n")
  
    
    nums.insert(middle, randint(1, 10))
    print("The list with number inserted into middle is: ",nums, "\n")
    for num in nums:
      nums[nums.index(num)] = num + 10
    
    print("The array values plus ten is: ",nums, "\n")
    
  
    third = nums[2]
    nums[2] = 5
    print("The third number of the array was: ",third, "\n")

    print("The numbers in the 50's are: ")
    for num in nums:
      if num < 60 and num <= 50: 
        print(num, end=" ")


    print("\n\nThe multiples of four in the list are: ")
    for num in nums:
      if num % 4 == 0:
        print(num, end=" ")


    if 60 in nums:
      print("\n\nThe list contains 60?: ",True, "\n")
    else: print("\n\nThe list contains 60?: ",False, "\n")

    reverseNum = nums[::-1]
    t = True
    for i in range (1, len(nums)):
        if reverseNum[i] != nums[i]: t = False
    print("The list front to back is: ", t, "\n")


    avg = 0
    for num in nums:
      avg += num
    avg /= len(nums)

    nummore = 0
    for num in nums:
      if num > avg: nummore += 1
    print("The amount of numbers more than the average is: ",nummore, "\n")
    numeven = 0
    for num in nums:
      if num % 2 == 0: numeven += 1
    print("Number of even numbers: ",numeven, "\n")
    print("The original list is: ", nums, "\n")
    print("The reversed list is: ",reverseNum, "\n")
    nums.insert(0, nums.pop())
    print("The rotated list is: ",nums)

    tot = 0
    for num in nums:
      tot += num
    print("The total of all the elements is: ", tot)

if __name__ == "__main__":
    main()
# The original list is:  [25, 48, 21, 46, 60, 50, 88, 85, 39, 52, 35, 51, 73, 87, 78, 80, 85, 56, 29]
#
# List with a for each loop is:
# 25 48 21 46 60 50 88 85 39 52 35 51 73 87 78 80 85 56 29
#
# The middle number is:  52
#
# The average of the first middle and last is:  35.333333333333336
#
# min and max switched:  [25, 48, 88, 46, 60, 50, 21, 85, 39, 52, 35, 51, 73, 87, 78, 80, 85, 56, 29]
#
# The list with number inserted into middle is:  [25, 48, 88, 46, 60, 50, 21, 85, 39, 4, 52, 35, 51, 73, 87, 78, 80, 85, 56, 29]
#
# The array values plus ten is:  [45, 58, 98, 66, 70, 60, 31, 95, 49, 14, 62, 35, 61, 83, 97, 88, 90, 95, 56, 39]
#
# The third number of the array was:  98
#
# The numbers in the 50's are:
# 45 5 31 49 14 35 39
#
# The multiples of four in the list are:
# 60 88 56
#
# The list contains 60?:  True
#
# The list front to back is:  False
#
# The amount of numbers more than the average is:  11
#
# Number of even numbers:  9
#
# The original list is:  [45, 58, 5, 66, 70, 60, 31, 95, 49, 14, 62, 35, 61, 83, 97, 88, 90, 95, 56, 39]
#
# The reversed list is:  [39, 56, 95, 90, 88, 97, 83, 61, 35, 62, 14, 49, 95, 31, 60, 70, 66, 5, 58, 45]
#
# The rotated list is:  [39, 45, 58, 5, 66, 70, 60, 31, 95, 49, 14, 62, 35, 61, 83, 97, 88, 90, 95, 56]
# The total of all the elements is:  1199