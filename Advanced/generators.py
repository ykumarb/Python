# problem

'''
x = [i ** 2 for i in range(10000000000000)]

for el in x:
    print(el)
'''

'''
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()
    
    def next(self):
        if self.last > self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv
    
g = Gen(10000)

while True:
    try:
        print(next(g))
    except StopIteration:
        break 

'''

import sys
def gen(n):
    for i in range(n):
        yield i ** 2

g = gen(1000)
x = [i ** 2 for i in range(1000)]

print(sys.getsizeof(g))
print(sys.getsizeof(x))

# for i in g: 
#     print(i)