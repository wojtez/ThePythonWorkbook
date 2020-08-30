'''
In the previous question you converted from note name to frequency.
In this question you will write a program that reverses that process.
Begin by reading a frequency from the user.

If the frequency is within one Hertz of a value listed in the table in the
previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need
to consider the notes listed in the table. There is no need to consider notes
from other octaves.
'''
C4 = 261.63; D4 = 293.66; E4 = 326.63; F4 = 349.23; G4 = 392.00; A4 = 440.00; 
B4 = 493.88
avg = 1.0

# Read the note from user
frequency = float(input("Type frequency to get her music note: "))

if frequency >= C4 - avg and frequency <= C4 + avg:
    print(frequency, " is app. frequency, closes to C4 music note =",C4)
elif frequency >= D4 - avg and frequency <= D4 + avg:
    print(frequency, " is app. frequency, closes to D4 music note =",D4)
elif frequency >= E4 - avg and frequency <= E4 + avg:
    print(frequency, " is app. frequency, closes to E4 music note =",E4)
elif frequency >= F4 - avg and frequency <= F4 + avg:
    print(frequency, " is app. frequency, closes to F4 music note =",F4)
elif frequency >= G4 - avg and frequency <= G4 + avg:
    print(frequency, " is app. frequency, closes to G4 music note =",G4)
elif frequency >= A4 - avg and frequency <= A4 + avg:
    print(frequency, " is app. frequency, closes to A4 music note =",A4)
elif frequency >= B4 - avg and frequency <= B4 + avg:
    print(frequency, " is app. frequency, closes to B4 music note =",B4)
else:
    print("Frequency you type in, is not coresponding with known notes. ")