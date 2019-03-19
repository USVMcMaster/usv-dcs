
class Node():

    def __init__(self, x, y, s=None, e=None, g=None, h=None, f=None, parent=None):
        x = self.x
        y = self.y
        
        s = self.s
        e = self.e

        f = self.f
        g = self.g
        h = self.f
        parent = self.parent

    def node(self, x, y):
        self.x = x
        self.y = y

    # get returns positional data
    def getXY(self):
        return self.x, self.y   

    def getG(self):
        return self.g

    def getH(self):
        return self.h

    def getF(self):
        return self.f

    # set sets the positional data
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def setG(self, g):
        self.g = g

    def setH(self, h):
        self.h = h

    def setF(self, f):
        self.f = f

    def isEqual(self, s, e):
        if s.getXY() is e.getXY():
            return True
        else:
            return False