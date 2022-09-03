
import random
# Erzeugt Zufallszahl zwischen 1 und 100
a = random.randint(1, 100)
b = int
b = 0

print("Die zufällige Zahl lautet " + str(a))

while a != b:
    b = int(input("Suche die Zahl zwischen 1 und 100: "))
    print("Du hast folgendes eingegeben: " + str(b) + "\n")
    if b > a:
        print("Your number is greater than my")
    elif a == b:
        print("You are right")
    else:
        print("Your number is smaller than my")

#if Value(nutzerZahl) == gesuchteZahl: 
#    print("Die Zahl ist korrekt!")
#if Value(nutzerZahl) > gesuchteZahl:
#    print("Deine Zahl ist zu groß!")
#if Value(nutzerZahl)5 < gesuchteZahl:
#    print("Deine Zahl ist zu klein!")
