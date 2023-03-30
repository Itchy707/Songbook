import subprocess
from BackEnd import *

if __name__ == "__main__":
    raise Exception("That is not Main!")

class LaTeXGenerator: # static class
   
   # variables to create Songs.tex file 
    __section_string__ = "\\section{Seznam písní}\n"
    __songs__ = list()
    __table_header__ = str()
    __table_beggining__ = ["\n\\begin{table}[htbp]", 
                           "\n\\centering",
                           "\n\\begin{tabular}{l|l" + "".join( "|c" for i in range(len(BackEnd.list_of_genres))) + "}"
                           ]
    __table_ending__ = ["\n\\end{tabular}",
                        "\n\\end{table}"
                        ]
    __max_string_length__ = 20
    
    # variables to create Songbook.tex file
    __documentclass__ = "article"
    __documentclass_params__ = ["", # font size
                                "", # paper size and format
                                "", # draft mode 
                                "", # multiple columns
                                "", # formula-specific options
                                "", # oneside/twoside
                                "", # titlepage behav
                                "", # chapter opening page
                                ]
    
    __packages__ = [["babel", "czech"],
                    ["fontenc", "T1"],
                    ["booktabs"],
                    ["inputenc", "cp1250"],
                    ["amssymb"],
                    ["geometry", "total={7in, 10.5in}"]]
    
    @staticmethod
    def __generate_table_header__():
        space = ' & '
        header = str()
        header += "\n\\textbf{Jméno písně}" + space
        header += "\\textbf{Autor písně}"
        for genre in BackEnd.list_of_genres:
            header += space + "\\textbf{" + genre + "}"
        header += "\\\\ \n\\midrule\n"
        LaTeXGenerator.__table_header__ = header
    
    @staticmethod
    #TODO
    # make it work for longer strings
    def __generate_songs_string__():
        songs = list()
        for song in BackEnd.song_list:
            if len(song[0]) > LaTeXGenerator.__max_string_length__ or len(song[1]) > LaTeXGenerator.__max_string_length__:
                song_line = LaTeXGenerator.__make_multiple_lines__(song)
            else: 
                song_line = song[0] + ' & ' + song[1] # add song name and song author
                for genre in BackEnd.list_of_genres:
                    if song[2].__contains__(genre):
                        song_line += ' & ' + ("  $$\\checkmark$$  ")
                    else:
                        song_line += ' & ' + ("     ")
                song_line += "\\\\\n"
            songs.append(song_line)
        LaTeXGenerator.__songs__ = songs
    
    @staticmethod
    def generate_file():
        LaTeXGenerator.generate_songbook_tex()
        LaTeXGenerator.__generate_table_header__()
        LaTeXGenerator.__generate_songs_string__()
        with open("Songs.tex", 'w') as f:
            f.write(LaTeXGenerator.__section_string__)
            f.writelines(LaTeXGenerator.__table_beggining__)
            f.write(LaTeXGenerator.__table_header__)
            f.writelines(LaTeXGenerator.__songs__)
            f.writelines(LaTeXGenerator.__table_ending__)
        subprocess.run(['pdflatex', "Songbook.tex"])
    
    @staticmethod
    def generate_table():
        LaTeXGenerator.__generate_table_header__()
        LaTeXGenerator.__generate_songs_string__()
        
    @staticmethod
    def generate_songbook_tex():
        package_string = str()
        for package in LaTeXGenerator.__packages__:
            if len(package) == 1:
                package_string += "\\usepackage{" + package[0] + "}\n"
            elif len(package) == 2:
                package_string += "\\usepackage[" + package[1] + "]{" + package[0] + "}\n"
            else:
                raise Exception("Too many package params!")
        with open("Songbook.tex", 'w') as f:
            f.write("\\documentclass{" + LaTeXGenerator.__documentclass__ + "}\n")
            f.write(package_string)
            f.write("\\begin{document}\n")
            f.write("\\include{Songs.tex}\n")
            f.write("\\end{document}")
            
            
    # TODO
    @staticmethod
    def __make_multiple_lines__(song):
        # separate song author and name by space
        # TODO make it separate by space AND by amount of chars, so it can reduce amount of needed columns
        name = song[0].split()
        author = song[1].split()
        
        for part in name:
            pass
        
        song_line = ''
        for row in range(max(len(name), len(author))):
            # each word is reparated into rows
            try:
                song_line += name[row] + ' & '
            except IndexError:
                song_line += ' & '
            try:
                song_line += author[row]
            except IndexError:
                song_line += ''
            
            # fill 1st row with genre checkmarks
            for genre in BackEnd.list_of_genres:
                    if song[2].__contains__(genre) and row == 0:
                        song_line += ' & ' + ("  $$\\checkmark$$  ")
                    else:
                        song_line += ' & ' + ("     ")
                
                
            song_line += '\\\\\n'
        
        return song_line    
        
        
        
         
            