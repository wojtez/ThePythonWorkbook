# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted 
# by 60 percent. Write a program that begins by reading the number of loaves 
# of day old bread being purchased from the user. Then your program should 
# display the regular price for the bread, the discount because it is a day 
# old, and the total price. All of the values should be displayed using two 
# decimal places, and the decimal points in all of the numbers should be 
# aligned when reasonable values are entered by the user.

oldBread = int(input('Enter number of old bread: '))

regularPrice = 3.49
totalPrice = oldBread * regularPrice
priceAfterDiscount = regularPrice * 0.60
totalPriceAfterDiscount = oldBread * priceAfterDiscount

discount = totalPrice - totalPriceAfterDiscount

print('You purchase', oldBread,'pce of old bread')
print('$%.2f' % totalPrice,'- regular price.')
print('$%.2f' % discount,'- discount due to old bread.')
print('$%.2f' % totalPriceAfterDiscount,'- price you have to pay.')