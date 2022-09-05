# Beispiel 1
print("Beispiel 1\nSo wird es richtig gemacht!")
rueckgabewert = 0

def bspfunktionfuerrueckgabe(eingabewert):
    rueckgabewert = eingabewert * 2
    return rueckgabewert

#print("1: " + str(rueckgabewert))
ergebnisausfunktion = bspfunktionfuerrueckgabe (5)
print(ergebnisausfunktion)
print(rueckgabewert)
print("=====")

# Beispiel 2
print("Beispiel 2\nHier ist die Variable außerhalb der Funktion nicht definiert!")

def bspfunktionfuerrueckgabe(eingabewert):
    rueckgabewert = eingabewert * 2
    return rueckgabewert

ergebnisausfunktion = bspfunktionfuerrueckgabe (5)
print(ergebnisausfunktion)
print(rueckgabewert)
print("=====")

# Beispiel 3
print("Beispiel 3\nVariablen global und lokal - hier global -> Ausgabefehler in Funktion")

variablenWert = "außerhalb der Funktion"
print("Variablenwert vor Funktion:", variablenWert)
def bspfunktion():
    # Hier kommt der Fehler, weil "variablenwert" lokal unbekannt!
    #print("Variablenwert in Funktion 1:", variablenWert)
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion 2:", variablenWert)

bspfunktion()
print("Variablenwert nach Funktion:", variablenWert)
print("=====")

# Beispiel 4
print("Beispiel 4\nVariablen global und lokal - hier global und lokal neu definiert")
# Es existieren offenbar 2! Variablen mit gleichem Namen!
variablenWert = "außerhalb der Funktion"
print("Variablenwert vor Funktion:", variablenWert)
def bspfunktion():
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion:", variablenWert)

bspfunktion()
print("Variablenwert nach Funktion:", variablenWert)
print("=====")

# Beispiel 5
print("Beispiel 5\nVariablen global und lokal - hier global und lokal als global definiert")
variablenWert = "außerhalb der Funktion"
print("Variablenwert vor Funktion:", variablenWert)
def bspfunktion():
    global variablenWert
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion:", variablenWert)

bspfunktion()
# Durch globale Definition in der Funktion bleibt der Wert nach der Funktion erhalten.
print("Variablenwert nach Funktion:", variablenWert)
print("=====")
