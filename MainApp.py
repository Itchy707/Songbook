import tkinter as tk

from tkinter.ttk import Separator

from BackEnd import *

from Add_song_frame import *

from ShowSongFrame import *

import os 


if __name__ != '__main__':
    raise Exception("File is not Main")

class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Songbook")
        self.geometry('1300x600')

        # Frame with ttk.treeview to show and handle present songs
        self.show_frame = tk.LabelFrame(master=self, text="Seznam písní", padx=10, pady=10)
        self.show_frame.grid(row=0, column=1, padx=10, pady=10)
        self.show_frame_content = ShowSongFrame(parent=self.show_frame)

        # Frame for adding a song
        self.add_frame = tk.LabelFrame(master=self, text="Přidat píseň", padx=10, pady=10)
        self.add_frame.grid(row=0, column=0, padx=10, pady=10)
        self.add_frame_content = AddSongFrame(parent=self.add_frame,
                                              add_function=self.show_frame_content.update_treeview) # junk way to keep ttk.treeview up to date when song is added
        
        self.add_frame_content.song_name_e.focus()
    

BackEnd.Get_songs('songs.csv')

MainApp = App()
MainApp.add_frame_content.song_name_e.focus()
MainApp.mainloop()

BackEnd.Save_songs("songs.csv")


