import tkinter as tk
root = tk.Tk()

# Textausgabe erzeugen
label1 = tk.Label(root, text='Hallo Welt', 
                        fg='red',
                        bg='yellow',
                        font=('times', 25, 'bold', 'italic'))

# in GUI Elemente einbetten
# pack und grid nicht gleichzeitig verwendbar
#label1.pack(side="left")
label1.grid(row=10, column=0, columnspan=3)

# Grafik einbetten
bild1 = tk.PhotoImage(file="biene.png")
#label2 = tk.Label(root, image=bild1).pack(side="right")
label2 = tk.Label(root, image=bild1, cursor='heart',).grid(row=11, column=0, columnspan=3)


# grid
label11 = tk.Label(root, text="Hallo Welt, here I am", bg="orange", font=('times', 12, 'bold', 'italic'))
label11.grid(row=0, column=0)

label12 = tk.Label(root, text="R1 / C1", bg="lightgreen")
label12.grid(row=1, column=1)

label13 = tk.Label(root, text="R2 / C2", bg="lightblue")
label13.grid(row=2, column=2)

label14 = tk.Label(root, text="rechts", bg="yellow")
label14.grid(row=3, column=0, sticky='e')

label15 = tk.Label(root, text="links", bg="yellow")
label15.grid(row=4, column=0, sticky='w')

label16 = tk.Label(root, text="mittig", bg="yellow")
label16.grid(row=5, column=0, sticky='')

# Label für anschließendes Eingabefeld
label21 = tk.Label(root, text="Jetzt kommt das Eingabefeld:", bg="lightblue")
label21.grid(row=20, column=0, sticky='')
# Eingabefeld
eingabefeld_wert=tk.StringVar()
eingabefeld=tk.Entry(root, textvariable=eingabefeld_wert)
eingabefeld.grid(row=21, column=0)
eingabefeld_wert.set('Hier eintippen ...')

# Muss VOR Aufruf definiert werden
def aktionSF():
    print("Aktion durchgeführt!")

# Dann wird Fenster NICHT mehr geschlossen!
#def quit():
#    print("Das ist das Ende!")

# Button
schaltf1 = tk.Button(root, text="Aktion durchführen", command=aktionSF)
schaltf1.grid(row=25, column=0)

# Exit-Button (Buttons mit identischem Namen funktionieren!???)
schaltf1 = tk.Button(root, cursor='hand2', text="Exit", command=quit)
schaltf1.grid(row=25, column=1)
# cursor='tcross' cursor='hand1' cursor='hand2' cursor='heart' cursor='pencil'

label31 = tk.Label(root, text="Hallo Klima", fg="red", bg="yellow", height=2, width=30, anchor="center")
label31.grid(row=30, column=0, columnspan=8)

# Radiobutton
mode_of_transportation = tk.Label(root, text="Mode of transportation: ")
mode_of_transportation.grid(column=0, row=51)

r = 1
#r = IntVar()
express = tk.Radiobutton(text="Express (Grab, Uber, Taxi)", variable=r, value=0, highlightthickness=0)
express.grid(column=0, row=52, sticky="W")

normal = tk.Radiobutton(text="Normal (Jeep, Bus, UV, Tric)", variable=r, value=1, highlightthickness=0)
normal.grid(column=0, row=53, sticky="W")

# Zwischenlabel
label31 = tk.Label(root, text="Hallo Leute", fg="darkgreen", bg="lightblue", font = "bold", height=2, width=30, anchor="se")
label31.grid(columnspan=8)

# Radiobutton 2
def ausgabe():
    print(ausgewaehlt.get())
    aktuell_ausgewaehlt = ausgewaehlt.get()
    textausgabe = tk.Label(root, text=aktuell_ausgewaehlt, bg="orange")
    textausgabe.grid()

anrede = ["Frau", "Herr", "Firma"]

ausgewaehlt = tk.StringVar()
ausgewaehlt.set("Frau")

for einzelwert in anrede:
    radiob = tk.Radiobutton(root, text=einzelwert, value=einzelwert, variable=ausgewaehlt, command=ausgabe)
#    radiob.pack()
    radiob.grid()

# Zwischenlabel
label31 = tk.Label(root, text="Hallo Fans", fg="darkgreen", bg="yellow", font = "bold", height=2, width=30, anchor="nw")
label31.grid(columnspan=8)

# Checkboxen
def ausgabe2():
    print(checkbox01var.get())
    aktuell_ausgewaehlt = checkbox01var.get()
    textausgabe = tk.Label(root, text=aktuell_ausgewaehlt, bg="orange")
    textausgabe.grid()

checkbox01 = tk.Checkbutton(root)
checkbox01["text"] = "Sport treiben"
checkbox01.grid()

checkbox01var = tk.BooleanVar()
checkbox01var.set(True)
checkbox01["variable"] = checkbox01var

checkbox02 = tk.Checkbutton(root)
checkbox02["text"] = "Lesen"
checkbox02.grid()

checkbox02var = tk.BooleanVar()
checkbox02["variable"] = checkbox02var

checkbox03 = tk.Checkbutton(root)
checkbox03["text"] = "Filme schauen"
checkbox03.grid()

checkbox03var = tk.BooleanVar()
checkbox03["variable"] = checkbox03var

schaltf1 = tk.Button(root, text="Aktion durchführen", bg="lightgreen", command= ausgabe)
schaltf1.grid()

# Labelframe
gruppehobby = tk.LabelFrame(root, text="Ihre Hobbies?")
gruppehobby.grid() 

checkbox011 = tk.Checkbutton(gruppehobby)
checkbox011["text"] = "Sport treiben"
checkbox011.grid(sticky="W")
checkbox011var = tk.BooleanVar()
checkbox011["variable"] = checkbox011var

checkbox012 = tk.Checkbutton(gruppehobby)
checkbox012["text"] = "Lesen"
checkbox012.grid(sticky="W")
checkbox012var = tk.BooleanVar()
checkbox012var.set(True)
checkbox012["variable"] = checkbox012var

checkbox013 = tk.Checkbutton(gruppehobby)
checkbox013["text"] = "Filme schauen"
checkbox013.grid(sticky="W")
checkbox013var = tk.BooleanVar()
checkbox013["variable"] = checkbox013var


root.mainloop()