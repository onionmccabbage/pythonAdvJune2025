#  When we run Python we may choose to inject string data from the system
import sys # this gives access to the operating system
import os

print(os.getcwd(), os.name)

# the system arguments all live in a list
# We may run a file and inject arguments
# python using_system_args.py data goes here
# NB All sys.args are STRING
for i in sys.argv:
    print(i)

# the sys has a 'path' which is all the places Python will look for imports
sys.path.append('D:\\pythonAdvJune2025\\architecture')
print(sys.path)

print(sys.version, sys.platform)