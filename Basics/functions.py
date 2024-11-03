def func1(x, y, z=None):
    print("z", z)
    return (x+y), (x*y)

print(func1(3,4,7)) 

print(func1(3,4)[0])
print(func1(3,4)[1])

r1, r2 = func1(3,4)
print(r1, r2)

print("---------Advanced Func------")
def foo(x):
    def bar():
        print(x)
    return bar

# print(foo(3)())

v = foo(3)
v()

# args, kwargs
print("---------------args/kwargs--------------")
def loom(*args, **kwargs):
    pass

print("----------Unpack operator---------------")
co = [1,3,4,5,6,7]
print(*co)


print("---------ex 2----------------")
def unpack_pair(x, y):
    print(x, y)

pairs = [(1,2), (3,4)]

for pair in pairs:
    unpack_pair(*pair)

unpack_pair(**{'x': 2, 'y': 5})
unpack_pair(**{'y': 5, 'x': 2})


def koo(*args, **kwargs):
    print(*args)
    print(**kwargs)


koo(45,6,[1,2,3,4,5])