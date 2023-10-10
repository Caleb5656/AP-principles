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
# The original list is:  [22, 55, 85, 82, 78, 84, 74, 77, 75, 75, 23, 53, 53, 70, 75, 76, 38, 41, 71]
#
# List with a for each loop is:
# 22 55 85 82 78 84 74 77 75 75 23 53 53 70 75 76 38 41 71
#
# The middle number is:  75
#
# min and max switched:  [85, 55, 22, 82, 78, 84, 74, 77, 75, 75, 23, 53, 53, 70, 75, 76, 38, 41, 71]
#
# The list with number inserted into middle is:  [85, 55, 22, 82, 78, 84, 74, 77, 75, 1, 75, 23, 53, 53, 70, 75, 76, 38, 41, 71]
#
# The array values plus ten is:  [95, 65, 32, 92, 88, 94, 84, 87, 85, 11, 85, 33, 63, 63, 80, 85, 86, 48, 51, 81]
#
# The third number of the array was:  32
#
# The numbers in the 50's are:
# 5 11 33 48
#
# The multiples of four in the list are:
# 92 88 84 80 48
#
# The list contains 60?:  False
#
# The list front to back is:  False
#
# The amount of numbers more than the average is:  12
#
# Number of even numbers:  7
#
# The original list is:  [95, 65, 5, 92, 88, 94, 84, 87, 85, 11, 85, 33, 63, 63, 80, 85, 86, 48, 51, 81]
#
# The reversed list is:  [81, 51, 48, 86, 85, 80, 63, 63, 33, 85, 11, 85, 87, 84, 94, 88, 92, 5, 65, 95]
#
# The rotated list is:  [81, 95, 65, 5, 92, 88, 94, 84, 87, 85, 11, 85, 33, 63, 63, 80, 85, 86, 48, 51]
# The total of all the elements is:  1381