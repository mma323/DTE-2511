import tkinter as tk
from tkinter import ttk

#"Select a shape" vises først i combobox
SHAPES = ["Select a shape...", "rectangle", "oval", "arc", "polygon", "line"]

class Window:
    def __init__(self):
        self.window = tk.Tk()

        self.window.geometry("300x200")
        self.window.resizable(False, False)
        self.window.title("Select shapes")

        self.selected_shape = tk.StringVar()
        self.selected_shape.set(SHAPES[0])

        self.shapes_combobox = ttk.Combobox(
                                            self.window, 
                                            textvariable=self.selected_shape
            )
        self.shapes_combobox["state"] = "readonly"
        self.shapes_combobox["values"] = SHAPES
        self.shapes_combobox.pack(fill=tk.X, padx=5, pady=5)

        self.canvas_for_shapes = tk.Canvas(self.window, bg="white")
        self.canvas_for_shapes.pack()
        
        self.shapes_combobox.bind("<<ComboboxSelected>>", self.display_shape)

        self.window.mainloop()

    def display_shape(self, event):
        selected_shape = self.selected_shape.get()
        canvas = self.canvas_for_shapes
        canvas.delete("all")
        
        if selected_shape == "rectangle":
            coordinates = 30, 20, 270, 150
            canvas.create_rectangle(coordinates)

        elif selected_shape == "oval":
            coordinates = 30, 20, 270, 150
            canvas.create_oval(coordinates, fill="red")

        elif selected_shape == "arc":
            coordinates = 100, 120, 280, 15
            canvas.create_arc(coordinates, fill="red", width=5)

        elif selected_shape == "polygon":
            coordinates = 0, 0, 100, 100, 150, 50
            canvas.create_polygon(coordinates)
        
        elif selected_shape == "line":
            coordinates = 10, 50, 240, 120
            canvas.create_line(coordinates)

Window()