# import from the Python standard library

# import ohter modules
import maths # our math.py is now available
from utility import makeDateString # only this function is imported

def doStuff():
    '''carry out operations'''
    n = maths.makeInt(5.5)
    d = makeDateString()
    return (n, d)

# Python will assign __main__ to the running module
# So this code ony executes if the module is run directly, not if it is imported elsewhere
if __name__ == '__main__':
    print(__name__)
    x = doStuff()
    print(x) # a tuple