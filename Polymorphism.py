print("Coding on Polymorphism Concepts ")

class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Bark"
class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Function that demonstrates polymorphism
def animal_sound(animal:Animal):
    print(animal.make_sound())

# Creating instances
dog = Dog()
cat = Cat()

# Demonstrating polymorphism
animal_sound(dog)
animal_sound(cat)