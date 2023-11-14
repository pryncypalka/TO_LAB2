from math import atan2
import Vector2D
class Polar2DInheritance(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)

    def getAngle(self):
        return atan2(self._y, self._x)
