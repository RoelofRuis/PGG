from projection import Camera
from canvas import Screen
from world import World
from forms import Point, Line

# Setting up a 3D scene:
# (1) Looking through a Camera
# (2) at a World
# (3) which is filled with Shapes
# (4) and drawing the result to a Screen.

# Setting up the basic objects:
s = Screen()
c = Camera(s)
w = World()

# Fill the world with objects:

w.addShapes([
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
])

w.view(c)
