from contextlib import contextmanager

# From contexlib we have a decorator that allow
# us to decorate a generator that becomes
# a context manager

@contextmanager

def file(filename, method):
    print("enter")
    file = open(filename, method)
    yield file
    file.close()
    print("exit")

with file("file.txt", "w") as f:
    print("middle")
    f.write("Hellou")
