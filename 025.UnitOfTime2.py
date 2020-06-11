# In this exercise you will reverse the process described in the previous 
# exercise. Develop a program that begins by reading a number of seconds 
# from the user. Then your program should display the equivalent amount of 
# time in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, 
# hours, minutes and seconds respectively. The hours, minutes and seconds
# should all be formatted so that they occupy exactly two digits, with a 
# leading 0 displayed if necessary.

#add amout of seconds in days, hours, minutes
secondPerDays = 86400
secondPerHours = 3600
secondPerMinutes = 60

#input data r
seconds = int(input('Enter number of seconds: '))

#first receive days and rest of seconds asign to next line
days = seconds / secondPerDays
seconds = seconds % secondPerDays
#than receive hours and rest of the seconds asign to next line
hours = seconds / secondPerHours
seconds = seconds % secondPerHours
#than receive minutes and the rest of of the second asign to next line
minutes = seconds / secondPerMinutes
seconds = seconds % secondPerMinutes

# %02d - special format which tell Python to format the integer using 2 
# digits adding the leading 0 if necessary
print("  %02d"%days,": %02d"%hours,": %02d"%minutes,": %02d"%seconds)
print('D %02d' % days,'h %02d' % hours,'m %02d' % minutes,'s %02d' % seconds)
