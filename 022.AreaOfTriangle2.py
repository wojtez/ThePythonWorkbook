# In the previous exercise you created a program that computed the area of 
# a triangle when the length of its base and its height were known. It is 
# also possible to compute the area of a triangle when the lengths of all 
# three sides are known. Let s1, s2 and s3 be the lengths of the sides.
 
# Let s = (s1 + s2 + s3)/2. 
# Then the area of the triangle can be calculated using the following 
# formula:

# area = SQRT s × (s − s1) × (s − s2) × (s − s3)

# Develop a program that reads the lengths of the sides of a triangle from 
# the user and displays its area.

import math # first need to import math to use sqrt function

s1 = float(input('Enter length of the first edge: '))
s2 = float(input('Enter length of the second edge: '))
s3 = float(input('Enter length of the third edge: '))

s = (s1 + s2 +s3)/2


area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print('Area of the triangle is: %.2f' % area)