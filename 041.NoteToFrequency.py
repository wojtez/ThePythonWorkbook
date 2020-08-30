'''
The following table lists an octave of music notes, beginning with middle C, 
along with their frequencies.

Note Frequency (Hz) C4 261.63 / D4 293.66 / E4 329.63 / F4 349.23 / 
G4 392.00 / A4 440.00 / B4 493.88

Begin by writing a program that reads the name of a note from the user and 
displays the note’s frequency. Your program should support all of the notes 
listed previously.  

Once you have your program working correctly for the notes listed previously 
you should add support for all of the notes from C0 to C8.

While this could be done by adding many additional cases to your if 
statement, such a solution is cumbersome, inelegant and unacceptable for 
the purposes of this exercise. 

Instead, you should exploit the relationship between notes in adjacent 
octaves. In particular, the frequency of any note in octave n is half 
the frequency of the corresponding note in octave n+1. By using this 
relationship, you should be able to add support for the additional notes 
without adding additional cases to your if statement.

Hint: To complete this exercise you will need to extract individual 
    characters from the two-character note name so that you can work with the 
    letter and the octave number separately. Once you have separated the parts,
    compute the frequency of the note in the fourth octave using the data in the 
    table above. Then divide the frequency by 24−x, where x is the octave number 
    entered by the user. This will halve or double the frequency the correct 
    number of times.
'''

C4 = 261.63
D4 = 293.66 
E4 = 326.63 
F4 = 349.23 
G4 = 392.00 
A4 = 440.00 
B4 = 493.88

#Read the note from user
print("You should use one of the capital letter (C, D, E, F, G, A, B), for music note.")
print("You should use one of the octave digit (0 - 8) for chosen octave.\n")

name = input("Please enter your input: ")

#Store the note and its octave in separate variables
note = name[0]
octave = int(name[1])
# for checking purpose
#print("You type:", note,octave)

#Get the frequency of note assuming it is in the forth octave
if octave == 4:
    if note == "C":
        freq = C4
    elif note == "D":
        freq = D4
    elif note == "E":
        freq = E4
    elif note == "F":
        freq = F4
    elif note == "G":
        freq = G4
    elif note == "A":
        freq = A4
    elif note == "B":
        freq = B4

#Adjust the frequency to bring in into corect octave
if octave == 0 or octave == 1 or octave == 2 or octave == 3 \
    or octave == 5 or octave == 6 or octave == 7 or octave == 8:
    if note == "C":
        freq = C4 / 2 ** (4 - octave)
    elif note == "D":
        freq = D4 / 2 ** (4 - octave)
    elif note == "E":
        freq = E4 / 2 ** (4 - octave)
    elif note == "F":
        freq = F4 / 2 ** (4 - octave)
    elif note == "G":
        freq = G4 / 2 ** (4 - octave)
    elif note == "A":
        freq = A4 / 2 ** (4 - octave)
    elif note == "B":
        freq = B4 / 2 ** (4 - octave)

#Display result
print("The frequency of", name, "is", freq)