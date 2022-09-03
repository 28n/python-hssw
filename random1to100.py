
import random
# Erzeugt Zufallszahl zwischen 1 und 100
a = random.randint(1, 100)
b = int
b = 0
min = int 
min = 0
max = int 
max = 100
versuche = int
versuche = 0

print("Die zufällige Zahl lautet " + str(a))

while a != b:
    b = int(input("Suche die Zahl zwischen 1 und 100: "))
    print("Du hast folgendes eingegeben: " + str(b) + "")
    versuche = versuche +1
    if b > a:
        print("Your number is greater than my")
        max = b
    elif a == b:
        print("You are right")
    else:
        print("Your number is smaller than my")
        min = b
    print("Minimum " + str(min) + " bis Maximum " + str(max) + " (" + str(versuche) + " Versuche)\n" )

#if Value(nutzerZahl) == gesuchteZahl: 
#    print("Die Zahl ist korrekt!")
#if Value(nutzerZahl) > gesuchteZahl:
#    print("Deine Zahl ist zu groß!")
#if Value(nutzerZahl)5 < gesuchteZahl:
#    print("Deine Zahl ist zu klein!")
