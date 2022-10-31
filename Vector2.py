import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self):
        x2 = (self.x / self.magnitude()) * (self.x / self.magnitude())
        y2 = (self.y / self.magnitude()) * (self.y / self.magnitude())
        unitVec = math.sqrt(x2 + y2)
        return unitVec

    def normalizedCoordinate(self):
        return [(self.x / self.magnitude()), (self.y / self.magnitude())]
