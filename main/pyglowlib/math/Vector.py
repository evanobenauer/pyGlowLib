import math


class Vector:
    x: float = None
    y: float = None
    z: float = None

    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def add(self, vector: 'Vector'):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def subtract(self, vector: 'Vector'):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z

    def multipy(self, mul: float):
        self.x *= mul
        self.y *= mul
        self.z *= mul

    def cross(self, vector: 'Vector'):
        self.x = self.y * vector.z - self.z * vector.y
        self.y = -1 * self.x * vector.z + self.z * vector.x
        self.z = self.x * vector.y - self.z * vector.x

    def getAdded(self, vector: 'Vector'):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def getSubtracted(self, vector: 'Vector'):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def getMultiplied(self, val: float):
        return Vector(self.x * val, self.y * val, self.z * val)

    def getCross(self, vector: 'Vector'):
        return Vector(
            self.y * vector.z - self.z * vector.y,
            -self.x * vector.z + self.z * vector.x,
            self.x * vector.y - self.z * vector.x)

    def getDot(self, vector: 'Vector'):
        return Vector(self.x * vector.x, self.y * vector.y, self.z * vector.z)

    def getMagnitude(self):
        return math.sqrt(pow(self.x, 2) + math.pow(self.y, 2) + pow(self.z, 2))

    def getUnitVector(self):
        return self.getMultiplied(1 / self.getMagnitude())

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ">"

    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y and self.z == vector.z
