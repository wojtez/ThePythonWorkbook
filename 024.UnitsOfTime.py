# Create a program that reads a duration from the user as a number of days, 
# hours, minutes, and seconds.

# Compute and display the total number of seconds represented by this duration.

# here we still not use datetime module
days = int(input('Enter number of days: '))
hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
seconds = int(input('Enter number of seconds: '))

uDay = days * 24 * 60 * 60
uHours = hours * 60 * 60
uMinutes = minutes * 60
uSeconds = seconds

time = uDay + uHours + uMinutes + uSeconds

print("\nD:",days,'+','h:',hours,'+','m:',minutes,'+','s:',seconds)
print('Gives total:',time,'seconds.\n')