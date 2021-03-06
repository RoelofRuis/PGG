from __future__ import division
import math
import random

from calc import Matrix

# The Projectable object represents any object that is projectable
# These objects should implement the 'project' method
class Projectable():
    def project(self):
        raise NotImplementedError()

		
# The Point object represents a point object in 3 Dimensional space
class Point():
    def __init__(self, my_x, my_y, my_z):
        self.x = my_x
        self.y = my_y
        self.z = my_z

    def __str__(self):
        return 'Point (%s, %s, %s)' % (self.x, self.y, self.z)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def setPosition(self, new_x, new_y, new_z):
        self.x = new_x
        self.y = new_y
        self.z = new_z

    def addPosition(self, new_x, new_y, new_z):
        self.x += new_x
        self.y += new_y
        self.z += new_z

    def copyAddPosition(self, new_x, new_y, new_z):
        return Point(self.x + new_x, self.y + new_y, self.z + new_z)

    def getHomCoords(self):
        return Matrix(4,1).setTo([[self.x], [self.y], [self.z], [1]])
        

# The Line Object represents a line between two points
class Line(Projectable):
    def __init__(self, point_a, point_b):
        self.pt_a = point_a
        self.pt_b = point_b

    def __str__(self):
        return 'Line (%s, %s)' % (self.pt_a, self.pt_b)

    def getLength(self):
        a = abs(self.pt_a.getX() - self.pt_b.getX())
        b = abs(self.pt_a.getY() - self.pt_b.getY())
        c = abs(self.pt_a.getZ() - self.pt_b.getZ())
        return math.sqrt(a**2 + b**2 + c**2)

    def addPosition(self, new_x, new_y, new_z):
        self.pt_a.addPosition(new_x, new_y, new_z)
        self.pt_b.addPosition(new_x, new_y, new_z)

    def getRelativeAngle(self, line):
        pass

    def getPoints(self):
        return [self.pt_a, self.pt_b]

    def project(self, camera):
        camera.projectLine(self)
    
	
# The Cube object represents a cube in 3d space
class Cube(Projectable):
    def __init__(self, point_center, size):
        cx = point_center.getX()
        cy = point_center.getY()
        cz = point_center.getZ()
        self.lines = [
            Line(Point(cx,cy,cz), Point(cx+size,cy,cz)),
            Line(Point(cx,cy,cz), Point(cx,cy+size,cz)),
            Line(Point(cx,cy,cz), Point(cx,cy,cz+size)),
            Line(Point(cx+size,cy,cz), Point(cx+size,cy+size,cz)),
            Line(Point(cx+size,cy,cz), Point(cx+size,cy,cz+size)),
            Line(Point(cx,cy+size,cz), Point(cx+size,cy+size,cz)),
            Line(Point(cx,cy+size,cz), Point(cx,cy+size,cz+size)),
            Line(Point(cx,cy,cz+size), Point(cx+size,cy,cz+size)),
            Line(Point(cx,cy,cz+size), Point(cx,cy+size,cz+size)),
            Line(Point(cx+size,cy+size,cz), Point(cx+size,cy+size,cz+size)),
            Line(Point(cx+size,cy,cz+size), Point(cx+size,cy+size,cz+size)),
            Line(Point(cx,cy+size,cz+size), Point(cx+size,cy+size,cz+size)),
        ]

    def project(self, camera):
        for line in self.lines:
            line.project(camera)


# The Polygon object represents a polygon
class Polygon(Projectable):
    def __init__(self, point_a, point_b, point_c):
        self.pt_a = point_a
        self.pt_b = point_b
        self.pt_c = point_c
        self.lines = [
            Line(self.pt_a, self.pt_b),
            Line(self.pt_b, self.pt_c),
            Line(self.pt_a, self.pt_c),
        ]
        
    def __str__(self):
        return 'Polygon (%s, %s, %s,)' % (self.pt_a, self.pt_b, self.pt_c)
    
    def getArea(self):
        b = Line(self.pt_a, self.pt_b).getLength()
        return b

    def project(self, camera):
        for line in self.lines:
            line.project(camera)

# The house object represents a house

class Roof():
    def fetch_projectables(self):
        raise NotImplementedError()

