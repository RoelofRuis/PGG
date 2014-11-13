from Tkinter import *

# The screen object is a simple wrapper for the Tkinter canvas on which the
# graphics can be drawn.
class Screen():
    def __init__(self, app):
        self.canvas = Canvas(app, width=800, height=800)
        self.canvas.pack()

    def drawLine(self, p1, p2):
        self.canvas.create_line(p1.getElem(0,0), p1.getElem(1,0),
                                p2.getElem(0,0), p2.getElem(1,0))
