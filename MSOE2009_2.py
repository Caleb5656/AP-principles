import math

lon_per = (float(input("Enter your current longitude: "))*(math.pi/180))
lat_per = (float(input("Enter your current latitude: "))*(math.pi/180))

lon_car = (float(input("Enter your car's current longitude: "))*(math.pi/180))
lat_car = (float(input("Enter your car's current latitude: "))*(math.pi/180))

r = 3963.1
d = r*math.acos((math.cos(lat_car)*math.cos(lon_car)*math.cos(lat_per)*math.cos(lon_per)) + (math.cos(lat_car)*math.sin(lon_car)*math.cos(lat_per)*math.sin(lon_per)) + (math.sin(lat_car)*math.sin(lat_per)))

print("The distance to your car is: ",round(d,3),"miles")

# Enter your current longitude: -87.905
# Enter your current latitude: 43.043
# Enter your car's current longitude: -87.918
# Enter your car's current latitude: 43.045
# The distance to your car is:  0.672 miles