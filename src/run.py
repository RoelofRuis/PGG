from projection import Camera
from canvas import Screen
from world import World
from forms import Point, Line, Cube, Polygon, House, PointyRoof, TriangleRoof, SlopedRoofXpositive, SlopedRoofXnegative
from program import Program



# Setting up a 3D scene:
# (1) Initialize a Program:
#     This is the frame which holds the program
# (2) Setup a camera:
#     This camera references a canvas that is drawn to the screen by the program
# (3) Initialize a world:
#     Setup the world and fill it with shapes which have to be displayable
# (4) Look at the world through the camera.
# (5) Run the program.

program = Program()

cam = Camera(program.getScreen())

world = World()

world.addShapes([
    House(Point(-2, 0, 0), 1, 0.5, TriangleRoof),
    House(Point(-1, 0, 0), 1, 0.5, SlopedRoofXnegative),
    House(Point(0, 0, 0), 1, 0.5, PointyRoof),
    House(Point(1, 0, 0), 1, 0.5, SlopedRoofXpositive)
])

cam.lookAt(world)

program.run()
