import math


class Vector:

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def add(self, vector: 'Vector') -> 'Vector':
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self

    def subtract(self, vector: 'Vector') -> 'Vector':
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z
        return self

    def scale(self, vector: 'Vector'):
        self.x *= vector.x
        self.y *= vector.y
        self.z *= vector.z
        return self

    def multipy(self, mul: float) -> 'Vector':
        self.x *= mul
        self.y *= mul
        self.z *= mul
        return self

    def cross(self, vector: 'Vector') -> 'Vector':
        self.x = self.y * vector.z - self.z * vector.y
        self.y = -1 * self.x * vector.z + self.z * vector.x
        self.z = self.x * vector.y - self.z * vector.x
        return self

    def getAdded(self, vector: 'Vector') -> 'Vector':
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def getSubtracted(self, vector: 'Vector') -> 'Vector':
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def getScaled(self, vector: 'Vector') -> 'Vector':
        return Vector(self.x * vector.x, self.y * vector.y, self.z * vector.z)

    def getMultiplied(self, val: float) -> 'Vector':
        return Vector(self.x * val, self.y * val, self.z * val)

    def getCross(self, vector: 'Vector') -> 'Vector':
        return Vector(
            self.y * vector.z - self.z * vector.y,
            -self.x * vector.z + self.z * vector.x,
            self.x * vector.y - self.z * vector.x)

    def getDot(self, vector: 'Vector') -> float:
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def getMagnitude(self) -> float:
        return math.sqrt(pow(self.x, 2) + math.pow(self.y, 2) + pow(self.z, 2))

    def getUnitVector(self) -> 'Vector':
        return self.getMultiplied(1 / self.getMagnitude())

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}, {self.z}>"

    def __eq__(self, vector: 'Vector') -> bool:
        return self.x == vector.x and self.y == vector.y and self.z == vector.z


class Angle:

    def __init__(self, angleRadians: float, isDegrees: bool = False):
        self.angleRadians: float = angleRadians
        self.isDegrees: bool = isDegrees

    def set(self, angle: float, isDegrees: bool = False):
        if not isDegrees:
            self.angleRadians = angle
        else:
            self.angleRadians = angle * 180 / math.pi

    def add(self, angle: 'Angle') -> 'Angle':
        self.angleRadians += angle.getRadians()
        return self

    def subtract(self, angle: 'Angle') -> 'Angle':
        self.angleRadians -= angle.getRadians()
        return self

    def multiply(self, val: float) -> 'Angle':
        self.angleRadians *= val
        return self

    def getAdded(self, angle: 'Angle') -> 'Angle':
        return Angle(self.getRadians() + angle.getRadians())

    def getSubtracted(self, angle: 'Angle') -> 'Angle':
        return Angle(self.getRadians() - angle.getRadians())

    def getMultiplied(self, val: float) -> 'Angle':
        return Angle(self.getRadians() * val)

    def getDegrees(self) -> float:
        return self.angleRadians * 180 / math.pi

    def getRadians(self) -> float:
        return self.angleRadians

    def getUnitVector(self) -> Vector:
        return Vector(math.cos(self.getRadians()), math.sin(self.getRadians()))

    def __eq__(self, other: 'Angle') -> bool:
        return other.angleRadians == self.angleRadians

    def __str__(self) -> str:
        return f"[Angle: {self.getRadians()}]"