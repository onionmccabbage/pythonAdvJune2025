#  When we run Python we may choose to inject string data from the system
import sys # this gives access to the operating system

# the system arguments all live in a list
# We may run a file and inject arguments
# python using_system_args.py data goes here
# NB All sys.args are STRING
for i in sys.argv:
    print(i)
