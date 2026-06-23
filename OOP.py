from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"
print(Dog("Fido").make_sound())
print(Cat("Luna").make_sound())
print(Cow("Spot").make_sound())

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

def get_animal_sounds(animals):
    return [animal.make_sound() for animal in animals]

print(get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

def get_animal_sounds(animals):
    return [animal.make_sound() for animal in animals]

def create_and_get_sounds():
    animals = [
        Dog("Fido"),
        Cat("Luna"),
        Cow("Spot")
    ]
    return [a.make_sound() for a in animals]

print(create_and_get_sounds())
print(get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))
print(create_and_get_sounds() == get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))
print(create_and_get_sounds() == create_and_get_sounds())
print(create_and_get_sounds() is create_and_get_sounds())
print(get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]) == get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))
