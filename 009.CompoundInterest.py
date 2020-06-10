# Pretend that you have just opened a new savings account that earns 4 percent 
# interest per year. The interest that you earn is paid at the end of the year, 
# and is added to the balance of the savings account. Write a program that 
# begins by reading the amount of money deposited into the account from the 
# user. Then your program should compute and display the amount in the 
# savings account after 1, 2, and 3 years. 
# Display each amount so that it is rounded to 2 decimal places.

percent = 0.04
deposit = int(input('How much money you deposit in bank? : '))

earningFirstYear = deposit + (deposit * percent)
earningSecondYear = earningFirstYear + (earningFirstYear * percent)
earningThirdYear = earningSecondYear + (earningSecondYear * percent)

print('You deposit in bank:', deposit)
print('After one year, it gives you %.2f' %earningFirstYear)
print('After two years, it gives you %.2f' %earningSecondYear)
print('After three years, it gives you %.2f' %earningThirdYear)