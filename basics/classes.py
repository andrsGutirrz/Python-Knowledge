# PascalCase
class Person:

    def __init__(self, name, age):
        # This == self in Java
        self.name = name
        self.age = age
        self.__weight = 0 # Simulates private

    def __repr__(self): # toString
        return f"Name: {self.name}"

    def get_weight(self):
        self.my_new_prop = 1
        return self.__weight

class SquareBox:
    pass


if __name__ == '__main__':
    andres = Person("Andres", 25)
    andres.get_weight()
    print(andres.my_new_prop)