# OOP means Object-Oriented Programming.
# It is a way to describe things using simple objects.

# 1. A class is like a toy-making plan.
class Toy:
    # This function makes a new toy.
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # This is an action the toy can do.
    def say_hello(self):
        print("Hello! I am a", self.color, self.name + ".")

    def play(self):
        print("Let's play with me!")


# 2. Objects are toys made from the plan.
red_car = Toy("car", "red")
blue_ball = Toy("ball", "blue")

# 3. Each object can do its actions.
red_car.say_hello()
red_car.play()

blue_ball.say_hello()
blue_ball.play()


# 4. Objects can have different information.
print("The first toy is a", red_car.color, red_car.name + ".")
print("The second toy is a", blue_ball.color, blue_ball.name + ".")


# 5. Another simple class: Animal.
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(self.name, "says", self.sound + "!")


cat = Animal("Cat", "meow")
dog = Animal("Dog", "woof")

cat.speak()
dog.speak()


# 6. A class can have a changing value.
class Puppy:
    def __init__(self, name):
        self.name = name
        self.happy = False

    def wag_tail(self):
        self.happy = True
        print(self.name, "is wagging its tail!")

    def show_feeling(self):
        if self.happy:
            print(self.name, "is happy!")
        else:
            print(self.name, "is waiting to play.")


puppy = Puppy("Buddy")
puppy.show_feeling()
puppy.wag_tail()
puppy.show_feeling()


# 7. Easy OOP words:
# Class  = a plan, like a recipe for making a toy.
# Object = one real thing made from the plan.
# Attribute = information about the thing, like colour or name.
# Method  = an action the thing can do, like play or speak.

print("\nOOP is like making friendly toys and animals with plans!")

# Hands-on Exercise

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
