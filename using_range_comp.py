# range, comprehension and generators
# the rnge object exists in memory, but all the values are provided on-demand
# For large amounts of data, this can be very efficient
r = range(0, 11) # start, stop-before, step
print(r, type(r))

# we may iterate over a range
for i in r:
    print(i, i*i)

# we may need a bunch of odd numbers
odds = range(-9, 10, 2)
for i in odds:
    print(i, end=', ')
print('\n')

# comprehension and generator
# here, comprehsion means deal with every member of a collection comprehensively
squares = (i**i for i in range(0,11))
print(squares, type(squares))
for i in squares:
    print(i, end=', ')
print('\n')

# also note... square brackets will comprehensively populate a list
cubes  =[i**3 for i in range(0,11)]
print(type(cubes), cubes)