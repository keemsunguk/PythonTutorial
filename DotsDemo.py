######################################################
# Struct Example:  dotsDemo
######################################################

import random
from structClass import Struct # defined above (saved in structClass.py)
from tkinter import *

class Dot(Struct): pass

def init(data):
    data.dots = [ ]

def dotContainsPoint(dot, x, y):
    d = ((dot.x - x)**2 + (dot.y - y)**2)**0.5
    return (d <= dot.r)

def mousePressed(event, data):
    for dot in reversed(data.dots):
        if (dotContainsPoint(dot, event.x, event.y)):
            dot.clickCount += 1
            return
    radius = random.randint(20,50)
    color = random.choice(["pink","orange","yellow","green","cyan","purple"])
    data.dots.append(Dot(x=event.x, y=event.y, r=radius,
                         fill=color, clickCount=0))

def redrawAll(canvas, data):
    for dot in data.dots:
        canvas.create_oval(dot.x-dot.r, dot.y-dot.r,
                           dot.x+dot.r, dot.y+dot.r,
                           fill=dot.fill)
        canvas.create_text(dot.x, dot.y, text=str(dot.clickCount))

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)