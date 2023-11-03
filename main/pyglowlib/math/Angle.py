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

    def getDegrees(self):
        return self.angleRadians * 180 / math.pi

    def getRadians(self):
        return self.angleRadians

    def getUnitVector(self):
        return Vector(math.cos(self.getRadians()), math.sin(self.getRadians()))
