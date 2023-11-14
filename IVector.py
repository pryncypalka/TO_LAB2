from abc import ABC, abstractmethod

class IVector(ABC):
    @abstractmethod
    def getComponents(self):
        pass

    @abstractmethod
    def abs(self):
        pass

    @abstractmethod
    def cdot(self):
        pass
