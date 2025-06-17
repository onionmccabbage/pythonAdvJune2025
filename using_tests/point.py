# here is a class representing a point in 2-d space
class Point(object):
    '''
    class representing x y values of a point'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x)==int:
            self.__x = new_x
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y)==int:
            self.__y = new_y
        else:
            raise TypeError
    def display(self):
        return (self.x, self.y) # return a tuple
    def moveBy(self, dx=0, dy=0):
        '''move the point by dx and dy'''
        # validate
        if type(dx) == int and type(dy)== int:
            self.x += dx
            self.y += dy
        else:
            raise TypeError()


# we can write unittest to test the capabilities of our class (in another module)