'''
file = open('file.txt', "w")
try:
    file.write("Hello")
finally:
    file.close()


with open("File.txt", "r") as file:
    file.write("JK")
'''

class File:
    def __init__(self, filename, methods):
        self.file = open(filename, methods)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        if type == Exception:
            return True

with File("file.txt", "w") as f:
    print("middle")
    f.write("HelloY")
    raise Exception()