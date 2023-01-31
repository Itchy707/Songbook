import tkinter as tk

from tkinter.ttk import Separator

from BackEnd import *

from Add_song_frame import *

from ShowSongFrame import *


if __name__ != '__main__':
    raise Exception("File is not Main")

class App(tk.Tk):
    

    def __init__(self):

        super().__init__()

        self.title("Songbook")
        self.geometry('1100x500')

        # Frame for adding a song
        self.add_frame = tk.LabelFrame(master=self, text="Přidat píseň", padx=10, pady=10)
        self.add_frame.grid(row=0, column=0, padx=10, pady=10)
        self.add_frame_content = AddSongFrame(parent=self.add_frame)
        
        # Frame with ttk.treeview to show and handle present songs
        self.show_frame = tk.LabelFrame(master=self, text="Seznam písní", padx=10, pady=10)
        self.show_frame.grid(row=0, column=1, padx=10, pady=10)
        self.show_frame_content = ShowSongFrame(parent=self.show_frame)
        
        # junk way to keep ttk.treeview up to date when song is added
        self.add_frame_content.add_function = self.show_frame_content.update_treeview

        # hotkey binds
        def downKey(event):
            self.add_frame_content.song_author_e.focus()

        def upKey(event):
            self.add_frame_content.song_name_e.focus()

        def enterKey(event):
            if self.add_frame_content.song_author_e.get() == '':
                self.add_frame_content.song_author_e.focus()
            else:
                self.add_frame_content.Add_song_click()
                self.show_frame_content.update_treeview()

        # binds
        self.bind('<Down>', downKey)
        self.bind('<Up>', upKey)
        self.bind('<Return>', enterKey)
        
        self.add_frame_content.song_name_e.focus()
    

BackEnd.Get_songs("songs.csv")

MainApp = App()
MainApp.add_frame_content.song_name_e.focus()
MainApp.mainloop()

BackEnd.Save_songs("songs.csv")


