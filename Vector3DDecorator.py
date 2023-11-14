from Vector2D import Vector2D


class Vector3DDecorator(Vector2D):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self._srcVector = Vector2D(x, y)
        self._z = z

    def abs(self):
        return (self._srcVector.abs() ** 2 + self._z ** 2) ** 0.5

    def cdot(self, param):
        return self._srcVector.cdot(param)

    def getComponents(self):
        return self._srcVector.getComponents() + [self._z]

    def cross(self, param):
        x1, y1, z1 = self.getComponents()
        x2, y2, z2 = param.getComponents()

        # Obliczanie iloczynu wektorowego
        result_x = y1 * z2 - y2 * z1
        result_y = z1 * x2 - z2 * x1
        result_z = x1 * y2 - x2 * y1

        return Vector3DDecorator(Vector2D(result_x, result_y), result_z)



