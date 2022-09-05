from tkinter import *

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button "Klick mich" anklickt
# event in Klammern, damit Übergabe an Funktion möglich!
def button_action():
#    print("Kontrolle")
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Gib zuerst einen Namen ein.")
    else:
        entry_text = "Welcome " + entry_text + "!" 
        welcome_label.config(text=entry_text)

def returnPressed(event):
    button_action()

fenster = Tk()
fenster.title("Ich warte auf eine Eingabe von dir.")
# Fenstergröße, Hintergrundfarbe
fenster.geometry('600x300')
fenster.configure(bg='lightgreen')

# Anweisungs-Label
my_label = Label(fenster, text="Gib deinen Namen ein: ")

# In diesem Label wird nach dem Klick auf den Button der Benutzer
# mit seinem eingegebenen Namen begrüsst.
# fg='#00ff00' (alternative Farbdefintion)
welcome_label = Label(fenster, text="Moin ...", bg="yellow", fg="red")

# Hier kann der Benutzer eine Eingabe machen
eingabefeld = Entry(fenster, bd=2, width=50)
# Setzt Fokus auf Eingabefeld
eingabefeld.focus()

# Returntaste wird an Funktion gekoppelt = Alternative zu Button
# Klappt nur über separate Funktion wg Übergabepb "event"
eingabefeld.bind("<Return>", returnPressed)


klickmich_button = Button(fenster, text="Klick mich", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)


# Nun fügen wir die Komponenten unserem Fenster hinzu
my_label.grid(row = 0, column = 0, sticky="w")
eingabefeld.grid(row = 1, column = 1, sticky="w")
klickmich_button.grid(row = 2, column = 2, sticky="w")
exit_button.grid(row = 3, column = 3, sticky="w")
welcome_label.grid(row = 4, column = 1, columnspan = 1, sticky="w")

mainloop()