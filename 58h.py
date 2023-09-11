p = float(input("Amount saved: "))
r = float(input("Interest rate: "))/100
n = float(input("Number of days compounded per year: "))
t = float(input("The number of days earning interest: "))
exp = ((n*t)/365)
A = p * ((1 +(pow((.01* r)/n, exp))))
print("The amount of interest earned is: ", A)
# ::-1 for inverting string
