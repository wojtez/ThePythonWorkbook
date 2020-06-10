# Write a program that begins by reading a radius, r , from the user. The 
# program will continue by computing and displaying the area of a circle 
# with radius r and the volume of a sphere with radius r. Use the pi constant 
# in the math module in your calculations.

# Hint: The area of a circle is computed using the formula area = πr 2. 

# The volume of a sphere is computed using the formula volume = 43πr 3.

from math import pi

r = int(input('Enter the radius of the ring: '))

# Program check the area of circle with radius r
print('Area of the circle with',r,'radius = %.2f' % (pi*(r**2)))

# Program check volume of sphere with radius r
print('Volume of the sphere with',r,'radius = %.2f' % (4/3 * (pi*(r**3))))