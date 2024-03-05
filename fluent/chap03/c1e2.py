from math import hypot

class vector:
    '''The Vector class'''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, o):
        x = self.x + o.x
        y = self.y + o.y
        return vector(x, y)

    def __mul__(self, s):
        return vector(self.x * s, self.y *s)

