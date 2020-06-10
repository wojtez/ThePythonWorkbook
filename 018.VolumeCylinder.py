# The volume of a cylinder can be computed by multiplying the area of its 
# circular base by its height.

# Write a program that reads the radius of the cylinder, along with its 
# height, from the user and computes its volume. Display the result 
# rounded to one decimal place.

from math import pi

r = float(input('Enter radius of the base of cylinder: '))
h = float(input('Enter height of the cylinder: '))

baseArea = pi * (r**2)

print('Area of base cylinder: = %.3f' % baseArea)
print('Volume of the cylinder: = %.1f' % (baseArea * h))