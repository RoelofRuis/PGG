from __future__ import division
from calc import Matrix

class Camera():
    def __init__(self):
        self.internal = Matrix(3,3).setTo([
            [1,0,0],
            [0,1,0],
            [0,0,1]])
        self.external = Matrix(3,4).setTo([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0]])

    def __str__(self):
        return ('Camera (\n M_int %s\n M_ext %s\n)' % (self.internal, self.external))

    def projectPoint(self, point):
        proj = self.external.multiply(point.getHomCoords())
        proj = self.internal.multiply(proj)
        print(proj)
        return Matrix(2,1).setTo([[proj.getElem(0,0)/proj.getElem(2,0)],
                                 [proj.getElem(1,0)/proj.getElem(2,0)]])
        
