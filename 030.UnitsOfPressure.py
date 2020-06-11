# In this exercise you will create a program that reads a pressure from the 
# user in kilopascals. Once the pressure has been read your program should 
# report the equivalent pressure in pounds per square inch, millimeters of 
# mercury and atmospheres. 
# 
# Use your research skills to determine the conversion factors between these 
# units.


kPa = int(input('Enter pressure in kilopascals: '))

PSI = kPa * 0.145038
mmHg = kPa / 0.1333224
atm = kPa / 101.325

# KiloPascal to Pounds per square Inch
print(kPa,'kPa to PSI = ',round(PSI, 3))
# KiloPascal to Millimeters of Mercury
print(kPa,'kPa to mmHg = ',round(mmHg, 3))
# KiloPascal to Atmospheres
print(kPa,'kPa to Atm. = ',round(atm, 3))