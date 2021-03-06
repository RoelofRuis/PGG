from __future__ import division
from calc import Matrix
from canvas import Screen

# The camera object represents a camera looking at the world
# The way it works is by transforming all points in the world with a
# projective transformation so they are displayed at the screen at the
# correct position.
class Camera():
    def __init__(self, screen):
        self.internal = Matrix(3,3).setTo([
            [100,0,400],
            [0,100,400],
            [0,0,1]])
        self.external = Matrix(3,4).setTo([
            [1,0,0,0.5],
            [0,1,0,0.5],
            [0,0,0.5,1]])
        self.screen = screen

    def __str__(self):
        return ('Camera (\n M_int %s\n M_ext %s\n)' % (self.internal, self.external))

    def getScreen(self):
        return self.screen

    def _transformPoint(self, point):
        proj = self.external.multiply(point.getHomCoords())
        proj = self.internal.multiply(proj)
        w = proj.getElem(2,0)
        if w == 0:
            return Matrix(2,1).setTo([[proj.getElem(0,0)],
                                      [proj.getElem(1,0)]])
        else:
            return Matrix(2,1).setTo([[proj.getElem(0,0)/proj.getElem(2,0)],
                                      [proj.getElem(1,0)/proj.getElem(2,0)]])

    def projectLine(self, line):
        pts = line.getPoints()
        pt1 = self._transformPoint(pts[0])
        pt2 = self._transformPoint(pts[1])
        self.screen.drawLine(pt1, pt2)

    def lookAt(self, world):
        for shape in world.getShapes():
            shape.project(self)
        
