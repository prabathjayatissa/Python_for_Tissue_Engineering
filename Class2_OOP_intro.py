# Object-Oriented Programming 
# With simple theory inside the script

print("Welcome to Object-Oriented Programming!")
print("We will use toys and animals to understand OOP.\n")


# ============================================================
# THEORY 1: What is OOP?
# ============================================================
# OOP means Object-Oriented Programming.
#
# It is a way to write programs by thinking about things.
#
# For example, a real world can have:
# - a car
# - a ball
# - a cat
# - a dog
#
# In Python, we can make these things into OBJECTS.
#
# An object can have:
# 1. Information about itself.
# 2. Actions that it can do.
#
# Example:
# A toy car has information:
# - name: car
# - color: red
#
# A toy car can do actions:
# - say hello
# - play


# ============================================================
# THEORY 2: What is a class?
# ============================================================
# A CLASS is like a plan, recipe, or drawing for making objects.
#
# Imagine that a toy maker has a plan for making cars.
# The plan says:
# - every car has a name
# - every car has a color
# - every car can say hello
# - every car can play
#
# The plan is not one real car.
# It only explains how to make a car.


class Toy:
    # ========================================================
    # THEORY 3: What is __init__?
    # ========================================================
    # __init__ is a special function.
    # It runs automatically when we make a new object.
    #
    # It gives the new toy its first information.
    #
    # The word "self" means:
    # "this particular toy".
    #
    # For example, self.name means:
    # "the name of this toy".
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # ========================================================
    # THEORY 4: What is a method?
    # ========================================================
    # A METHOD is an action that an object can perform.
    #
    # This method allows a toy to say hello.
    # A method is a function written inside a class.

    def say_hello(self):
        print("Hello! I am a", self.color, self.name + ".")

    def play(self):
        print("Let's play with the", self.color, self.name + "!")


# ============================================================
# THEORY 5: What is an object?
# ============================================================
# An OBJECT is a real thing made from a class plan.
#
# Toy is the plan.
# red_car and blue_ball are real objects made from that plan.
#
# We can make many objects from one class.

red_car = Toy("car", "red")
blue_ball = Toy("ball", "blue")

# Each object has its own information and can use its methods.
red_car.say_hello()
red_car.play()

blue_ball.say_hello()
blue_ball.play()


# ============================================================
# THEORY 6: What is an attribute?
# ============================================================
# An ATTRIBUTE is information stored inside an object.
#
# The red car has:
# - name = car
# - color = red
#
# The blue ball has:
# - name = ball
# - color = blue
#
# The objects use the same class plan,
# but they can have different information.

print("The first toy is a", red_car.color, red_car.name + ".")
print("The second toy is a", blue_ball.color, blue_ball.name + ".")


# ============================================================
# THEORY 7: A class can describe many similar things.
# ============================================================
# We can use one Animal class for many animals.
# Each animal has:
# - a name
# - a sound
#
# Each animal can also speak.


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


# ============================================================
# THEORY 8: Objects can change.
# ============================================================
# An object can have information that changes.
#
# A puppy can be:
# - not happy at first
# - happy after playing
#
# The attribute happy stores the puppy's feeling.


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


# ============================================================
# THEORY 9: The four important OOP ideas
# ============================================================
# 1. Class
#    A plan for making objects.
#    Example: Toy is a plan for making toys.
#
# 2. Object
#    One real thing made from a class.
#    Example: red_car is one Toy object.
#
# 3. Attribute
#    Information about an object.
#    Example: red_car.color is "red".
#
# 4. Method
#    An action that an object can do.
#    Example: red_car.play() makes the car play.


# ============================================================
# THEORY 10: Why is OOP useful?
# ============================================================
# OOP helps us organize big programs.
#
# Instead of putting everything in one large list,
# we group related information and actions together.
#
# For example, a Dog object can keep together:
# - its name
# - its color
# - its sound
# - its actions
#
# This makes programs easier to understand and reuse.


print("\nOOP is like making friendly things from simple plans!")
print("A class is a plan.")
print("An object is a thing made from the plan.")
print("An attribute is information about the thing.")
print("A method is an action the thing can do.")
