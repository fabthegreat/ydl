import tkinter as tk
from tkinter import filedialog
import os
import sys

class Interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_command(self):
        if os.path.split(sys.argv[0])[1] == 'core.py':
            command = 'python {}'.format(os.path.abspath(sys.argv[0]))
        else:
            command = '{}'.format(os.path.abspath(sys.argv[0]))

        for key in self.args:
            if bool(self.args[key].get()):
                print('{}: Option non vide'.format(key))
                if self.args[key].get() in [0,1]:
                    value = ''
                else:
                    value = '\'{}\''.format(self.args[key].get())
                command = '{} --{} {}'.format(command,key,value)
            else:
                print('{}: Option vide'.format(key))

        print(command)
        return command

    def process_window(self,command):
        term_window = tk.Toplevel(self.master,height='600',width='600')
        term_window.title("YDL: process in progress")
        wid = term_window.winfo_id()
        for key,value in self.args.items():
            print('{} : {}'.format(key,value.get()))
        system_command = 'xterm -into {} -geometry 400x200 -hold -sb -e \"{}\" &'.format(wid,command)
        print(system_command)
        os.system(system_command)

    def select_directory(self):
        folder_selected = filedialog.askdirectory()
        self.dir.set(folder_selected)

    def create_widgets(self):

        tk.Label(self.master, padx=10,text="Youtube URL",bg="red").grid(row=0,columnspan='1')
        tk.Label(self.master, padx=10,text="Folder").grid(row=1,columnspan='1')
        tk.Label(self.master, padx=10,text="Podcast website root").grid(row=2,columnspan='1')

        # Vars attached to args
        self.youtube_url = tk.StringVar()
        self.dir = tk.StringVar() 
        self.podcast_url = tk.StringVar()
        self.simulate = tk.IntVar()
        self.feed = tk.IntVar()
        self.video = tk.IntVar()

        # Default values
        # TODO: 
        self.youtube_url.set('https://www.youtube.com/watch?v=xJO5GstqTSY&list=PLxzM9a5lhAumFRpcigmGY1QLDYxb4-P2B')
        self.dir.set('~/Vidéos')
        self.podcast_url.set('podcast.lutix.org')

        tk.Entry(self.master,width=70,textvariable = self.youtube_url).grid(row=0, column=1,columnspan='8',sticky='W')
        tk.Entry(self.master, textvariable = self.dir).grid(row=1, column=1,columnspan='6',sticky='WE')
        tk.Entry(self.master,width=70, textvariable = self.podcast_url).grid(row=2, column=1,columnspan='8',sticky='W')
        tk.Checkbutton(self.master, text="simulate", variable=self.simulate).grid(row=3,column=1,sticky='WE')
        tk.Checkbutton(self.master, text="feed", variable=self.feed).grid(row=3,column=2,sticky='WE')
        tk.Checkbutton(self.master, text="video only", variable=self.video).grid(row=3,column=3,sticky='WE')

        self.args = {'youtube_url':self.youtube_url,'dir':self.dir,'podcast_url':self.podcast_url,'simulate':self.simulate,'feed':self.feed,'video':self.video}


        tk.Button(self.master,text='Choose folder', command = self.select_directory).grid(row=1,column=8,sticky='WE')
        tk.Button(self.master,text='Process', command = lambda: self.process_window(self.create_command())).grid(row=4,column=8,sticky='WE')


if __name__ == "__main__":
    root = tk.Tk() #create window
    root.title("Ydl - Youtube downloader")

    app = Interface(master=root) #create all components inside the window
    app.mainloop()
