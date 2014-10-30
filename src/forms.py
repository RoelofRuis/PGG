import math

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
    

# The Polygon object represents a polygon
class Polygon():
    def __init__(self, point_a, point_b, point_c):
        self.pt_a = point_a
        self.pt_b = point_b
        self.pt_c = point_c
        
    def __str__(self):
        return 'Polygon (%s, %s, %s,)' % (self.pt_a, self.pt_b, self.pt_c)
    
    def getArea(self):
        b = Line(self.pt_a, self.pt_b).getLength()
        return b
