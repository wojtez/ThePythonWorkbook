# A triangle can be classified based on the lengths of its sides as equilateral,
# isosceles or scalene. All 3 sides of an equilateral triangle have the same 
# length. An isosceles triangle has two sides that are the same length, and 
# a third side that is a different length. If all of the sides have different 
# length then the triangle is scalene. 

# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

a = int(input('Enter lenght of the first side: '))
b = int(input('Enter lenght of the second side: '))
c = int(input('Enter lenght of the third side: '))

print('a=',a)
print('b=',b)
print('c=',c)

if a == b == c:
    print('Triangle is equilateral')
elif a == b or a == c or b == c:
    print('Triangle is isosceles')
#elif b == a or b == c:
#    print("Triange is isosceles")
else:
    print('Triangle is scalene')