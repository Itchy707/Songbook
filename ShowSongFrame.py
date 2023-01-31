import tkinter as tk
from BackEnd import *
import ConfigSongFrame
from tkinter import ttk
import re
import numpy as np
import subprocess
from LaTeXGenerator import *

if __name__ == "__main__":
    raise Exception("That is not main!")

class ShowSongFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__()
        
        # treeview
        columns = BackEnd.list_of_genres.copy()
        columns.insert(0, 'Autor')
        columns.insert(0, 'Název písně')
        columns.insert(0, 'ID')
        self.treeview = ttk.Treeview(parent, columns=columns, show='headings')
        
        self.__create_headings__(columns)
        self.treeview.grid(row=0, column=0, columnspan = 5, sticky='nsew')
        self.update_treeview()
        
        # Button for deleting a selected song
        self.delete_song_button = tk.Button(master=parent, text="Smazat píseň", command=lambda: self.__delete_item__(self))
        self.delete_song_button.grid(row=1, column=4)
        
        # Button for creating PDF file via LaTeX
        self.latex_song_button = tk.Button(master=parent, text="Vytvořit PDF", command=lambda: LaTeXGenerator.generate_file())
        self.latex_song_button.grid(row=1, column=3)
        
        # Doubleclick on heading sorts treeview by associated collumn
        self.treeview.bind('<Double-1>', self.__sort_items__)
        
        # Doubleclick on item allows to modify associated data
        self.treeview.bind('<Double-1>', self.__config_item__)
        
        
    # Deletes database and recreates it with fresh data
    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        for id, song in enumerate(BackEnd.song_list):
            song_row = [id, song[0], song[1]]
            for genre in BackEnd.list_of_genres:
                if song[2].__contains__(genre):
                    song_row.append('✔')
                else:
                    song_row.append(' ')
            song_row = tuple(song_row)
            self.treeview.insert('', 'end', values=song_row)
                    
    def __create_headings__(self, columns):
        for id, column in enumerate(columns):
            self.treeview.heading(columns[id], text=column)
            if id == 1 or id == 2: # for song name and song author make the column wider
                self.treeview.column(columns[id], stretch=tk.NO, width=150)
            else:
                self.treeview.column(columns[id], stretch=tk.NO, width=len(column)*10)
                
    def __delete_item__(self, event):
        item = self.treeview.selection()
        if len(item) != 1:
            return
        index = self.treeview.index(item)
        del BackEnd.song_list[index]
        self.update_treeview()
    
    
    # --works only for song name and song author; also makes differences between upper and lower case, which should be repaired
    # TODO    
    def __sort_items__(self, event):
        index = self.treeview.identify('column', event.x, event.y)
        index = re.findall('\d+', index)
        index = int(index[0]) - 2
        print(index)
        if index > 1 or index < 0:
            return
        a = np.array(BackEnd.song_list.copy())
        a = a[a[:, index].argsort()]
        BackEnd.song_list = list(a)
        self.update_treeview()
    
    # TODO
    def __config_item__(self, event):
        item = self.treeview.identify('item', event.x, event.y)
        item = self.treeview.index(item)
        print(item)
        child_w = ConfigSongFrame(parent=self)

        
        
    
        
                
    
