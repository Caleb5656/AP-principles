p = float(input("Amount saved: "))
r = float(input("Interest rate: "))/100
n = float(input("Number of days compounded per year: "))
t = float(input("The number of days earning interest: "))

A = p * (1 + (r / n)) ** (n * (t / 365))
A = round(A, 2)
print("The amount of interest earned is: ", (A - p))
print("The total amount available in savings is now: ", A)
# ::-1 for inverting string
# Amount saved: 5000
# Interest rate: 11.5
# Number of days compounded per year: 365
# The number of days earning interest: 900
# The amount of interest earned is:  1638.96
# The total amount available in savings is now:  6638.96
