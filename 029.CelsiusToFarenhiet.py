# Write a program that begins by reading a temperature from the user in 
# degrees Celsius. Then your program should display the equivalent 
# temperature in degrees Fahrenheit and degrees Kelvin.

# The calculations needed to convert between different units of temperature 
# can be found on the internet.


celsius = int(input('Enter temperature in C degree: '))

fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15

print(celsius,'C =',round(fahrenheit, 2),'of fahrenheit deg.')
print(celsius,'C =',round(kelvin, 2),'of Kelvin deg.')