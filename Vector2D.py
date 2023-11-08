class Vector2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getComponents(self):
        return [self._x, self._y]

    def abs(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def cdot(self, param):
        if isinstance(param, Vector2D):
            param_comp = param.getComponents()
            return self._x * param_comp[0] + self._y * param_comp[1]
        else:
            raise ValueError("Parameter must be an instance of Vector2D")
