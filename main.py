from Vector2D import Vector2D
from Polar2DAdapter import Polar2DAdapter
from Vector3DInheritance import Vector3DInheritance
from Polar2DInheritance import Polar2DInheritance
from Vector3DDecorator import Vector3DDecorator



def main():
    # Tworzenie przykładowych wektorów
    vector1 = Vector3DInheritance(1, 2, 3)
    vector2 = Vector3DDecorator(2, 2, 0)
    vector3 = Polar2DInheritance(1, 1)

    print("układ karteziański:")

    print("Vector1: ", vector1.getComponents())
    print("Vector2: ", vector2.getComponents())
    print("Vector3: ", vector3.getComponents())

    print("\n")
    print("Układ biegunowy: ")
    print("kąt: ")
    print("Vector3: ", vector3.getAngle())
    print("Długość: ")
    print("Vector3: ", vector3.abs())
    print("\n")

    print("Iloczyn skalarny: ")
    print("Vector2 i Vector3: ", vector2.cdot(vector3))
    print("Vector2 i Vector2: ", vector2.cdot(vector2))
    print("Vector3 i Vector3: ", vector3.cdot(vector3))
    print("\n")
    print("Iloczyn wektorowy: ")
    print("Vector1 i Vector2: ", vector1.cross(vector2).getComponents())



if __name__ == "__main__":
    main()


