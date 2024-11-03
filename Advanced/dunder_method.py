# To showcase what is dunder/magic/double underscore method in python


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"
    
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        
        self.name = self.name * x

p1 = Person("Tim")
p1 * 4  
print(p1)
