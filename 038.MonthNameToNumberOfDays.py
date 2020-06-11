# The length of a month varies from 28 to 31 days. In this exercise you will 
# create a program that reads the name of a month from the user as a string. 
# Then your program should display the number of days in that month. 

# Display “28 or 29 days” for February so that leap years are addressed.

month = (input('Enter name of the month: '))

if month == 'january' or month == 'march' or month == 'may' or \
    month == 'july' or month == 'august' or month == 'october' or \
    month == 'december':
    print(month,'have 31 days.')
elif month == 'april' or month == 'june' or month == 'september' or \
    month == 'november':
    print(month, 'have 30 days.')
elif month == 'february':
    print(month, 'can have 28 or 29 days, depend from the year')
else:
    print('You type wrong name of the month')