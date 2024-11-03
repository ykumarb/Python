# Decorators
'''
They allow us to modify the behavior of the function
without actually changing any of its code
'''

# Non-decorator code 

def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv
    return wrapper

@func
def func2(x,y):
    print("I'm func2")
    print(x)
    return y

@func
def func3(c,v):
    print("I'm func3")
    return v

x = func3(3,4)
print(x)
y = func2(3,4)
print(y)
# x = func(func3)
# y = func(func2)
# x()
# y()


# Replace 
# func2 = func(func2)
# func2()

# func3 = func(func3)
# func3()