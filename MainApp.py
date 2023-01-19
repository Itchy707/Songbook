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
        self.geometry('700x500')
        
        # frames
        self.add_frame = AddSongFrame(parent=self)
        self.show_frame = ShowSongFrame(parent=self)
        #self.add_frame.grid(padx=10, pady=10)
        
        # hotkey binds
        def downKey(event):
            self.add_frame.song_author_e.focus()

        def upKey(event):
            self.add_frame.song_name_e.focus()

        def enterKey(event):
            if self.add_frame.song_author_e.get() == '':
                self.add_frame.song_author_e.focus()
            else:
                Add_song_click()

        # binds
        self.bind('<Down>', downKey)
        self.bind('<Up>', upKey)
        self.bind('<Return>', enterKey)
        
        self.add_frame.song_name_e.focus()
    
    
MainApp = App()
# if __name__ != '__main__':
Get_songs("songs.csv")
#MainApp.add_frame.song_name_e.focus()
MainApp.mainloop()
Save_songs("songs.csv")

