# Create a program that reads two integers, a and b, from the user.Your 
# program should compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab

# we need to import log10 function from math module
from math import log10

a = int(input('a: = '))
b = int(input('b: = '))

print('a sum with b, (a + b):              = ', a + b)
print('b subtracted from a, (a - b):       = ', a - b)
print('product of a and b, (a * b):        = ', a * b)
print('quotient a divided by b, (a / b):   = ', a / b)
print('reminder a divided by b, (a % b):   = ', a % b)
print('log10 for',a,' :                      = ', log10(a))
print('a to the b degree, (a**b):          = ', a ** b)
