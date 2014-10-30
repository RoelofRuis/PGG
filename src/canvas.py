from __future__ import division
from Tkinter import *
from calc import Matrix
from forms import Point, Line

def drawLine(canvas, projection, line):
    points = line.getPoints()
    pt1 = projection.multiply(points[0].getCoords())
    pt2 = projection.multiply(points[1].getCoords())
    w.create_line(pt1.getElem(0,0), pt1.getElem(1,0), pt2.getElem(0,0), pt2.getElem(1,0))

lines = [
    Line(Point(100,100,0), Point(200,100,0)),
    Line(Point(100,100,0), Point(100,200,0)),
    Line(Point(200,100,0), Point(200,200,0)),
    Line(Point(100,200,0), Point(200,200,0)),
    Line(Point(100,100,0), Point(100,100,100)),
    Line(Point(200,100,0), Point(200,100,100)),
    Line(Point(200,200,0), Point(200,200,100)),
    Line(Point(100,200,0), Point(100,200,100)),
    Line(Point(100,100,100), Point(100,200,100)),
    Line(Point(100,100,100), Point(200,100,100)),
    Line(Point(200,100,100), Point(200,200,100)),
    Line(Point(100,200,100), Point(200,200,100)),
]


# Drawing and all
p = Matrix(2,3).setTo([[1,0,0.5],[0,1,-0.2]])
master = Tk()
w = Canvas(master, width=400, height=400)
w.pack()

# Drawing the lines
for l in lines:
    drawLine(w, p, l)

mainloop()
