# It is commonly said that one human year is equivalent to 7 dog years. 
# However this simple conversion fails to recognize that dogs reach adulthood 
# in approximately two years. As a result, some people believe that it is 
# better to count each of the first two human years as 10.5 dog years, and 
# then count each additional human year as 4 dog years.

# Write a program that implements the conversion from human years to dog 
# years described in the previous paragraph. 

# Ensure that your program works 
# correctly for conversions of less than two human years and for conversions 
# of two or more human years. Your program should display an appropriate 
# error message if the user enters a negative number.

humanYears = float(input('Enter human years: '))

if humanYears > 0:
    if humanYears >= 2:
        #add first 2 years 2*10.5 and than rest of years *4
        dogYears = 21 + ((humanYears - 2) * 4)
    elif humanYears < 2:
        dogYears = humanYears * 10.5
    print('\nWhen you convert',humanYears,'of Human years, it gives you:',dogYears,'of dog years.\n')
elif humanYears < 0:
    print('\nYou enter wrong number. Years cannot be below 0\n')