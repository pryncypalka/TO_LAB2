from math import cos, sin, sqrt, atan2

class Polar2DAdapter:
    def __init__(self, srcVector):
        self.srcVector = srcVector

    def abs(self):
        return self.srcVector.abs()

    def cdot(self, param):
        return self.srcVector.cdot(param)

    def getComponents(self):
        return self.srcVector.getComponents()

    def getAngle(self):
        x, y = self.srcVector.getComponents()
        return atan2(y, x)  # Obliczanie kąta między osią OX a wektorem