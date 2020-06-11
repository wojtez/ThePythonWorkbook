# Write a program that reads an integer from the user. Then your program 
# should display a message indicating whether the integer is even or odd.

number = int(input('Enter integer number: '))

if number % 2 == 1:
    number = 'Number you enter is even'
else:
    number = 'Number you enter is odd'

print(number)