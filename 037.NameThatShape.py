# Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user and then report the appropriate name 
# as part of a meaningful message. 

# Your program should support shapes with  anywhere from 3 up to 
# (and including) 10 sides. If a number of sides outside of this range is 
# entered then your program should display an appropriate error message.

sides = int(input('Enter number of sides (from 3 to 10): '))

if sides == 3:
    print(sides,'gives you triangle')
elif sides == 4:
    print(sides,'gives you square')
elif sides == 5:
    print(sides,'gives you pentagon')
elif sides == 6:
    print(sides,'gives you hexagon')
elif sides == 7:
    print(sides,'gives you heptagon')
elif sides == 8:
    print(sides,'gives you octagon')
elif sides == 9:
    print(sides,'gives you nonagon')
elif sides == 10:
    print(sides,'gives you decagon')
else:
    print("You enter out of the range value")