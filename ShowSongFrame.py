import tkinter as tk
from BackEnd import *


class ShowSongFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__()
        
        self.scroll = tk.Scrollbar(parent)
        self.scroll.grid(row=5, column=0)
        
        self.l = tk.Listbox(parent, yscrollcommand=self.scroll.set)
    
    
    def __create_labels__():
        pass