# we may also use classes to run threads
from threading import Thread
import random
import time

class MyClass(Thread):
    '''This class will be invoked in a new Thread'''
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n # we would usually have get/set methods to validate
    # we override the 'run' method
    def run(self): # remember every method of a class must take self
        '''When this class is invoked, this function will run in a new Thread'''
        for i in range(0,50):
            # print(f'{self.n} is sleeping ....')
            time.sleep( random.random()*0.1 )

if __name__ == '__main__':
    '''exercise the code'''
    start = time.time()
    # we need instances of our class
    thread_l = [] # we have an empty list
    for i in range(0,8): # we might have thousands of threads
        c = MyClass(i) # i will be 0, 1, 2 ...
        thread_l.append(c) # add our new instane into the list

    # next we iterate over the list to start each thread
    for thr in thread_l:
        thr.start()

    # finally we iterate over the threads to join each one
    for thr in thread_l:
        thr.join()

    c1 = MyClass(1) # we may pass in values for 'n'
    c2 = MyClass(2)
    # we start tem (on new threads)
    c1.start()
    c2.start()
    # optionally we join
    c1.join()
    c2.join()
    end = time.time()
    print(f'Total execution time: {end-start:0.2f} seconds')