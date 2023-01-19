import tkinter as tk
import csv

# variables
song_list = list()

#genres
list_of_genres = ["Folk",
                  "Rock",
                  "Rap",]

# Get songs from file (init)
def Get_songs(file_name):
    global song_list
    with open(file_name) as csv_file:
        song_list = list(csv.reader(csv_file, delimiter=","))   

# Save songs to file
def Save_songs(file_name):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for song in song_list:
            if len(song) == 2:
                new = [song[0], song[1]]
            else:    
                new = [song[0], song[1], song[2]]
            writer.writerow(new)
       
# Generate genre stream for current song
def Generate_genre_stream():
    pass     

# Add song
def Add_song(song_name, song_author, genres):
    if song_name != '' and song_author != '':
        song_stream = [song_name, song_author, genres]
        song_list.append(song_stream)
        

# Reset
def Reset_click():
    pass
    print(song_list)
    
    
    


