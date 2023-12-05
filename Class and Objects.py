# Definition of Class:
#     --> Class is a blueprint that defines some properties and behaviors
#     --> Class is a code template for creating objects
#     --> A class is not allocated memory when it is defined
#     --> Class is a logical entity

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

# Definition of object: 
#     --> Object is an instance of a class that has those properties and behaviours attached
#     --> An object is allocated memory when it is created
#     --> Objects are physical entities

# Creating Object

dog1 = dog()
dog1.eat()
dog1.sleep()
dog1.make_sound()

cat1 = cat()
cat1.eat()
cat1.sleep()
cat1.make_sound()

rabbit1 = animal()
rabbit1.eat()
rabbit1.sleep()
rabbit1.make_sound()

