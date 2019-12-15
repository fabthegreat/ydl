import tkinter as tk

class Interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def process(self):
        print(self.simulate.get())

    def create_widgets(self):
#        inputs.config(bd=4,bg="blue")
#        inputs.pack()
#
        tk.Label(self.master, padx=10,text="Youtube URL",bg="red").grid(row=0)
        tk.Label(self.master, padx=10,text="Folder").grid(row=1)
        tk.Label(self.master, padx=10,text="Podcast website root").grid(row=2)

        tk.Entry(self.master,width=70).grid(row=0, column=1,columnspan='8')
        tk.Entry(self.master,width=70).grid(row=1, column=1,columnspan='8')
        tk.Entry(self.master,width=70).grid(row=2, column=1,columnspan='8')


        self.simulate = tk.IntVar() 
        tk.Checkbutton(self.master, text="simulate", variable=self.simulate
                       ).grid(row=3,column=1,sticky='WE')
    

        tk.Button(self.master,text='Interrupt').grid(row=4,column=7,sticky='WE')
        tk.Button(self.master,text='Process', command =
                  self.process).grid(row=4,column=8,sticky='WE')


if __name__ == "__main__":
    root = tk.Tk() #create window
    root.title("Ydl - Youtube downloader")

    app = Interface(master=root) #create all components inside the window
    app.mainloop()
