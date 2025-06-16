# Abstract Base Class (ABC) may be useful
import abc

class MyAbsctract(abc.ABCMeta):
    '''An abstract base class (ABC) gives structure with NO implementation'''


# we then use our abstract base class to make concrete classes
class MyConcrete(MyAbsctract):
    '''Here we write the actual class'''

from abc import ABCMeta, abstractmethod

class AbstractShape(metaclass=ABCMeta): # we now have an abstract class
    '''Abstraction means we can declare properties and methods
    that we will need to implement in concrete classes'''
    __slots__ = ('__num_sides','__colour') # a tuple of permitted properties of this class
    @property # we may declare abstract properties
    @abstractmethod
    def num_sides(self, num_sides):
        pass # we make no implementation code within abstract
    @abstractmethod
    def __str__(self):
        '''All objects in Python will use their __str__ method when being printed
        We may oerride __str__ to implement our own print routine'''
        pass

if __name__ == '__main__':
    s = Shape()