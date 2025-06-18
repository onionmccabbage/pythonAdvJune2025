# rules for names
# letters numbers and underscore
# don't start with a digit
# avoid keywords

import random
import time
import threading

def myFn(n):
    ''' this is a normal function which sleeps for a random time '''
    for i in range(0,10):
        print(f'{n} is sleeping...')
        time.sleep( random.random()*0.1 ) # sleep for up to 0.1 of a second

if __name__ == '__main__':
    '''We may target any function to be run within a separate thread'''
    start = time.time()
    # NB one-member tuple MUST include a trailing comma (otherwise its just brackets)
    t1 = threading.Thread(target=myFn, args=(1,)) # we may also provide kwargs={}
    t2 = threading.Thread(target=myFn, args=(2,))
    t3 = threading.Thread(target=myFn, args=(3,))
    # threads cannot communicate with each other, they are completely separate
    t1.start() # here our new thread begin to run the function
    t2.start()
    t3.start()
    t1.join() # this will pause the main thread until the other thread completes
    t2.join() 
    t3.join()
    end = time.time()
    print(f'Total execution time: {end-start:0.2f} seconds') # about 0.5