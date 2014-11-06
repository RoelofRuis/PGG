from projection import Camera
from canvas import Screen
from world import World
from forms import Point, Line, Cube
from program import Program

program = Program()

# Setting up a 3D scene:
# (1) Looking through a Camera
# (2) at a World
# (3) which is filled with Shapes
# (4) and drawing the result to a Screen.

# Setting up the basic objects:
cam = Camera(program.getScreen())
world = World()

# Fill the world with objects:

world.addShapes([
    Cube(Point(0,0,0), 2),
    Cube(Point(0,0,0), 1),
    Cube(Point(0,0,0), 0.5),
    Cube(Point(-4,0,3), 1),
])

cam.lookAt(world)

program.run()
