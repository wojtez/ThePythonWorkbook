# Consider the software that runs on a self-checkout machine. One task that 
# it must be able to perform is to determine how much change to provide when 
# the shopper pays for a purchase with cash.

# Write a program that begins by reading a number of cents from the user as 
# an integer. Then your program should compute and display the denominations 
# of the coins that should be used to give that amount of change to the 
# shopper. The change should be given using as few coins as possible. Assume 
# that the machine is loaded with pennies, nickels, dimes, quarters, loonies 
# and toonies.
#
# A one dollar coin was introduced in Canada in 1987. It is referred to as a 
# loonie because one side of the coin has a loon (a type of bird) on it. 
# The two dollar coin, referred to as a toonie, was introduced 9 years later. 
# It’s name is derived from the combination of the number two and the name 
# of the loonie.

centPerToonie = 200
centPerLoonie = 100
centPerQuarter = 25
centPerDime = 10
centPerNickle = 5

cents = int(input('Enter the number of cents: '))

print('You can get', cents // centPerToonie,' tonnies')  # returns integer value
cents = cents % centPerToonie                            # returns moduo
print('You can get', cents // centPerLoonie,' loonies')
cents = cents % centPerLoonie
print('You can get', cents // centPerQuarter,' quarters')
cents = cents % centPerQuarter
print('You can get', cents // centPerDime,' dimes')
cents = cents % centPerDime
print('You can get', cents // centPerNickle,' nickles')
cents = cents % centPerNickle
print('You can get', cents,' pennies')
