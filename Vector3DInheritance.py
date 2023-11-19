from math import sqrt
from Vector2D import Vector2D


class Vector3DInheritance(Vector2D):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self._z = z

    def abs(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def cdot(self, param):
        return super().getComponents()[0] * param.getComponents()[0] + super().getComponents()[1] * param.getComponents()[1] + self._z * 0


    def getComponents(self):
        return [self._x, self._y, self._z]

    def cross(self, param):
        _temp_x = super().getComponents()[1] * 0 - self._z * param.getComponents()[1]
        _temp_y = super().getComponents()[0] * 0 - self._z * param.getComponents()[0]
        _temp_z = super().getComponents()[0] * param.getComponents()[1] - super().getComponents()[1] * \
                  param.getComponents()[0]
        return Vector3DInheritance(_temp_x, _temp_y, _temp_z)

    def getSrcV(self):
        return self

