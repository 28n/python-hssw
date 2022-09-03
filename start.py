print("Hello World!")
# Dies ist ein Kommentar, diese fangen mit einem # an und hören am Zeilenumbruch auf

text = "Hallo!"
# Variablen werden mit einem Namen und einem Wert deklariert. Es gibt keine Typen, jeder Wert kann jeder Variable zugewiesen werden.
print(text)

nummer1 = 5
nummer2 = 2
ergebnis = nummer1 + nummer2
# mathematische operationen können ganz einfach durchgeführt werden! mögliche operatoren sind: +, -, *, /

print(ergebnis)
print(nummer1 + nummer2)
# mathematische operationen können auch direkt durchgeführt werden

nutzereingabe = input("Bitte gib etwas ein! ")
print("Du hast folgendes eingegeben: " + nutzereingabe + "\n")
# Nutzereingabe funktioniert mit input!
# ACHTUNG: Probier auch mal aus, eine Nummer oder das wort "true" einzugeben.

class Person:
    def __init__(self, name, beruf):
        self.name = name
        self.beruf = beruf

    def hallo(self):
        print("Hallo, ich bin " + self.name + ". Mein Beruf ist " + self.beruf + ".")
    
# eine klasse ist ein umriss eines objektes

hssw = Person("hssw", "Entwickler")
wssh = Person("wssh", "Zocker")

# man kann mehrere Objekte mit der selben Klasse erstellen

print(hssw.beruf)
print(hssw.name)
hssw.hallo()