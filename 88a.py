n1 = int(input("Number 1-13: "))
n2 = int(input("Number 2-20: "))
sum = n1 + n2
dif = n1 - n2
prod = n1 * n2
avg = sum/2
abso = abs(dif)
if n1 > n2:
    max = n1
    min = n2
else:
    max = n2
    min = n1

print("The original numbers are ", n1, " and ", n2)
print("sum: ", sum)
print("Difference: ", dif)
print("Product: ", prod)
print("average: ", avg)
print("Absolute value: ",abso)
print("Max: ", max)
print("Min: ", min)
# Number 1-13: 13
# Number 2-20: 20
# The original numbers are  13  and  20
# sum:  33
# Difference:  -7
# Product:  260
# average:  16.5
# Absolute value:  7
# Max:  20
# Min:  13
