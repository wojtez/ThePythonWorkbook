# Many people think about their height in feet and inches, even in some 
# countries that primarily use the metric system. Write a program that reads 
# a number of feet from the user, followed by a number of inches. Once these 
# values are read, your program should compute and display the equivalent 
# number of centimeters.
#
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

inchesInFeet = 12
centimetersInInches = 2.54

print('Enter your height:')
feet = int(input('How many feet: '))
inches = int(input('Chow many inches: '))

total_cm = (feet*inchesInFeet*centimetersInInches)+((inches*centimetersInInches))

meters = total_cm//100
centimeters = total_cm%100

print('Your height in metric system is:',round(total_cm,2),'centimeters')
print("Which gives you", round(meters,0),"meters, and", round(centimeters,2), "centimeters.")