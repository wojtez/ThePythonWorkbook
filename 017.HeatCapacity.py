# The amount of energy required to increase the temperature of one gram of 
# a material by one degree Celsius is the material’s specific heat capacity, C. 
# The total amount of energy required to raise m grams of a material by ΔT 
# degrees Celsius can be computed using the formula: q = mCΔT.

# Write a program that reads the mass of some water and the temperature 
# change from the user. Your program should display the total amount of 
# energy that must be added or removed to achieve the desired temperature 
# change.

# Hint: The specific heat capacity of water is 4.186 J g◦C.

# Because water has a density of 1.0 gram per millilitre, you can use grams 
# and millilitres interchangeably in this exercise.

# Extend your program so that it also computes the cost of heating the water. 
# Electricity is normally billed using units of kilowatt hours rather than 
# Joules. In this exercise, you should assume that electricity costs 8.9 
# cents per kilowatt-hour. Use your program to compute the cost of boiling 
# water for a cup of coffee.

# Hint: You will need to look up the factor for converting between Joules 
# and kilowatt hours to complete the last part of this exercise.

waterHeatCapacity = 4.186
electricityPrice = 8.9
conversion = 2.777778e-007
cap = 250
temperature = 100

mass = float(int(input('Enter amount of water in millilitres: ')))
deltaTemp = float(int(input('Enter change of temperature Celsius deg.: ')))

# Total amount of energy in Joules:
energy = mass * waterHeatCapacity * deltaTemp
print('\n---   Change of the water temperature   ---\n')
print(mass,'milliliters of water required',energy,'Joules of energy to increase temperature for', deltaTemp,'deg.')


print('\n---   Warming up one cup of Coffee   ---\n')
# Change Joules to KWH
q = cap * waterHeatCapacity * temperature
kwh = q * conversion

# price for this amount of energy
price = kwh * electricityPrice

print('You will need', round(kwh, 3), "of KWH to heat up", cap, 'milliliters of water. It will cost you app.', round(price, 3), 'cents')
