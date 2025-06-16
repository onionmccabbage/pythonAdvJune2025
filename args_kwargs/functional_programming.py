# We may choose to write functional code
# We have choices about how we use function arguments

# a simple x-y function
# here we have two positional arguments
def point(x=3,y=4): # here we provide default values
    '''describe a point in 2-d space defined by x and y positions'''
    hypot = (x*x + y*y)**0.5
    return f'The point {x} and {y} is {hypot} long'

# a function taking just positional arguments
def useArgs( *args ):
    '''All positional arguments are gathered into a tuple named 'args' '''
    return args

# a function taking just keyword arguments
def useKWargs(**kwargs):
    '''All keyword arguments are gathered into a dcitionary'''
    return kwargs

if __name__ == '__main__':
    l = point(y=4, x=3) # we may choose to identify the arguments
    print(l) # 5.0
    m = point() # in the absence of any values, the defaults are used
    print(m) # 5.0
    # use the args and kwargs
    d = useArgs(3,7,2.5, True, 'clever', None, [])
    print(d, type(d))
    e = useKWargs(x=99, freda='Manager', age=42, nums=(5,4,3,2))
    print(e, type(e))