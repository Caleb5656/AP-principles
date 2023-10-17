import mylibrary
import numpy as np
#from mylibrary import area, perim

arr = np.array([1, 2, 3])
arr2 = np.array([6, 7, 8])
print(arr - arr2)
len = 5
wid = 10
a = mylibrary.area(len, wid)
p = mylibrary.perim(len, wid)

print(f"Area: {a}   Perimeter: {p}")

