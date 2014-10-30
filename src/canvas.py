from Tkinter import *

class Screen():
    def __init__(self):
        self.m = Tk()
        self.canvas = Canvas(self.m, width=400, height=400)
        self.canvas.pack()

    def drawLine(p1, p2):
        self.canvas.create_line(p1.getElem(0,0), p1.getElem(1,0),
                                p2.getElem(0,0), p2.getElem(1,0))

    def show(self):
        mainloop()
