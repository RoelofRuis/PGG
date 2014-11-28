from projection import Camera
from canvas import Screen
from world import World
from forms import Point, Line, Cube, Polygon, House, PointyRoof, TriangleRoof, SlopedRoofXpositive, SlopedRoofXnegative, RandomRoof, Street
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
    Street(Point(-4, 0, -10), 1.5, 1, 10)
])

cam.lookAt(world)

program.run()
