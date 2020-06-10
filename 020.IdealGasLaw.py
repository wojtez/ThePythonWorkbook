# The ideal gas law is a mathematical approximation of the behavior of gasses 
# as pressure, volume and temperature change. It is usually stated as: 
# PV = nRT where P is the pressure in Pascals, V is the volume in liters, 
# n is the amount of substance in moles, R is the ideal gas constant, equal 
# to 8.314 J mol K , and T is the temperature in degrees Kelvin.

# Write a program that computes the amount of gas in moles when the user 
# supplies the pressure, volume and temperature. Test your program by 
# determining the number of moles of gas in a SCUBA tank.

# A typical SCUBA tank holds 12 liters of gas at a pressure of 20,000,000 
# Pascals (approximately 3,000 PSI).
# Room temperature is approximately 20 degrees Celsius or 68 degrees Fahrenheit.

# Hint: A temperature is converted from Celsius to Kelvin by adding 273.15 
# to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from 
# it, multiply it by 5/9 and then add 273.15 to it.

p = float(input('Enter pressure in Pascal: '))
v = float(input('Enter volume in liters: '))
t = float(input('Enter temperature in Celsius: '))

r = 8.314 # ideal gas constant

#converting Cesius to Kelwin
celToKal = t + 273.15

#to get amount of gas in moles, need convert PV = nRT
n = (p*v) / (r * celToKal)

#printing results
print("Input data:")
print("pressure:     =", p,"\nvolume:       =", v,"\ntemperature:  =", t)

print("Amount in mol:", round(n, 3))

#testing values
p = 20000000
v = 12
t = 20
celToKal = t + 273.15
n = (p*v) / (r * celToKal)

print("Values with testing data gives:", round(n, 3))