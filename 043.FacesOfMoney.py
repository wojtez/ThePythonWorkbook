'''
It is common for images of a country’s previous leaders, or other individuals 
of historical significance, to appear on its money. The individuals that appear 
on banknotes in the United States are listed in Table below.

Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears 
on the banknote of the entered amount. An appropriate error message should be 
displayed if no such note exists.

Individual          Amount
George Washington   $1
Thomas Jefferson    $2
Abraham Lincoln     $5
Alexander Hamilton  $10
Andrew Jackson      $20
Ulysses S. Grant    $50
Benjamin Franklin   $100

While two dollar banknotes are rarely seen in circulation in the United States, 
they are legal tender that can be spent just like any other denomination. The 
United States has also issued banknotes in denominations of $500, $1,000, 
$5,000, and $10,000 for public use. However, high denomination banknotes have 
not been printed since 1945 and were officially discontinued in 1969. As a 
result, we will not consider them in this exercise.
'''

quote = input("Enter amount of $ you like to check: ")
quote = int(quote)

while quote > 0:
    if quote >= 100:
        print("You get 100$ - Benjamin Franklin")
        quote = quote - 100
    elif quote >= 50 and quote < 100:
        print("You get  50$ - Ulysses S. Grant")
        quote = quote - 50
    elif quote >= 20 and quote < 50:
        print("You get  20$ - Anrew Jackson")
        quote = quote - 20
    elif quote >= 10 and quote < 20:
        print("You get  10$ - Alexander Hamilton$")
        quote = quote - 10
    elif quote >= 5 and quote < 10:
        print("You get   5$ - Abraham Lincoln$")
        quote = quote - 5
    elif quote >= 2 and quote < 5:
        print("You get   2$ - Thomas Jefferson$")
        quote = quote - 2
    elif quote >= 1 and quote < 2:
        print("You get   1$ - George Washington$")
        quote = quote - 1