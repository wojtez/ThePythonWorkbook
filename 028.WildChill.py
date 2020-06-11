# When the wind blows in cold weather, the air feels even colder than it 
# actually is because the movement of the air increases the rate of cooling 
# for warm objects, like people. This effect is known as wind chill.

# In 2001, Canada, the United Kingdom and the United States adopted the 
# following formula for computing the wind chill index. Within the formula 
# Ta is the air temperature in degrees Celsius and V is the wind speed in 
# kilometers per hour. A similar formula with different constant values 
# can be used with temperatures in degrees Fahrenheit and wind speeds in 
# miles per hour.

# WCI = 13.12 + 0.6215 * T − 11.37 V**0.16 + 0.3965 * T V**0.16

# Write a program that begins by reading the air temperature and wind speed 
# from the user. Once these values have been read your program should 
# display the wind chill index rounded to the closest integer.

# HINT
# The wind chill index is only considered valid for temperatures less than 
# or equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers 
# per hour.

print("\nFormula is valid ONLY for temp <= 10 C degrees and wind speed < 4.8 km/h\n")
temp = int(input('Enter air temperature in C deg: '))
wind = int(input('Enter wind speed in km/h: '))

# Formula was splited to 4 different digit
factor1 = 13.12
factor2 = 0.6215 * temp
factor3 = 11.37 * (wind**0.16)
factor4 = 0.3965 * temp * (wind**0.16)

# checking WCI
wci = factor1 + factor2 - factor3 + factor4

print('WCI =',  round(wci))
