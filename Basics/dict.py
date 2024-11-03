# key-value pairs
x = {'Key': 89}
print(x['Key'])

x['Key2'] = 87

print(x)

x[2] = 90

print(x)

x[3] = [4,3,1,2,5]

print(x)

print(2 in x)

print(x.values())
print(x.keys())

print(list(x.values()))

print(list(x.keys()))

del x['Key']

print(x)

for k, v in x.items():
    print(f'key: {k}, val: {v}')