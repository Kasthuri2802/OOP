# Definition of Class:
#     --> Class is a blueprint that defines some properties and behaviors
#     --> Class is a code template for creating objects

# Base class

class animal:
    def eat(self):
        print("I can eat")
    def sleep(self):
        print("I can sleep")
    def make_sound(self):
        print("I can make sound")

# derived class

class dog(animal):
    def make_sound(self):
        print("I can make wow wow sound")

class cat(animal):
    def make_sound(self):
        print("I can make meow meow sound")

