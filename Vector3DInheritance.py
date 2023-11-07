from math import sqrt

class Vector3DInheritance:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def abs(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def cdot(self, param):
        if isinstance(param, Vector3DInheritance):
            return self.x * param.getComponents()[0] + self.y * param.getComponents()[1] + self.z * param.getComponents()[2]
        else:
            raise ValueError("Parameter must be an instance of IVector")

    def getComponents(self):
        return [self.x, self.y, self.z]

    def cross(self, param):
        x1, y1, z1 = self.getComponents()
        x2, y2, z2 = param.getComponents()

        # Obliczanie iloczynu wektorowego
        result_x = y1 * z2 - y2 * z1
        result_y = z1 * x2 - z2 * x1
        result_z = x1 * y2 - x2 * y1

        return Vector3DInheritance(result_x, result_y, result_z)

    def getSrcV(self):
        return self
