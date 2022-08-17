#Hentet fra løsningsforslag, modifisert i ettertid
import tkinter as tk 
from gift_wrapping import *

def add(event):
    points.append([event.x, event.y])
    repaint()

def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()

def repaint():
    canvas.delete("point")
    if len(points) > 0:
        canvas.create_polygon(
            get_convex_hull(points), 
            fill = "gray", 
            tags = "point"
        )

    for [x, y] in points:
        canvas.create_oval(
            x - radius, 
            y - radius,
            x + radius,
            y + radius,
            tags = "point"
        )
    
def display_instructions():
    instructions = [
        "INSTRUCTIONS", 
        "Add:", 
        "Left Click", 
        "Remove:", 
        "Right Click"
    ]
    x = 20
    y = 20
    canvas.create_rectangle(
        x, 
        y, 
        x + 160, 
        y + 80
    )
    canvas.create_text(
        x + 10 + 40, 
        y + 20, 
        text = instructions[0], 
        justify = tk.CENTER
    )
    for i in range(1, len(instructions), 2):
        canvas.create_text(
            x + 10 + 40, 
            y + 20 + (i + 1) * 10, 
            text = instructions[i], 
            justify = tk.RIGHT
        )
        canvas.create_text(
            x + 80 + 40, 
            y + 20 + (i + 1) * 10, 
            text = instructions[i + 1], 
            justify = tk.RIGHT
        )


window = tk.Tk() # Create a window
window.title("Convex Hull") # Set title

width = 500
height = 150
radius = 2
canvas = tk.Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

display_instructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)

window.mainloop() # Create an event loop
