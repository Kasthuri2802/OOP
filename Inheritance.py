# Definition of Inheritance:
#     --> Inheritance allows us to define a class that inherits all the methods and properties from another class.
#     --> Parent class is the class being inherited from, also called base class.
#     --> Child class is the class that inherits from another class, also called derived class.

# Base Class (Parent Class)

class bird:
    Name = ""
    Age = 0

# Derived Class (Child Class)

class parrot(bird):
    fly_height = 100
    color = "green"

class eagle(bird):
    eyes = "black"

#  Creating object

parrot1 = parrot()
parrot1.Name = "blu"
parrot1.Age = 8

parrot2 = parrot()
parrot2.Name = "red"
parrot2.Age = 10

eagle1 = eagle()
eagle1.Name = "Raja"
eagle1.Age = 20

print(f"{parrot1.Name} is {parrot1.Age} years old and flying height is {parrot1.fly_height}")
print(f"{parrot2.Name} is {parrot2.Age} years old and flying height is {parrot2.fly_height}")
print(f"{eagle1.Name} is {eagle1.Age} years old and color of eyes is {eagle1.eyes}")
