# Create a program that determines how quickly an object is traveling when 
# it hits the ground. The user will enter the height from which the object 
# is dropped in meters (m).

# Because the object is dropped its initial speed is 0m/s. Assume that the 
# acceleration due to gravity is 9.8m/s2.

# You can use the formula vf =  v 2i + 2ad to compute the final speed, vf,
# when the initial speed, vi, acceleration, a, and distance, d, are known.

from math import sqrt

h = float(input('Enter the height in meters: '))
gravity = 9.8
initialSpeed = 0


totalTime = sqrt((2*h)/gravity)
totalSpeed = sqrt(initialSpeed**2 + (2 * gravity * h))

print('Object will hit ground after %.2f' % totalTime,'seconds')
print('Object will hit ground with speed of %.1f' % totalSpeed,'m/s')