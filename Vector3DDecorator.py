from math import sqrt
from Vector2D import Vector2D

class Vector3DDecorator:
    def __init__(self, srcVector, z):
        self.srcVector = srcVector
        self.z = z

    def abs(self):
        return sqrt(self.srcVector.abs() ** 2 + self.z ** 2)

    def cdot(self, param):
        return self.srcVector.cdot(param)

    def getComponents(self):
        return self.srcVector.getComponents() + [self.z]

    def cross(self, param):
        x1, y1, z1 = self.getComponents()
        x2, y2, z2 = param.getComponents()

        # Obliczanie iloczynu wektorowego
        result_x = y1 * z2 - y2 * z1
        result_y = z1 * x2 - z2 * x1
        result_z = x1 * y2 - x2 * y1

        return Vector3DDecorator(Vector2D(result_x, result_y), result_z)



