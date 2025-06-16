# a simple utiltiy to rerturn a nice pretty date string
import datetime

def makeDateString():
    ''' retrun a nicely formatted date'''
    now = datetime.datetime.now()
    return now

# what does Python call this module?
print(__name__)


if __name__ == '__main__':
    d = makeDateString()
    print(d)