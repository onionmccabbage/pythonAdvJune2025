# we may need to ask for the user to enter data
import random

z = random.randint(0,10) # a random integer 0-10

def getInfo():
    '''ask the user to enter a value
    - if it is numeric, convert to a number
    - if not, just return the value'''
    # Remember - every input is ALWAYS a string value
    k = input('Please enter a value: ')
    if k.isnumeric():
        k = int(float(k))
    # remember to return something!
    return k

def myRunLoop():
    '''This will continually run until we break'''
    while True:
        q = random.randint(0,10)
        if q == z:
            break # this will break out of our endless loop
        else:
            print(q,z)

if __name__ == '__main__':
    r = getInfo()
    print(r, type(r))
    print(z)
    # exercise our function
    myRunLoop()