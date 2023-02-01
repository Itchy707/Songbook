import tkinter as tk
import csv

class BackEnd: # static class
    
    
    # variables
    song_list = list()
    list_of_genres =    ["Punk",
                        "Rock",
                        "Táborové",
                        "Anglické",
                        "Smutné",
                        "Odrhovačka"]

    # Get songs from file (init)
    @staticmethod
    def Get_songs(file_name):
        with open(file_name) as csv_file:
            BackEnd.song_list = list(csv.reader(csv_file, delimiter=","))   

    # Save songs to file
    @staticmethod
    def Save_songs(file_name):
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for song in BackEnd.song_list:
                if len(song) == 2:
                    new = [song[0], song[1]]
                else:    
                    new = [song[0], song[1], song[2]]
                writer.writerow(new)

    # Generate genre stream for current song
    @staticmethod
    def Generate_genre_stream():
        pass     

    # Add song
    @staticmethod
    def Add_song(song_name, song_author, genres):
        if song_name != '' and song_author != '':
            song_stream = [song_name, song_author, genres]
            BackEnd.song_list.append(song_stream)
            

    
    


