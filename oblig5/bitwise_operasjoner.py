import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bitwise operators")

        self.first_number_label = tk.Label (
            self.root, 
            text="First number, range 0-255"
        )
        self.first_number_entry = tk.Entry(self.root, width=3)
        self.first_number_label.grid(row=0, column=0, sticky=tk.W)
        self.first_number_entry.grid(row=0, column=1)

        self.first_number_bit_label = tk.Label(self.root)
        self.first_number_bit_label.grid(row=0, column=2)

        self.second_number_label = tk.Label (
            self.root, 
            text="Second number, range 0-255"
        )
        self.second_number_entry = tk.Entry(self.root, width=3)
        self.second_number_label.grid(row=1, column=0)
        self.second_number_entry.grid(row=1, column=1)

        self.second_number_bit_label = tk.Label(self.root)
        self.second_number_bit_label.grid(row=1, column=2)

        self.create_info_label()

        self.user_answer_label = tk.Label (
            self.root, 
            text="Your answer"
        )
        self.user_answer_entry = tk.Entry(self.root, justify="center", width=8)
        self.user_answer_label.grid(row=2, column=0, sticky=tk.W)
        self.user_answer_entry.grid(row=2, column=2)

        self.correct_answer_label_prefix = tk.Label (
            self.root, 
            text="Correct answer"
        )
        self.correct_answer_label = tk.Label(self.root)
        self.correct_answer_label_prefix.grid(row=3, column=0, sticky=tk.W)
        self.correct_answer_label.grid(row=3, column=2)


        combobox_values = [
            "Select operator...", 
            "AND", 
            "OR", 
            "OCOMP", 
            "XOR", 
            "SHIFTLEFT", 
            "SHIFTRIGHT"
        ]
        self.combobox = ttk.Combobox(self.root)
        self.combobox.grid(row=2, column=3)
        self.combobox["values"] = combobox_values
        self.combobox["state"] = "readonly"
        self.combobox.current(0)

        self.check_button = tk.Button(text="Check", command=self.check)
        self.check_button.grid(row=2, column=4)

        self.first_number_entry.bind(
            "<FocusOut>", self.update_first_bit_label
        )
        self.second_number_entry.bind(
            "<FocusOut>", self.update_second_bit_label
        )

        self.invalid_input_label = tk.Label(self.root)
        self.invalid_input_label.grid(row=3, column=3)

        self.root.mainloop()
    
    def update_first_bit_label(self, event):
        try:
            first_number = int( self.first_number_entry.get() )
            if self.is_valid(first_number):

                self.first_number_bit_label["text"] = f"{first_number:08b}"
            else:
                self.invalid_value()
        except ValueError:
            self.invalid_value()

    def update_second_bit_label(self, event):
        try:
            second_number = int( self.second_number_entry.get() )
            if self.is_valid(second_number):
                self.second_number_bit_label["text"] = f"{second_number:08b}"
            else:
                self.invalid_value()
        except ValueError:
            self.invalid_value()
    
    def create_info_label(self):
            self.info_label = tk.Label(
            self.root, 
            text="Only this for SHIFTRIGHT(1), SHIFTLEFT(1), OCOMP",
            fg = "black"
        )
            self.info_label.grid(row=0, column=3)
    
    def is_valid(self, number):
        if number >= 0 and number <= 255:
            return True
        else:
            return False
    
    def invalid_value(self):
        self.invalid_input_label["fg"] = "red"
        self.invalid_input_label["text"] = "Enter integer(s) in range 0-255"

    def check(self):
        try:
            self.user_answer_entry["bg"] = "white"
            first_number  = int( self.first_number_entry.get() )
            second_number = int( self.second_number_entry.get() )

        except ValueError:
            self.invalid_value()

        else:
            try:
                self.invalid_input_label.config(text="")
                if (
                    self.is_valid(first_number) 
                    and 
                    self.is_valid(second_number)
                ):
                    if self.combobox.get() == "AND":
                        correct_answer = first_number & second_number
                        correct_answer = f"{correct_answer:08b}"
                        self.correct_answer_label["text"] = correct_answer 

                    elif self.combobox.get() == "OR":
                        correct_answer = first_number | second_number
                        correct_answer = f"{correct_answer:08b}"
                        self.correct_answer_label["text"] = correct_answer
                    
                    elif self.combobox.get() == "OCOMP":
                        correct_answer = ~first_number & 255
                        correct_answer = f"{correct_answer:08b}"
                        self.correct_answer_label["text"] = correct_answer

                    elif self.combobox.get() == "XOR":
                        correct_answer = first_number ^ second_number
                        correct_answer = f"{correct_answer:08b}"
                        self.correct_answer_label["text"] = correct_answer

                    elif self.combobox.get() == "SHIFTLEFT":
                        #Bildet i oppgaven viser SHIFTLEFT(1)
                        correct_answer = first_number << 1 & 255
                        correct_answer = f"{correct_answer:08b}"
                        self.correct_answer_label["text"] = correct_answer

                    elif self.combobox.get() == "SHIFTRIGHT":
                        #Bildet i oppgaven viser SHIFTRIGHT(1)
                        correct_answer = first_number >> 1
                        correct_answer = f"{correct_answer:08b}"
                        self.correct_answer_label["text"] = correct_answer

                    user_answer = self.user_answer_entry.get()
                    if user_answer == correct_answer:
                        self.user_answer_entry["bg"] = "green"
                    elif user_answer != correct_answer:
                        self.user_answer_entry["bg"] = "red"
                else:
                    self.invalid_value()
            except UnboundLocalError:
                self.invalid_input_label.config(text="")
                self.invalid_input_label["fg"] = "red"
                self.invalid_input_label["text"]= "Select an operator"

GUI()