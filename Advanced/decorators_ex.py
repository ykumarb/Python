# Example code to know how decorators work
import time
def timer(test):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = test()
        end = time.time() - start
        print("Time: ",end)
        return rv
    return wrapper

@timer
def test():
    for _ in range(100000000):
        pass
@timer
def test2():
    time.sleep(2)

test()
test2()