# if more than one thread tries to access a global asset, we have a problem
from threading import Thread
from threading import Lock
import random
import time
count = 100
# we may use a lock to provide exclusive access for a thread
# now our code is thread-safe there is no collision when multiple threads access the same data
l = Lock()

def worker_A():
    '''Worker A will decrement count by one until we reach zero'''
    global count # this might be a database, an API, a file....
    l.acquire()
    while count >0:
        count -= 1
        print(f'Worker A sets count to {count}')
        # time.sleep(random.randint(0,1))
    l.release()

def worker_B():
    '''Worker B will increment count by one until we reach 200'''
    global count # this might be a database, an API, a file....
    l.acquire()
    while count <200:
        count += 1    
        print(f'Worker B sets count to {count}')
        # time.sleep(random.randint(0,1))
    l.release()

if __name__ == '__main__':
    print(count) # 100
    # NB be careful - we do not actually CALL the function here
    # a daemon thread will run as long as the main thread is running
    t1 = Thread(target=worker_A, daemon=True) # default is False
    t2 = Thread(target=worker_B)
    t2.start()
    t1.start()
    t2.join()
    t1.join()
    print(count)
