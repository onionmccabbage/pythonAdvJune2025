# scope is programming concept
# sometimes called 'name-space'
# Everything that is not inside a code block is in the global scope
# Code within a code block is within a local scope

# Any Python module can be profiled using cProfile
# python -m cProfile -o prof_out using_scope.py

# here is a global entity
g = 'this is global' # NB we try to have a minimum amount of global entities

def fn():
    global g # we now have access to the global asset
    g ='this is local'
    return g

if __name__ == '__main__':
    print(g) # access the global entity
    print( fn() ) # access the local entity inside the function
    print(g) # access the global entity