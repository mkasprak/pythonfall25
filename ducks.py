"""
    Demonstrate creating and implementing the duck class

"""


class ToyDuck:
    """
        Document with docstrings every class. This class represents
        a toy duck.
    """

    def __init__(self, color: str, material: str, size: str, name:str):
        """ 
            Initialize all the basic attributes of our toy duck
        """
        self.__color = color # enables "data mangling" makes hidden from other programs
        self.__material = material
        self.__size = size
        self.__name = name
    
    def describe(self):
        print(f"My Duck, {self.__name}, is {self.__material}, {self.__color}, {self.__size}, and is my favorite")


    # Setters
    def set_color(self, color):
        self.__color = color

    def set_material(self, material):
        self.__material = material
    
    def set_size(self, size):
        self.__size = size

    def set_name(self, name):
        self.__name = name

    # Getters

    def get_name(self):
        return self.__name

    def get_material(self):
        return self.__material
    
    def get_size(self):
        return self.__size
    
    def get_name(self):
        return self.__name


def main():
    fluffy = ToyDuck("brown", "fabric", "large", "Wolf")
    squeak = ToyDuck("Yellow", "rubber", "small", "Squeak")
    print("\n\n\n")
    fluffy.describe()
    squeak.describe()

    fluffy.set_color("tan")
    squeak.set_name("Splash")

    fluffy.describe()
    squeak.describe()

    print(f"I like both of my ducks, but {fluffy.get_name()} stays in my bed \n and {squeak.get_name()} prefers the tub.")
main()