# In the United States, fuel efficiency for vehicles is normally expressed 
# in miles-per gallon (MPG). In Canada, fuel efficiency is normally expressed 
# in liters-per-hundred kilometers (L/100 km).

# Use your research skills to determine how to convert from MPGto L/100 km. 
# Then create a program that reads a value from the user in American units 
# and displays the equivalent fuel efficiency in Canadian units.

# US Gallon = 3.785411784
# 1 mile = 1.609344

USGallon = 3.785411784
mile = 1.609344
mpg = float(input('Write how many Miles per Gallon: '))

#convert Miles per Gallon to Litters per 100km
litersPerKm = (100 * USGallon) / (mile * mpg)

print(mpg,'miles per Gallon gives $%.2f' %litersPerKm,'litters per 100km\n')
