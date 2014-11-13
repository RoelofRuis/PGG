from projection import Camera
from canvas import Screen
from world import World
from forms import Point, Line, Cube, Polygon, House
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
    House(Point(-1, 0, 0), 1, 0.5),
    House(Point(0, 0, 0), 1, 0.5),
    House(Point(1, 0, 0), 1, 0.5),
])

cam.lookAt(world)

program.run()
