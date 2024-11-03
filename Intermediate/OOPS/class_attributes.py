# Import required modules

# Class attributes

class Person:
    # Class attribute
    numberOfPerson = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Person.numberOfPerson += 1
        Person.addPerson()

    def getAge(self):
        return self.age
    
    # Class method
    @classmethod # To denote it is a class method not specific to instance
    def numberOfPeople_(cls):
        return cls.numberOfPerson
    
    @classmethod # To denote it is class method not specific to instance
    def addPerson(cls):
        cls.numberOfPerson += 1


p1 = Person("Jim", 10)
p2 = Person("John", 20)
print(Person.numberOfPeople_())