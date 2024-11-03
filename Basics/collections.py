# unordered or ordered group of elements

# lists
x = [4, 'Group', 'you', 0]

# store different elements - ordered collection - order is maintained.
# mutable ones are lists . It stores ref to obj. Original stored somewhere

print(len(x))

x.append('Love')

print(x)

print(len(x))

x.extend([90, 45, 34])

print(x)

print(x.pop())

print(x)

print(x.pop(len(x) - 1))

print(x)

y = x # Stores ref
z = x[:] # stores copy
x[0] = 89

print(x[1])
print(x)
print(y)
print(z)


# tuples - immutable

print("----------")
print("tuples")
print("----------")

x = (0,0,4,5, 5)

print(x)

print(x[2])

print(x.index(5))
print(x.count(5))

po = [1,4,2,67,34]

for i, val in enumerate(po):
    # print(f'{i}, {val}')
    print(i, val)