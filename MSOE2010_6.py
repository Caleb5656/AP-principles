n = int(input("Enter the number of vertices for the polygon: "))
x_coord = []
y_coord = []
for i in range(0,n-1):
    x = float(input(f"Enter the x-Coordinate for the vertex #{i+1}"))
    y = float(input(f"Enter the y-Coordinate for the vertex #{i+1}"))
    x_coord.append(x)
    y_coord.append(y)

A=0.0
