# map and filter that use lambda functions

x = [1,2,3,4,12,657,33,875,93,62,87,673,612,789, 543]

# map will take all the elements of the list and use function to map them to new list

mp = map(lambda i: i+5, x)

print(list(mp))

# filter - tells whether or not we shuld include item in final list/filtered obj

fl = filter(lambda i: i % 2 == 0, x)

print(list(fl))