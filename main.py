

from Vector2D import Vector2D
from Vector3DInheritance import Vector3DInheritance
from Polar2DAdapter import Polar2DAdapter
from Polar2DInheritance import Polar2DInheritance




def main(self):
    # Tworzenie przykładowych wektorów
    vector1 = Vector3DInheritance(1, 2, 3)
    vector2 = Vector3DInheritance(10, 2, 0)
    vector3 = Vector3DInheritance(1, 5, 3)

    # Wyświetlenie współrzędnych wektorów w układach kartezjańskim i biegunowych
    print("Współrzędne wektora 1:")
    print("Kartezjański:", vector1.get_cartesian())
    print("Biegunowy:", vector1.get_polar())

    print("\nWspółrzędne wektora 2:")
    print("Kartezjański:", vector2.get_cartesian())
    print("Biegunowy:", vector2.get_polar())

    print("\nWspółrzędne wektora 3:")
    print("Kartezjański:", vector3.get_cartesian())

    # Wyświetlenie wyników iloczynu skalarnego i wektorowego
    # (w formie współrzędnych kartezjańskich) dla wszystkich możliwych kombinacji
    print("\nIloczyn skalarny i wektorowy:")
    print("Iloczyn skalarny wektor 1 i wektor 2:", vector1.dot(vector2))
    print("Iloczyn wektorowy wektor 1 i wektor 2:", vector1.cross(vector2).get_cartesian())

    print("Iloczyn skalarny wektor 1 i wektor 3:", vector1.dot(vector3))
    print("Iloczyn wektorowy wektor 1 i wektor 3:", vector1.cross(vector3).get_cartesian())

    print("Iloczyn skalarny wektor 2 i wektor 3:", vector2.dot(vector3))
    print("Iloczyn wektorowy wektor 2 i wektor 3:", vector2.cross(vector3).get_cartesian())

if __name__ == "__main__":
    main()


