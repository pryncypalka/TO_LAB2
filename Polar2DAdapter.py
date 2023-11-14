from math import atan2
import IVector, IPolar2D
class Polar2DAdapter(IPolar2D, IVector):
    def __init__(self, srcVector):
        self._srcVector = srcVector

    def abs(self):
        return self._srcVector.abs()

    def cdot(self, param):
        return self._srcVector.cdot(param)

    def getComponents(self):
        return self._srcVector.getComponents()

    def getAngle(self):
        x, y = self._srcVector.getComponents()
        return atan2(y, x)  # atan2(y, x) zwraca kąt w radianach