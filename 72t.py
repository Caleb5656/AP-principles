t1 = int(input("enter the first time: "))
t2 = int(input("Enter the second time: "))
dif = 0
if t2 > t1:
    dif = t2 - t1
    h = dif/100
    min = dif%100
else:
    dif = t1 - t2
    h = dif/100
    min = dif%100
print(int(h), "Hours", min, "Minutes")
# enter the first time: 1730
# Enter the second time: 900
# 8 Hours 30 Minutes
# enter the first time: 900
# Enter the second time: 1730
# 8 Hours 30 Minutes
