e = int(input("Enter the number of eggs:" ))
ind = e % 12
e = (e - ind)/12
if (e > 0 and e < 4):
    c = .5
elif (e >=4 and e < 6):
    c = .45
elif (e >=6 and e < 11):
    c = .4
elif (e >= 11):
    c = .35
tot = (e * c) + (ind * (c / 12))
print("The total cost is: ", round(tot, 2))
# Enter the number of eggs:18
# The total cost is:  0.75
