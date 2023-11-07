class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getComponents(self):
        return [self.x, self.y]

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def cdot(self, param):
        if isinstance(param, Vector2D):
            return self.x * param.x + self.y * param.y
        else:
            raise ValueError("Parameter must be an instance of Vector2D")
