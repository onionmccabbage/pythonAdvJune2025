# here are some useful mathematical functions

def makeInt(n):
    '''Try to convert n to an integer
    - if n is a string, try to find teh numeric part
    - if n is a float, make it an integer
    - if else, raise TypeError'''
    if type(n) == str:
        try:
            n_numeric = int(float(n)) # convert to float then to int
        except Exception as err:
            n_numeric == 1 # a sensible default
    elif type(n) in (int, float):
        n_numeric = int(n) # just make it into an integer
    else:
        raise TypeError('Cannot work with non-numeric values')
    return n_numeric

if __name__ == '__main__':
    x = makeInt(4.6) # always rounds down!!!
    y = makeInt(3)
    z = makeInt('55.32353')
    print(x, y ,z) # 4, 3, 55