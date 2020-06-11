# The following table lists the sound level in decibels for several common 
# noises.

# Noise:            Decibel level(dB)
# Jackhammer        130
# Gas lawnmower     106
# Alarm clock       70
# Quiet room        40

# Write a program that reads a sound level in decibels from the user. 

# If the user enters a decibel level that matches one of the noises in the 
# table then your program should display a message containing only that noise. 

# If the user enters a number of decibels between the noises listed then 
# your program should display a message indicating which noises the level is 
# between. 

# Ensure that your program also generates reasonable output for a 
# value smaller than the quietest noise in the table, and for a value larger 
# than the loudest noise in the table.

soundLevel = int(input('Enter the noice level in dB: '))
if soundLevel == 130:
    print(soundLevel,'dB is equal to Jackhammer sound.')
elif soundLevel == 106:
    print(soundLevel,'dB is equal to Gas lawnmover sound.')
elif soundLevel == 70:
    print(soundLevel,'dB is equal to Alarm clock sound.')
elif soundLevel == 40:
    print(soundLevel,'dB is equal to Quiet room sound.')
elif soundLevel > 130:
    print(soundLevel,'dB is above sound level of Jackhammer sound.')
elif soundLevel < 130 and soundLevel > 106:
    print(soundLevel,'dB is between Jackhammer and Gas lawnmower sounds.')
elif soundLevel < 106 and soundLevel > 70:
    print(soundLevel,'dB is between Gas lawnmower and Alarm clock sounds.')
elif soundLevel < 70 and soundLevel > 40:
    print(soundLevel,'dB is between Alarm clock and Quiet room sounds.')
elif soundLevel < 40:
    print(soundLevel,'dB is below sound level of Quiet room.')