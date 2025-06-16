# the easiest way to persist data into a file is to use print

def printToFile(s):
    '''use print to send 's' to a text file'''
    # we need a file access object
    fout = open('my_log.txt', 'at') # 'at' will append text
    print(s, file=fout)
    fout.close() # remember to tidy up

if __name__ == '__main__':
    words = 'here is some important information'
    printToFile(words)