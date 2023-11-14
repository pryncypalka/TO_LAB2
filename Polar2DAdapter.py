from math import atan2
from IVector import IVector
from IPolar2D import IPolar2D
from Vector2D import Vector2D

class Polar2DAdapter(IPolar2D, IVector):
    def __init__(self, Vector2D):
        self._srcVector = Vector2D

    def abs(self):
        return self._srcVector.abs()

    def cdot(self, param):
        if isinstance(param, Vector2D):
            return self._srcVector.cdot(param)
        else:
            raise ValueError("Parameter must be an instance of IVector")

    def getComponents(self):
        return self._srcVector.getComponents()

    def getAngle(self):
        x, y = self._srcVector.getComponents()
        return atan2(y, x)  # atan2(y, x) zwraca kąt w radianach