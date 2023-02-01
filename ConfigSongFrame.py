import tkinter as tk
from BackEnd import *



class EntryPopup(tk.Entry):

    def __init__(self, parent, text, index, column, destr_func):
        super().__init__(parent)
        self.tv = parent
        self.index = index
        self.column = column
        self.destr_func = destr_func

        self.insert(0, text) 
        # self['state'] = 'readonly'
        # self['readonlybackground'] = 'white'
        # self['selectbackground'] = '#1BA1E2'
        self['exportselection'] = False

        self.focus_force()
        self.bind('<Return>', self.on_return)
        self.bind('<Escape>', lambda *ignore: self.destroy())

    def on_return(self, event):
        if self.index < 2: # edit song name or song author
            BackEnd.song_list[self.index][self.column] = self.get()
        else: # edit genre
            pass
            # if BackEnd.song_list[self.index][self.column] == 
        self.destr_func()
        self.destroy()
            
    def __del__(self):
        pass