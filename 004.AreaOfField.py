# Create a program that reads the length and width of a farmer’s field 
# from the user in feet. Display the area of the field in acres.

# Hint: There are 43,560 square feet in an acre.

width = float(input('What is the width of the field in feet: '))
length = float(input('What is the length of the field in feet: '))

area = width * length
acr = round((area / 43560), 2)

print('Area of the field is:', area, 'square feet, which gives:', acr, 'acres')
