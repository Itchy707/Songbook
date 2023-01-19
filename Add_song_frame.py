import tkinter as tk
from tkinter.ttk import Separator
from BackEnd import *

if __name__ == "__main__":
    raise Exception("That is not main!")

class AddSongFrame(tk.LabelFrame):
    
    def __init__(self, parent):
        super().__init__()
        
        # name
        self.song_name_e = tk.Entry(parent, width=40)
        self.song_name_label = tk.Label(   parent,
                                   text="Název písně",
                                   font=('Times', 10, 'bold'))
        self.song_name_e.grid(row=0, column=1, columnspan=9, padx=5, pady=5)
        self.song_name_label.grid(row=0, column=0)

        # author
        self.song_author_e = tk.Entry(parent, width=40)
        self.song_author_e.grid(row=1, column=1, columnspan=9)
        self.song_author_label = tk.Label(parent,
                                  text="Autor písně",
                                  font=('Times', 10, 'bold')
                                  )
        self.song_author_label.grid(row=1, column=0)

        # generate genre checklabels
        row = 3
        genre_boxes = list()
        for genre in list_of_genres:
            self.check_label = tk.Label(parent,text=genre, font=('Times', 10), padx=5, pady=5)
            self.check_label.grid(row=row, column=0, sticky='W')
            checkb_var = tk.IntVar()
            self.checkb = tk.Checkbutton(parent,
                                 variable=checkb_var,                
                                )
            self.checkb.grid(row = row, column=1)
            genre_boxes.append(checkb_var)
            row = row + 1

        sep = Separator(parent, orient='horizontal')
        sep.grid(row=2, column=0, columnspan=11, sticky='ew', padx=5, pady=5)

        # button commands
        def Add_song_click():
            # global genre_boxes
            s_song_name = self.song_name_e.get()
            s_song_author = self.song_author_e.get()

            genres = list()
            genre_num = 0
            for g in genre_boxes: # get genres of current song to list
                if g.get() == 1:
                    genres.append(list_of_genres[genre_num])
                genre_num = genre_num + 1

            Add_song(s_song_name, s_song_author, genres)
            self.song_name_e.delete(0, tk.END),
            self.song_author_e.delete(0, tk.END),
            self.song_name_e.focus()

        # buttons
        Add_song_button = tk.Button(parent,
                                 text = "Přidat píseň",
                                 command=Add_song_click)
        Reset_button = tk.Button(parent,
                              text = "Zrušit výběr",
                              command=Reset_click)

        Add_song_button.grid(row=5, column=9)
        Reset_button.grid(row=6, column=9)