num = int(input("Enter the numbe of copies: "))
if(num >0 and num <= 99):
    c = .30
elif (num >= 100 and num <= 499):
    c = .28
elif (num >= 500 and num <= 749):
    c = .27
elif (num >= 750 and num <= 1000):
    c = .26
else:
    c = .25
tot = num * c
print("The total cost of the copies is: ", round(tot, 2))
# Enter the numbe of copies: 1001
# The total cost of the copies is:  250.25
