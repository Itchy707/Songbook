import tkinter as tk
from BackEnd import *
from tkinter import ttk


if __name__ == "__main__":
    raise Exception("That is not main!")

class ShowSongFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__()
        
        # treeview
        columns = BackEnd.list_of_genres
        columns.insert(0, 'Autor')
        columns.insert(0, 'Název písně')
        columns.insert(0, 'ID')
        self.treeview = ttk.Treeview(parent, columns=columns, show='headings')
        
        self.create_headings(columns)
        self.treeview.grid(row=0, column=0, columnspan = 5, sticky='nsew')
        self.update_treeview()
        
        # buttons
        self.delete_song_button = tk.Button(master=parent, text="Smazat píseň", command=self.delete_item)
        self.delete_song_button.grid(row=1, column=4)
    
    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        for id, song in enumerate(BackEnd.song_list):
            self.treeview.insert('', 'end', values=(id, song[0], song[1]))
        
    def create_headings(self, columns):
        for id, column in enumerate(columns):
            self.treeview.heading(columns[id], text=column)
            if id == 1 or id == 2: # for song name and song author make the column wider
                self.treeview.column(columns[id], stretch=tk.NO, width=150)
            else:
                self.treeview.column(columns[id], stretch=tk.NO, width=len(column)*10)
                
    def delete_item(self):
        item = self.treeview.selection()[0]
        print(item)
        self.treeview.delete(item)
        self.update_treeview()
                
    