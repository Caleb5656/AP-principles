n = int(input("Enter the number of vertices for the polygon: "))
x_coord = []
y_coord = []
for i in range(0,n-1):
    x = float(input(f"Enter the x-Coordinate for the vertex #{i+1}"))
    y = float(input(f"Enter the y-Coordinate for the vertex #{i+1}"))
    x_coord.append(x)
    y_coord.append(y)

x_coord.append(x_coord[0])
y_coord.append(y_coord[0])

A=0.0
for i in range (0,n-1):
    A +=((x_coord[i]*y_coord[i+1])-(x_coord[i+1]*y_coord[i]))
A = .5*A
print("The area of the polygon is: ", A)