# we may read and display a profile from cProfile in the following manner:

import pstats

def main():
    '''open an existing profile report and display the results'''
    p = pstats.Stats('prof_out')
    p.print_stats()

if __name__ == '__main__':
    main()