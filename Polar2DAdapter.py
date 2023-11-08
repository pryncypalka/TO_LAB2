from math import atan2

class Polar2DAdapter:
    def __init__(self, srcVector):
        self._srcVector = srcVector

    def abs(self):
        return self._srcVector.abs()

    def cdot(self, param):
        return self._srcVector.cdot(param)

    def getComponents(self):
        return self._srcVector.getComponents()

    def getAngle(self):
        comp = self._srcVector.getComponents()
        x = comp[0]
        y = comp[1]
        return atan2(y, x)  # atan2(y, x) zwraca kąt w radianach