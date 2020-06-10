# In many jurisdictions a small deposit is added to drink containers to 
# encourage people to recycle them. In one particular jurisdiction, 
# drink containers holding one liter or less have a $0.10 deposit, and drink
# containers holding more than one liter have a $0.25 deposit.
# Write a program that reads the number of containers of each size from the 
# user. Your program should continue by computing and displaying the refund 
# that will be received for returning those containers. Format the output so 
# that it includes a dollar sign and always displays exactly two decimal 
# places.

smallcontainer = int(input('How many containers below one liter? '))
bigcontainer = int(input('How many containers above one liter? '))
smalldep = 0.10
bigdep = 0.25

totaldeposit = (smallcontainer * smalldep) + (bigcontainer * bigdep)

# $%.2f this statement shows results with 2 digit after coma and $ (dolar) before
print('\nIf you give containers back, you will get $%.2f.' % totaldeposit) 
print('\nReturn', smallcontainer,'piece of small containers for $%.2f' % smalldep,', and',bigcontainer,'piece of big containers for $%.2f' % bigdep,'\n')