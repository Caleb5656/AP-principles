we = int(input("Enter the weight in kilo: "))
l = int(input("enter the length in cm: "))
wi = int(input("Enter the width in cm: "))
h = int(input("Enter the height in cm: "))
s = float(l * wi * h)/100000
if(we > 27 and s > .1):print("Too heavy and too large")

if (we > 27 and s < .1):print("Too heavy")
if(s > .1 and we <= 27):print("Too large")
# Enter the weight in kilo: 32
# enter the length in cm: 10
# Enter the width in cm: 25
# Enter the height in cm: 38
# Too heavy
