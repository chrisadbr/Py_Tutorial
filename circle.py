# Program to calculate circumference and area of a circle

import math

radius = int(input('Enter radius of a circle: '))

# Calculate the area  of a circle
area = round(math.pi * (radius ** 2), 2)
circumference = round(2 * (math.pi * radius), 2)

# Print area and circumference of a circle
print("Area of a circle: " + str(area))
print("Circumference of a circle: " + str(circumference))