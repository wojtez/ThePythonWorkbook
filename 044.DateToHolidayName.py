'''
Canada has three national holidays which fall on the same dates each year.

Holiday             Date
New year’s day      January 1
Canada day          July 1
Christmas day       December 25

Write a program that reads a month and day from the user. If the month and day 
match one of the holidays listed previously then your program should display the 
holiday’s name. Otherwise your program should indicate that the entered month and 
day do not correspond to a fixed-date holiday.

Canada has two additional national holidays, Good Friday and Labour Day, whose 
dates vary from year to year. There are also numerous provincial and territorial 
holidays, some of which have fixed dates, and some of which have variable dates. 
We will not consider any of these additional holidays in this exercise.
'''

holidays = {01.01: "New Year's Day", 01.07: "Canada day", 25.12: "Christmas Day"}

# taking input from user
month = input("Enter month in format mm: ")
day = input("Enter the day in format dd: ")

# adding days to month
date = day+'.'+month

# compareing input with holidays
if date == "01.01":
    print("You enter", date,"that is", holidays[01.01])
elif date == "01.07":
    print("You enter", date,"that is", holidays[01.07])
elif date == "25.12":
    print("You enter", date,"that is", holidays[25.12])
else:
    print("You enter:",date,"- there is no holiday asign to this date.")