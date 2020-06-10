# In this exercise, you will create a program that begins by reading a 
# measurement in feet from the user. Then your program should display the 
# equivalent distance in inches, yards and miles. Use the Internet to look 
# up the necessary conversion factors if you don’t have them memorized.

foot = float(input('Enter distance in feet: '))

inches = foot * 12
print(foot,'feet distance is %.2f' % inches,'inches')

yards = foot * 0.3333333
print(foot,'feet distance is %.2f' % yards,'yards')

miles = foot * 0.0001893939
print(foot,'feet distance is %.2f' % miles,'miles')
