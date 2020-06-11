# In this exercise you will create a program that reads a letter of the 
# alphabet from the user. If the user enters a, e, i, o or u then your 
# program should display a message indicating that the entered letter is a 
# vowel. If the user enters y then your program should display a message 
# indicating that sometimes y is a vowel, and sometimes y is a consonant. 
# Otherwise your program should display a message indicating that the letter 
# is a consonant.


letter = input('Enter the letter: ')

if letter == 'a' or letter == 'e' or letter == 'i' or \
    letter == 'o' or letter == 'u':
    print(letter,': is vowel\n')
elif letter == 'y':
    print(letter,': sometimes can be a vowel, sometimes consonant\n')
else:
    print(letter,': is consonant\n')