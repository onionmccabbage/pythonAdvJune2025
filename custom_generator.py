# We can write our own custom generator
import datetime
import time
# we can use built-in generator syntax

evens = (i for i in range(0, 101, 2))
print(type(evens))

def dt():
    '''provide a niely formatted datetime stamp'''
    while True: # run forever
        # strftime lets us string-format a time object
        ts = datetime.datetime.now().strftime('%H:%M:%S %m-%D-%y')
        # any function may be a generator: use yield instead of return
        yield ts

if __name__ == '__main__':
    # we need an instance of our generator
    inst = dt()
    # then we may use the instance to generate values
    # for i in inst:
    #     print(i)
    # if we choose we may ask for a single yield
    result=inst.__next__()
    print(result)