import tkinter as tk
from math import sqrt

class Circle():
    def __init__(self, center_x, center_y, radius):
        self.center_x  = center_x
        self.center_y  = center_y
        self.radius    = radius

    def is_inside(self, point_x, point_y):
        center_x = self.center_x
        center_y = self.center_y

        if (point_x - center_x)**2 + (point_y - center_y)**2 < self.radius**2:
            return True
        else:
            return False

class TwoCircles:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TwoCircles")
        self.window.resizable(False, False)

        self.CANVAS_WIDTH  = 350 
        self.CANVAS_HEIGHT = 150 
        self.canvas = tk.Canvas (
                self.window, 
                bg     = "white", 
                width  = self.CANVAS_WIDTH, 
                height = self.CANVAS_HEIGHT
            )
        self.canvas.pack()

        self.CIRCLES_RADIUS = 20
        self.CIRCLE_1_START_X = 20
        self.CIRCLE_1_START_Y = 20
        self.CIRCLE_2_START_X = 120
        self.CIRCLE_2_START_Y = 50
        self.circles = []
        
        self.circle_1 = Circle (
            self.CIRCLE_1_START_X, 
            self.CIRCLE_1_START_Y, 
            self.CIRCLES_RADIUS
        )

        self.circle_2 = Circle (
            self.CIRCLE_2_START_X, 
            self.CIRCLE_2_START_Y, 
            self.CIRCLES_RADIUS
            )

        self.circles.append(self.circle_1)
        self.circles.append(self.circle_2)
        
        for circle in self.circles:
           create_circle(self.canvas, circle)

        self.create_line_between_circles()

        self.canvas.bind("<B1-Motion>", self.mouse_moved)

        self.window.mainloop()
    
    def mouse_moved(self, event):

        if self.circle_1.is_inside(event.x, event.y):
             self.set_circles_position(
                event.x, event.y,
                self.circle_2.center_x, self.circle_2.center_y
            )
                
        if self.circle_2.is_inside(event.x, event.y):
             self.set_circles_position(
                self.circle_1.center_x, self.circle_1.center_y,
                event.x, event.y
            )

        circles_distance = self.circles_distance(self.circle_1, self.circle_2)

        #Forrige figurer skal slettes og nye tegnes opp dersom
        #avstanden mellom sirklene blir for kort
        if circles_distance < 70:
            self.set_circles_position(
                self.CIRCLE_1_START_X, self.CIRCLE_1_START_Y,
                self.CIRCLE_2_START_X, self.CIRCLE_2_START_Y
            )
        
        self.create_line_between_circles()

    def create_line_between_circles(self):
            self.canvas.create_line (
                self.circle_1.center_x, 
                self.circle_1.center_y,
                self.circle_2.center_x,
                self.circle_2.center_y
        )
            self.canvas.create_text(
                175,
                75,
                text=str(
                     round(
                        self.circles_distance(self.circle_1, self.circle_2), 
                        2 ) 
                     )
        )

    def set_circles_position(
            self, 
            circle_1_x, circle_1_y, 
            circle_2_x, circle_2_y
        ):
        self.canvas.delete("all")
        
        self.circle_1 = Circle (
            circle_1_x, 
            circle_1_y, 
            self.CIRCLES_RADIUS
        )
    
        self.circle_2 = Circle (
            circle_2_x, 
            circle_2_y, 
            self.CIRCLES_RADIUS
        )

        create_circle(self.canvas, self.circle_1)
        create_circle(self.canvas, self.circle_2)

    def circles_distance(self, circle_1, circle_2):
        circle_distance = sqrt(
            (circle_2.center_x - circle_1.center_x)**2 + 
            (circle_2.center_y - circle_1.center_y)**2
        )
        return circle_distance


def create_circle(canvas, circle):
    canvas.create_oval(
        circle.center_x - circle.radius,
        circle.center_y - circle.radius,
        circle.center_x + circle.radius,
        circle.center_y + circle.radius,
        fill = "red"
    )

TwoCircles()