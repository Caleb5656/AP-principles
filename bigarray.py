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

    print()
    for num in nums:
        print(num, end=" ")
    
    
    middle = round(len(nums) / 2) - 1

    print("\nThe middle number is: ",nums[middle], "\n")

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
    
    for num in nums:
      if num < 60 and num <= 50: 
        print(num, end=" ")
    print("\n")
  
    for num in nums:
      if num % 4 == 0:
        print(num, end=" ")
    print()

    if 60 in nums:
      print(True)
    else: print(False)

    reverseNum = nums[::-1]
    if reverseNum == nums: print(True)
    else: print(False)
    avg = 0
    for num in nums:
      avg += num
    avg /= len(nums)
    nummore = 0
    for num in nums:
      if num > avg: nummore += 1
    print(nummore)
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
