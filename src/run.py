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
cam = Camera()
world = World()

# Fill the world with objects:

world.addShapes([
    Line(Point(0,0,0), Point(1,0,0)),
    Line(Point(0,0,0), Point(0,1,0)),
    Line(Point(0,0,0), Point(0,0,1)),
    Line(Point(1,0,0), Point(1,1,0)),
    Line(Point(1,0,0), Point(1,0,1)),
    Line(Point(0,1,0), Point(1,1,0)),
    Line(Point(0,1,0), Point(0,1,1)),
    Line(Point(0,0,1), Point(1,0,1)),
    Line(Point(0,0,1), Point(0,1,1)),
    Line(Point(1,1,0), Point(1,1,1)),
    Line(Point(1,0,1), Point(1,1,1)),
    Line(Point(0,1,1), Point(1,1,1)),
])

cam.lookAt(world)
