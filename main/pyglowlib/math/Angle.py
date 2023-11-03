import math

from pyglowlib.math.Vector import Vector


class Angle:
    angleRadians: float
    isDegrees: bool

    def __init__(self, angleRadians: float, isDegrees: bool = False):
        self.angleRadians = angleRadians
        self.isDegrees = isDegrees

    def set(self, angle: float, isDegrees: bool = False):
        if not isDegrees:
            self.angleRadians = angle
        else:
            self.angleRadians = angle * 180 / math.pi

    def getDegrees(self) -> float:
        return self.angleRadians * 180 / math.pi

    def getRadians(self) -> float:
        return self.angleRadians

    def getUnitVector(self) -> Vector:
        return Vector(math.cos(self.getRadians()), math.sin(self.getRadians()))

    def __eq__(self, other: 'Angle') -> bool:
        return other.angleRadians == self.angleRadians

    def __str__(self):
        pass