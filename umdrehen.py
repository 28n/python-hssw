import tkinter
class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master) #
        self.pack()# 
        self.createWidgets()

    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self, fg="red", bg="yellow", insertwidth=10, borderwidth=20, insertborderwidth=500, font=('arial', 20, 'bold'), border=4, )
        self.nameEntry.grid(padx=50, pady=20)

        self.name = tkinter.StringVar()
        self.name.set("Eingabe eintippen ...")
        self.nameEntry["textvariable"] = self.name

        self.kopie = tkinter.Button(self, height=3, width=50, border=0, fg="green", bg="lightgrey", font = ("arial", 20, "bold"))
        self.kopie["text"] = "Kopie"
        self.kopie["command"] = self.onReverse
        self.kopie.grid()

        self.rev = tkinter.Button(self, height=3, width=50, border=4, fg="darkblue", bg="lightgreen", font = "bold")
        self.rev["text"] = "Umdrehen"
        self.rev["command"] = self.onReverse
        self.rev.grid()

        self.ok = tkinter.Button(self, height=3, width=50, border=4, fg="red", bg="yellow", font = "bold")
        self.ok["text"] = "Beenden"
        self.ok["command"] = self.quit
        self.ok.grid()



    def onReverse(self):
        #self.name.set(self.name.get()[::-1])
        self.kopie["text"] = self.name.get()[::-1]

root = tkinter.Tk()
app = MyApp()
app.mainloop()