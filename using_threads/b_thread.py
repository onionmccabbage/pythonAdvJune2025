# we may also use classes to run threads
from threading import Thread
import random
import time

class MyClass(Thread):
    '''This class will be invoked in a new Thread'''
    def __init__(self):
        Thread.__init__(self)
    # we override the 'run' method
    def run(self): # remember every method of a class must take self
        '''When this class is invoked, this function will run in a new Thread'''
        for i in range(0,50):
            print(f'Sleeping ....')
            time.sleep( random.random()*0.1 )

if __name__ == '__main__':
    '''exercise the code'''
    start = time.time()
    # we need instances of our class
    c1 = MyClass()
    c2 = MyClass()
    # we start tem (on new threads)
    c1.start()
    c2.start()
    # optionally we join
    c1.join()
    c2.join()
    end = time.time()
    print(f'Total execution time: {end-start:0.2f} seconds')