import tkinter as tk
import functools as funct
from tkinter.ttk import Separator
from BackEnd import *
from ShowSongFrame import *

if __name__ == "__main__":
    raise Exception("That is not main!")

class AddSongFrame(tk.LabelFrame):
    
    def __init__(self, parent, add_function):
        super().__init__()
        
        root = parent
        self.add_function = add_function
        # song name entry and label
        self.song_name_e = tk.Entry(root, width=40)
        self.song_name_label = tk.Label(root,
                                        text="Název písně",
                                        font=('Times', 10, 'bold'))
        self.song_name_e.grid(row=0, column=1, columnspan=9, padx=5, pady=5)
        self.song_name_label.grid(row=0, column=0)

        # song author entry and label
        self.song_author_e = tk.Entry(root, width=40)
        self.song_author_e.grid(row=1, column=1, columnspan=9)
        self.song_author_label = tk.Label(root,
                                  text="Autor písně",
                                  font=('Times', 10, 'bold')
                                  )
        self.song_author_label.grid(row=1, column=0)

        # generate genre checklabels from Backend
        row = 3
        self.genre_boxes = list()
        for genre in BackEnd.list_of_genres:
            self.check_label = tk.Label(root,text=genre, font=('Times', 10), padx=5, pady=5)
            self.check_label.grid(row=row, column=0, sticky='W')
            checkb_var = tk.IntVar()
            checkb = tk.Checkbutton(root,
                                    variable=checkb_var,                
                                    )
            checkb.grid(row = row, column=1)
            self.genre_boxes.append(checkb_var)
            row = row + 1

        # Separating line between entries and genre checkboxes
        self.sep = Separator(root, orient='horizontal')
        self.sep.grid(row=2, column=0, columnspan=11, sticky='ew', padx=5, pady=5)
        
        # buttons
        self.Add_song_button = tk.Button(root,
                             text = "Přidat píseň",
                             command= lambda: self.Add_song_click())
        self.Reset_button = tk.Button(root,
                          text = "Zrušit výběr",
                          command= lambda: self.Reset_click())
        self.Add_song_button.grid(row=5, column=9)
        self.Reset_button.grid(row=6, column=9)

        # binds
        self.song_name_e.bind('<Down>', self.downKey)
        self.song_author_e.bind('<Up>', self.upKey)
        self.song_name_e.bind('<Return>', self.enterKey)
        self.song_author_e.bind('<Return>', self.enterKey)
        
        self.song_name_e.bind('<Control-Key-1>', lambda event: self.controlKey(self, number=0))
        self.song_author_e.bind('<Control-Key-1>', lambda event: self.controlKey(self, number=0))
        self.song_name_e.bind('<Control-Key-2>', lambda event: self.controlKey(self, number=1))
        self.song_author_e.bind('<Control-Key-2>', lambda event: self.controlKey(self, number=1))
        self.song_name_e.bind('<Control-Key-3>', lambda event: self.controlKey(self, number=2))
        self.song_author_e.bind('<Control-Key-3>', lambda event: self.controlKey(self, number=2))
        self.song_name_e.bind('<Control-Key-4>', lambda event: self.controlKey(self, number=3))
        self.song_author_e.bind('<Control-Key-4>', lambda event: self.controlKey(self, number=3))
        self.song_name_e.bind('<Control-Key-5>', lambda event: self.controlKey(self, number=4))
        self.song_author_e.bind('<Control-Key-5>', lambda event: self.controlKey(self, number=4))
        self.song_name_e.bind('<Control-Key-6>', lambda event: self.controlKey(self, number=5))
        self.song_author_e.bind('<Control-Key-6>', lambda event: self.controlKey(self, number=5))
        self.song_name_e.bind('<Control-Key-7>', lambda event: self.controlKey(self, number=6))
        self.song_author_e.bind('<Control-Key-7>', lambda event: self.controlKey(self, number=6))
        self.song_name_e.bind('<Control-Key-8>', lambda event: self.controlKey(self, number=7))
        self.song_author_e.bind('<Control-Key-8>', lambda event: self.controlKey(self, number=7))
        self.song_name_e.bind('<Control-Key-9>', lambda event: self.controlKey(self, number=8))
        self.song_author_e.bind('<Control-Key-9>', lambda event: self.controlKey(self, number=8))
        self.song_name_e.bind('<Control-Key-0>', lambda event: self.controlKey(self, number=9))
        self.song_author_e.bind('<Control-Key-0>', lambda event: self.controlKey(self, number=9))
        

    # button commands
    def Add_song_click(self):
        # global genre_boxes
        s_song_name = self.song_name_e.get()
        s_song_author = self.song_author_e.get()
        genres = list()
        genre_num = 0
        for g in self.genre_boxes: # get genres of current song to list
            if g.get() == 1:
                genres.append(BackEnd.list_of_genres[genre_num])
            genre_num = genre_num + 1
        BackEnd.Add_song(s_song_name, s_song_author, genres)
        self.song_name_e.delete(0, tk.END),
        self.song_author_e.delete(0, tk.END),
        self.song_name_e.focus()
        if self.add_function != None:
            self.add_function()        
        
        
    # Reset
    def Reset_click(self):
        print(BackEnd.song_list)
        
    # hotkey binds
    def downKey(self, event):
        self.song_author_e.focus()

    def upKey(self, event):
        self.song_name_e.focus()

    def enterKey(self, event):
        if self.song_author_e.get() == '':
            self.song_author_e.focus()
        else:
            self.Add_song_click()
            self.add_function()
    
    
    # by pressing ctrl+<number> select genre
    # TODO
    def controlKey(self, event, number):
        print("s")
        if number < len(self.genre_boxes):
            self.genre_boxes[number].set((self.genre_boxes[number].get() + 1) % 2)
        