from math import sqrt
from Vector2D import Vector2D


class Vector3DInheritance(Vector2D):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self._z = z

    def abs(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def cdot(self, param):
        if isinstance(param, Vector3DInheritance):
            p_x, p_y, p_z = param.getComponents()
            return self._x * p_x + self._y * p_y + self._z * p_z
        else:
            raise ValueError("Parameter must be an instance of IVector")

    def getComponents(self):
        return [self._x, self._y, self._z]

    def cross(self, param):
        x1, y1, z1 = self._x, self._y, self._z
        x2, y2, z2 = param.getComponents()

        # Obliczanie iloczynu wektorowego
        result_x = y1 * z2 - y2 * z1
        result_y = z1 * x2 - z2 * x1
        result_z = x1 * y2 - x2 * y1

        return Vector3DInheritance(result_x, result_y, result_z)

    def getSrcV(self):
        return self

