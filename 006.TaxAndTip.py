# The program that you create for this exercise will begin by reading the cost 
# of a meal ordered at a restaurant from the user. Then your program will 
# compute the tax and tip for the meal. Use your local tax rate when computing 
# the amount of tax owing. Compute the tip as 18 percent of the meal amount 
# (without the tax). The output from your program should include the tax 
# amount, the tip amount, and the grand total for the meal including both 
# the tax and the tip. Format the output so that all of the values are 
# displayed using two decimal places.

costOfTheMeal = float(input('What was the cos of the meal...? '))
tax = 0.23 * costOfTheMeal
tip = 0.18 * costOfTheMeal

totalPrice = float(costOfTheMeal + tax + tip)

print('Tax = $%.2f, Tip = $%.2f., Total cost of your meal is: $%.2f'%(tax, tip, totalPrice))

#another display solution

#print('$%.2f.'% costOfTheMeal,' Cost of the meal.')
#print('$%.2f.'% tax,' Tax for food.')
#print('$%.2f.'% tip,' Tip for service.')