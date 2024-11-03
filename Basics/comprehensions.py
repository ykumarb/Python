# import if necessary 

x = [str(x)+'3' for x in range(10)]
print(x)

y = [[0 for x in range(100)] for x in range(5)]
print(y)

z = [i for i in range(100) if i % 5 == 0]
print(z)

z2 = {i:0 for i in range(100) if i % 5 == 0}
print(z2)

z3 = {i for i in range(100) if i % 5 == 0}
print(z3)

z4 = tuple(i for i in range(100) if i % 5 == 0)
print(z4)