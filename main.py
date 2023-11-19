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

    print("Układ karteziański:")
    print("wektor 3Dinheritance: ", vector1.getComponents())
    print("wektor 3Ddecorator: ", vector2.getComponents())
    print("wektor Polar2Dinheritance: ", vector3.getComponents())


    print("\n")
    print("Układ biegunowy: ")
    print("kąt: ")
    print("Vector Polar2Dinheritance: ", vector3.getAngle())
    print("promień wodzący: ")
    print("Vector Polar2Dinheritance: ", vector3.abs())
    print("\n")

    print("Iloczyn skalarny: ")
    print("Vector 3Ddecorator i Vector Polar2DInheritance: ", vector2.cdot(vector3))
    print("Vector Polar2DInheritance i Vector Polar2DInheritance: ", vector3.cdot(vector3))
    print("Vector 3DInheritance i Vector Polar2DInheritance: ", vector1.cdot(vector3))

    print("\n")
    print("Iloczyn wektorowy: ")
    print("Vector 3DInheritance i Vector 3DDecorator: ", vector1.cross(vector2).getComponents())
    print("Vector 3DInheritance i Vector Polar2DInheritance: ", vector1.cross(vector3).getComponents())



if __name__ == "__main__":
    main()


