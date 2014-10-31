from forms import Projectable

class World():
    def __init__(self):
        self.shapes = list()

    def addShapes(self, shapes):
        for shape in shapes:
            self.addShape(shape)

    def addShape(self, shape):
        if shape.__class__.__bases__[0] == Projectable:
            self.shapes.append(shape)

    def getShapes(self):
        return self.shapes
