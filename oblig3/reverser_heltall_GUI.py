import tkinter as tk
from reverser_heltall import *

def reverse_integer_helper():
    try:
        integer_reversed_entry.configure(state="normal")
        integer = int( integer_entry.get() )
        integer_reversed = reverse_integer(integer)
        integer_reversed_entry.delete(0, "end")
        integer_reversed_entry.insert( 0, str(integer_reversed) )
        integer_reversed_entry.configure(state="readonly")
    except ValueError:
        integer_reversed_entry.configure(state="normal")
        integer_reversed_entry.delete(0, "end")
        integer_reversed_entry.insert( 0, "Skriv inn et heltall" )
        integer_reversed_entry.configure(state="readonly")

root = tk.Tk()
root.geometry('300x90')
root.resizable(False, False)
root.title('Reverse integer')

integer_entry = tk.Entry(
    root,
    text="Enter integer: "
)

integer_entry.pack()

reverse_button = tk.Button(
    root,
    text='Reverse',
    command=reverse_integer_helper
)
reverse_button.pack()
integer_reversed_entry = tk.Entry(root, state="readonly")
integer_reversed_entry.pack()

root.mainloop()