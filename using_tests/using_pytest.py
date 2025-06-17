from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


# remember we may need to pip install pytest

# we invoke pytest like this:
# python -m pytest -v using_pytest.py


def testDefaults():
    '''Using no parameters should result in the defaults'''
    tA = Task() # this will invoke the default values
    tC = Task(None, None, False, None)
    assert tA == tC

if __name__ == '__main__':
    tDemo = Task('....', 'Floella', False, 896587)
    print(tDemo, type(tDemo))