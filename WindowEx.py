from tkinter import *
import math
import time

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawClock(canvas, x0, y0, x1, y1, hour, minute):

    # find relevant values for positioning clock
    width = (x1 - x0)
    height = (y1 - y0)
    r = min(width, height)/2
    cx = (x0 + x1)/2
    cy = (y0 + y1)/2

    # draw the clock face
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="black", 
                        width=2, fill="yellow")
    r *= 0.85 # make smaller so time labels lie inside clock face
    for hr in range(12):
        hourAngle = math.pi/2 - (2*math.pi)*(hr/12)
        hourX = cx + r * math.cos(hourAngle)
        hourY = cy - r * math.sin(hourAngle)
        label = str(hr if (hr > 0) else 12)
        canvas.create_text(hourX, hourY, text=label, font="Arial 16 bold")
        
    # adjust the hour to take the minutes into account
    hour += minute/60.0

    # find the hourAngle and draw the hour hand
    # but we must adjust because 0 is vertical and
    # it proceeds clockwise, not counter-clockwise!
    hourAngle = math.pi/2 - 2*math.pi*hour/12
    hourRadius = r*1/2
    hourX = cx + hourRadius * math.cos(hourAngle)
    hourY = cy - hourRadius * math.sin(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, fill="black", width=1)

    # repeat with the minuteAngle for the minuteHand
    minuteAngle = math.pi/2 - 2*math.pi*minute/60
    minuteRadius = r*9/10
    minuteX = cx + minuteRadius * math.cos(minuteAngle)
    minuteY = cy - minuteRadius * math.sin(minuteAngle) 
    canvas.create_line(cx, cy, minuteX, minuteY, fill="black", width=1)
    
def draw(canvas, width, height):
#    canvas.create_rectangle(1,1,30,30, fill="yellow")
#    (cx, cy) = (width/2, height/2)
#    (rectWidth, rectHeight) = (width/4, height/4)
#    canvas.create_rectangle(cx - rectWidth/2, cy - rectHeight/2,
#                            cx + rectWidth/2, cy + rectHeight/2,
#                            fill=rgbString(23,200,230))
    # draw a clock in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    # with the given time
    # draw an outline rectangle
    (cx, cy, r) = (width/2, height/2, min(width, height)/3)
    x0 = cx - r
    y0 = cy - r
    x1 = cx + r
    y1 = cy + r
    mrg = 5
    canvas.create_rectangle(x0-mrg, y0-mrg, x1+mrg, y1+mrg, outline="black", width=1, fill=rgbString(23,200, 231))

    h = time.localtime().tm_hour
    m = time.localtime().tm_min
    drawClock(canvas, x0, y0, x1, y1, h, m)
    
def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    
    root.mainloop()
    print("bye!")

runDrawing(400, 200)