p = float(input("Amount saved: "))
r = float(input("Interest rate: "))/100
n = float(input("Number of days compounded per year: "))
t = float(input("The number of days earning interest: "))

A = p * (1 + (r / n)) ** (n * (t / 365))
print("The amount of interest earned is: ", A)
# ::-1 for inverting string
