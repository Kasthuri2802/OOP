# Definition of Polymorphism:
#     Poly - Many ; Morph - Form ==> Polymorphism - Many forms
# --> In Python, Polymorphism lets us define methods in the child class 
#        that have the same name as the methods in the parent class.

# Base class

class animal:
    def eat(self):
        print("I can eat")
    def sleep(Self):
        print("I can sleep")
    def make_sounds(self):
        print("I can make sounds")

# Derived class

class dog(animal):
    def make_sounds(self):
        print("I can make wow wow sounds")
class cat(animal):
    def make_sounds(self):
        print("I can make meow meow sounds")

# Creating Object

dog1 = dog()
dog1.eat()
dog1.sleep()
dog1.make_sounds()

cat1 = cat()
cat1.eat()
cat1.sleep()
cat1.make_sounds()

rabbit1 = animal()
rabbit1.eat()
rabbit1.sleep()
rabbit1.make_sounds()
