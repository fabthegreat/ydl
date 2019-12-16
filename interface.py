import tkinter as tk
import os

class Interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_command(self):
        command = 'python core.py'
        for key in self.args:
            if bool(self.args[key].get()):
                print('{}: Option non vide'.format(key))
            else:
                print('{}: Option vide'.format(key))

        print(command)
        return command

    def process_window(self,command):
        term_window = tk.Toplevel(self.master,height='600',width='600')
        term_window.title("Process in progress")
        wid = term_window.winfo_id()
        for key,value in self.args.items():
            print('{} : {}'.format(key,value.get()))
        os.system('xterm -into {} -geometry 400x200 -hold -sb -e \'{}\' &'.format(wid,command))

    def create_widgets(self):
#
        tk.Label(self.master, padx=10,text="Youtube URL",bg="red").grid(row=0)
        tk.Label(self.master, padx=10,text="Folder").grid(row=1)
        tk.Label(self.master, padx=10,text="Podcast website root").grid(row=2)

        self.youtube_url = tk.StringVar()
        self.dir = tk.StringVar()
        self.url = tk.StringVar()

        tk.Entry(self.master,width=70, textvariable = self.youtube_url).grid(row=0, column=1,columnspan='8')
        tk.Entry(self.master,width=70, textvariable = self.dir).grid(row=1, column=1,columnspan='8')
        tk.Entry(self.master,width=70, textvariable = self.url).grid(row=2, column=1,columnspan='8')

        self.simulate = tk.IntVar()
        self.feed = tk.IntVar()
        self.video = tk.IntVar()

        tk.Checkbutton(self.master, text="simulate", variable=self.simulate).grid(row=3,column=1,sticky='WE')
        tk.Checkbutton(self.master, text="feed", variable=self.feed).grid(row=3,column=2,sticky='WE')
        tk.Checkbutton(self.master, text="video only", variable=self.video).grid(row=3,column=3,sticky='WE')

        self.args = {'youtube_url':self.youtube_url,'dir':self.dir,'url':self.url,'simulate':self.simulate,'feed':self.feed,'video':self.video}

        tk.Button(self.master,text='Interrupt').grid(row=4,column=7,sticky='WE')
        tk.Button(self.master,text='Process', command = lambda: self.process_window(self.create_command())).grid(row=4,column=8,sticky='WE')


if __name__ == "__main__":
    root = tk.Tk() #create window
    root.title("Ydl - Youtube downloader")

    app = Interface(master=root) #create all components inside the window
    app.mainloop()
