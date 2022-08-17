from tkinter import * # Import tkinter
from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))
        
# Define a Ball class
class Ball:
    def __init__(self, dx=2, dy=2):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = dx # Move right by default
        self.dy = dy # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

    def move_faster(self):
        self.dx *= 1.1
        self.dy *= 1.1

    def move_slower(self):
        if self.dx > 1 and self.dy > 1: #Begrenser minstehastighet
            self.dx /= 1.1
            self.dy /= 1.1
            

class BounceBalls:
    def __init__(self):
        self.ballList = [] # Create a list for balls
        
        self.window = Tk() # Create a window
        self.window.title("Bouncing Balls") # Set a title
        
        # Handle window closed event
        self.window.protocol("WM_DELETE_WINDOW", self.quit) 
        
        self.width = 350 # Width of the self.canvas
        self.height = 150 # Width of the self.canvas
        self.canvas = Canvas(self.window, bg = "white", 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        frame = Frame(self.window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume",
            command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        btFaster = Button(frame, text = "Faster", command = self.balls_faster)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame, text = "Slower", command = self.balls_slower)
        btSlower.pack(side = LEFT)

        self.sleepTime = 100 # Set a sleep time 
        self.isStopped = False
        self.animate()
        
        self.window.mainloop() # Create an event loop

    def balls_faster(self):
        for ball in self.ballList:
            ball.move_faster()

    def balls_slower(self):
        for ball in self.ballList:
            ball.move_slower()

    def stop(self): # Stop animation
        self.isStopped = True
    
    def resume(self): # Resume animation
        self.isStopped = False   
        self.animate()
    
    def add(self): # Add a new ball
        #dx=2 og #dy=2 dersom første ball
        if len(self.ballList) == 0:
            self.ballList.append(Ball())
        #Ønsker samme fart som de andre ballene på baller som legges til
        else:
            self.ballList.append(
                Ball(self.ballList[0].dx, self.ballList[0].dy)
            )
    
    def remove(self): # Remove the last ball 
        self.ballList.pop()
                                
    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.delete("ball") 
            
            for ball in self.ballList:
                self.redisplayBall(ball)

            self.canvas.after(self.sleepTime) # Sleep 
            self.canvas.update() # Update self.canvas
    
    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
            
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

            
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, 
            ball.y - ball.radius, ball.x + ball.radius, 
            ball.y + ball.radius, fill = ball.color, tags = "ball")
                              
    def quit(self):
        self.stop()
        self.window.destroy()
               
BounceBalls() # Create GUI
