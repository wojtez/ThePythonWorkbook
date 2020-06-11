# Create a program that reads three integers from the user and displays them 
# in sorted order (from smallest to largest). 

# Use the min and max functions to find the smallest and largest values.

# The middle value can be found by computing the sum of all three values, 
# and then subtracting the minimum value and the maximum value.

number1 = int(input('Enter first umber: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))

max = max(number1, number2, number3)
min = min(number1, number2, number3)
med = (number1 + number2 + number3) - max - min

print('max =', max)
print('med =', med)
print('min =', min)
