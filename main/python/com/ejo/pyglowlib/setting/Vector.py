import math


class Vector3:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getAdded(self, vector):
        return Vector3(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def getSubtracted(self, vector):
        return Vector3(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def getMultiplied(self, val):
        return Vector3(self.x * val, self.y * val, self.z * val)

    def getMagnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def getUnitVector(self):
        return self.getMultiplied(1 / self.getMagnitude())

    def getCross(self, vector):
        return Vector3(
            self.y * vector.getZ() - self.z * vector.getY(),
            -self.x * vector.getZ() + self.z * vector.getX(),
            self.x * vector.getY() - self.z * vector.getX())

    def getDot(self, vector):
        return Vector3(self.x * vector.x, self.y * vector.y, self.z * vector.z)

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ">"


class Vector2(Vector3):
    def __init__(self, x, y):
        Vector3.__init__(self, x, y, 0)
