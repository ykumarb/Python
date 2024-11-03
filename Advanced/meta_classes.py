class Foo:
    def show(self):
        print("hi")

def add(self, y=None):
    self.z = y

Test = type('Test', (Foo,), {"x":5, "add": add})
t1 = Test()
t1.wy = "Hello"
print(type(Test))
print(type(t1))
print(t1.wy)
print(t1.x)
t1.show()
t1.add()
print(t1.z)


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}

        for k, v in attrs.items():
            if k.startswith("__"):
                a[k] = v
            else:
                a[k.upper()] = v
        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 6

    def func(self, name):
        self.name = name

d = Dog()
d.FUNC("name")