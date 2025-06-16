# We can be more controlled about file output using 'write'

def writeToFile(s):
    '''Use a file access object to write to a text file'''
    # 'x' means exclusive access
    fout = open('my_log.txt', 'wt') # 'w' will (over)write the file
    with fout: # NB 'with' will close the file access object when done
        fout.write(s)
        fout.write('\n') # \n is the new line character

if __name__ == '__main__':
    w = 'further details to remember'
    writeToFile(w)