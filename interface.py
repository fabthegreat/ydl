import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        Frame1 = tk.Frame(self, borderwidth=2, relief="groove")
        Frame1.pack(side="left", padx=330, pady=330)
        nom = tk.Label(self, text = 'Votre nom :')
        reponse = tk.Entry(self)
        valeur = tk.Button(self, text =' Valider', command=self.repondre)
        reponse.pack()
        valeur.pack()
    
    def repondre():
        print("reponse")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
