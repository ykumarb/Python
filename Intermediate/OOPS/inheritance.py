# Inheritance example

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print("I don't what to say!")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # Inits the parent class attributes
        self.color = color
    def speak(self):
        print("Meow")

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color} color')

p1 = Pet('Jimmy', 12)
p1.show()

c1 = Cat('Meowwww', 19, 'Brown')
c1.show()
c1.speak()

d1 = Dog('Honey', 20)
d1.show()
d1.speak()