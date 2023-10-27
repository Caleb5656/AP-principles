str1 = input("Enter a string: ")
str2 = input("Enter a second string: ")
doesContain = False

contains = str1.find(str2)
if contains != -1: doesContain = True
print("The first string is contained in the second string: ", doesContain)
# Enter a string: hello
# Enter a second string: lo
# The first string is contained in the second string:  True