class House(Projectable):
    def __init__(self, point_origin, size_cube, height_roof, roof_type):
        roof = roof_type(point_origin, size_cube, height_roof)
        roof_elems = roof.fetch_projectables()
        self.house = [
            Cube(point_origin, size_cube
            ), 
        ] + roof_elems
        
    def project(self, camera):
        for obj in self.house:
            obj.project(camera)

class PointyRoof(Roof):
    def __init__(self, point_origin, size_cube, height_roof):
        pt_pl_center = point_origin.copyAddPosition(size_cube/2, -height_roof, size_cube/2)       
        self.roof = [
            Polygon(point_origin,
                    point_origin.copyAddPosition(size_cube, 0, 0),
                    pt_pl_center
            ),
            Polygon(point_origin.copyAddPosition(0, 0, size_cube),
                    point_origin.copyAddPosition(size_cube, 0, size_cube),
                    pt_pl_center
            ), 
        ]

    def fetch_projectables(self):
        return self.roof

class TriangleRoof(Roof):
    def __init__(self, point_origin, size_cube, height_roof):
        pt_pl_front = point_origin.copyAddPosition(size_cube/2, -height_roof, 0) 
        pt_pl_back = point_origin.copyAddPosition(size_cube/2, -height_roof, size_cube)
        self.roof = [
            Polygon(point_origin,
                    point_origin.copyAddPosition(size_cube, 0, 0),
                    pt_pl_front
            ),
            Polygon(point_origin.copyAddPosition(0, 0, size_cube),
                    point_origin.copyAddPosition(size_cube, 0, size_cube),
                    pt_pl_back
            ),
            Line(pt_pl_front, pt_pl_back
            ),  
        ]
        
    def fetch_projectables(self):
        return self.roof

class SlopedRoofXnegative(Roof):
    def __init__(self, point_origin, size_cube, height_roof):
        pt_pl_front = point_origin.copyAddPosition(0, -height_roof, 0) 
        pt_pl_back = point_origin.copyAddPosition(0, -height_roof, size_cube)
        self.roof = [
            Polygon(point_origin,
                    point_origin.copyAddPosition(size_cube, 0, 0),
                    pt_pl_front
            ),
            Polygon(point_origin.copyAddPosition(0, 0, size_cube),
                    point_origin.copyAddPosition(size_cube, 0, size_cube),
                    pt_pl_back
            ),
            Line(pt_pl_front, pt_pl_back
            ),  
        ]
        
    def fetch_projectables(self):
        return self.roof

class SlopedRoofXpositive(Roof):
    def __init__(self, point_origin, size_cube, height_roof):
        pt_pl_front = point_origin.copyAddPosition(size_cube, -height_roof, 0) 
        pt_pl_back = point_origin.copyAddPosition(size_cube, -height_roof, size_cube)
        self.roof = [
            Polygon(point_origin,
                    point_origin.copyAddPosition(size_cube, 0, 0),
                    pt_pl_front
            ),
            Polygon(point_origin.copyAddPosition(0, 0, size_cube),
                    point_origin.copyAddPosition(size_cube, 0, size_cube),
                    pt_pl_back
            ),
            Line(pt_pl_front, pt_pl_back
            ),  
        ]
        
    def fetch_projectables(self):
        return self.roof

class RandomRoof(Roof):
    def __init__(self, point_origin, size_cube, max_height):
        i = random.randint(1, 4)
        height_roof = random.uniform(0, max_height)
        roof_type = {
            1 : PointyRoof,
            2 : TriangleRoof,
            3 : SlopedRoofXnegative,
            4 : SlopedRoofXpositive
        }
        random_roof = roof_type[i](point_origin, size_cube, height_roof)
        self.roof_elems = random_roof.fetch_projectables()
        

    def fetch_projectables(self):
        return self.roof_elems

class Street(Projectable):
    def __init__(self, street_origin, house_size, max_roof_height, house_count):
        self.street = [] 
        for i in range(0, house_count):
            house_origins = street_origin.copyAddPosition(house_size*i, 0, 0)
            self.street += [House(house_origins, house_size, max_roof_height, RandomRoof)]

            
              
    def project(self, camera):
        for house in self.street:
            house.project(camera)
        


        
