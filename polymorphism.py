class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Horse(Animal):
    def make_sound(self):
        return "Neigh!"

def animal_sound(animal):
    print(animal.make_sound())


dog = Dog()
cat = Cat()
horse = Horse()


animal_sound(dog)    
animal_sound(cat)    
animal_sound(horse)  