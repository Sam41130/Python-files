# 1. Base class
class Animal:
    def fur(self):
        print("I have fur all over my body")

# 2. Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("woof!woof!")

# 3. Grandchild class inheriting from Dog
class Puppy(Dog):
    def play(self):
        print("I play all the time")

# 4. Create instance and call methods
bosco = Puppy()

# Call all available methods (demonstrating inheritance)
bosco.play()
bosco.bark()
bosco.fur()
