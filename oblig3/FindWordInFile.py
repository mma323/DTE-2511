import os
import tkinter as tk

def main():

    def search():
        get_occurences.directory_count = 0
        get_occurences.file_count = 0
        text_area.delete("1.0", "end")
        text_area.insert("end", "Search start.\n")
        text_area.insert("end", "-----------------------------------------\n")
        path = ( path_entry.get() ).strip()   
        word = word_entry.get()
        word = word.lower()
        occurences = get_occurences(path, word)
        text_area.insert(
            "end", 
            f"Directories: {get_occurences.directory_count} " 
            + f"Files: {get_occurences.file_count} " 
            + f"Occurences of word:{occurences}\n"
        )
        text_area.insert("end", "-----------------------------------------\n")
        text_area.insert("end", "Search end.")

    def replace_punctuation(string):
        for character in string:
            if character in "~@#$%^&*()_-+=~<>?/,.;:![]|'\"":
                string = string.replace(character, " ")
        return string

    def find_word(path, word):
        file = open(path, "r")
        occurences = 0
        line_number = 0
        for line in file:
            line_number += 1
            line = line.lower() 
            line = replace_punctuation(line)
            words = line.split()
            occurences += words.count(word)
            if word in words:
                text_area.insert("end", f"{path}    Line: {line_number}\n")
        file.close
        return occurences

    def get_occurences(path, word):
        try:
            occurences = 0

            if not os.path.isfile(path):
                get_occurences.directory_count += 1
                directory_list = os.listdir(path) 
                for subdirectory in directory_list:
                    occurences += (
                        get_occurences(path + "\\" + subdirectory, word) 
                    )
                    
            else: 
                get_occurences.file_count += 1
                occurences += find_word(path, word)

            return occurences
        except FileNotFoundError:
            text_area.insert("end", "File not found, type an existing path\n")


    gui = tk.Tk()
    path_entry_label = tk.Label(gui, text="Path: ")
    path_entry_label.pack(side=tk.LEFT)
    path_entry = tk.Entry(gui)
    path_entry.pack(side=tk.LEFT)

    word_entry_label = tk.Label(gui, text="Word: ")
    word_entry_label.pack(side=tk.LEFT)
    word_entry = tk.Entry(gui)
    word_entry.pack(side=tk.LEFT)

    search_button = tk.Button(gui, text="Search", command=search)
    search_button.pack(side=tk.LEFT)

    text_area = tk.Text(gui)
    text_area.pack()


    gui.mainloop()

if __name__ == "__main__":
    main() 