# Develop a program that reads a four-digit integer from the user and displays 
# the sum of the digits in the number. For example, if the user enters 3141 
# then your program should display 3+1+4+1=9.

number = input('\nEnter the number: ')

sum = 0
for i in number:
    sum += int(i)

print('\nSum of all digits in number =', sum,'\n')