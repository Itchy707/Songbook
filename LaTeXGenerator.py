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
    
    # variable to create Songbook.tex file
    __documentclass__ = "article"
    __packages__ = [["babel", "czech"], ["fontenc", "T1"], ["booktabs"], ["inputenc", "cp1250"], ["amssymb"]]
    
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
    def __generate_songs_string__():
        space = ' & '
        songs = list()
        for song in BackEnd.song_list:
            song_line = song[0] + space + song[1] # add song name and song author
            for genre in BackEnd.list_of_genres:
                if song[2].__contains__(genre):
                    song_line += space + ("  $$\\checkmark$$  ")
                else:
                    song_line += space + ("     ")
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
            
                         
             
                        
    