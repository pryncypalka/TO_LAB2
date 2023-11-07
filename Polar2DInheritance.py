from math import atan2
import Vector2D
class Polar2DInheritance(Vector2D):
    def getAngle(self):
        return atan2(self.y, self.x)