# doctest is built in to Python
import doctest


def cubes(x):
    # we assert the expected outcome
    '''return the cube of x
    >>> cubes(3)
    27
    >>> cubes('3')
    Traceback (most recent call last):
        ...
    TypeError: x must be numeric
    '''
    if type(x) in (int, float):
        return x**3
    else:
        raise TypeError('x must be numeric')

if __name__ == '__main__':
    # c = cubes(3)
    # print(c) # 27
    # e = cubes('3')
    doctest.testmod()
