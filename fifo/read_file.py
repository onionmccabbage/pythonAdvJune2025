# we may read back from a text file using a file access object

def readFromFile():
    '''Retrieve the content from a text file'''
    fin = open('my_log.txt', 'rt') # 'rt' will read text
    with fin:
        r = fin.read() # read the entire contents of the file
    return r

if __name__ == '__main__':
    r = readFromFile()
    print(r, type(r))