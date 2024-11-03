# Class working in Python

class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    
    def numberOfChild(self):
        if self.name == "Jack":
            return 2
        else:
            return 3
    def stare(self):
        print("I stare coz I'm a dog!!!")
    def bark(self):
        print("I bark coz I'm a dog!!!")


# Instantiate class Dog
d = Dog("Jack", 23)

# Print the name of the dog
print(d.getName())

# print the age of the dog
print(d.getAge())

# Set the age of the dog
d.setAge(24)

# print the age of the dog
print(d.getAge())

# Access method of Dog class
d.bark()

# Access the stare method of Dog class
d.stare()

# Get the number of children the Dog has
n_child = d.numberOfChild()

# Print the n_child
print(f'{d.name} - {n_child}')

# Print the type of dog object
print(type(d))



# Instantiate class Dog
d2 = Dog("Jim", 43)

# print the name of the dog
print(d2.getName())

# Print the age of the dog
print(d2.getAge())

# Set the age of the dog
d2.setAge(44)

# print the age of the dog
print(d2.getAge())

# Access method of Dog class
d2.bark()

# Access the stare method of Dog class
d2.stare()

# Get the number of children the Dog has
n_child = d2.numberOfChild()

# Print the n_child
print(f'{d2.name} - {n_child}')

# Print the type of dog object
print(type(d2))