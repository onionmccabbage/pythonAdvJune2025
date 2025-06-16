# Class encapsulate code

a = 5   # 
b = 7.5 #
# we also have boolean, None
# collections
s = 'string' # an ordinal immutable collection of characters
s = 'changed'
# we can use slicing
print( s[0:6] ) # slicing start:stop-before:step
# list and tuple
# both ordinal collections of any data type

# dict - a non ordinal collection of key:value pairs
# e.g. a person has a name, age, email
gail = {'name':'Gail', 'age':42, 'email':'gail@hmrc.gov.uk'}

# here is a class
class Person:
    # we may choose to pass in data we wish to persist
    __slots__ = ['__name' , '__age', '__email'] # we restrict the permitted properties of this class
    def __init__(self, name, age, email): # 'self' must appear in class methods
        self.name  = name # we attach the incoming arguments to 'self'
        self.age   = age  # NB this calls the setter function
        self.email = email
    # property decorators, name mangling and __slots__
    @property # the get-method (the accessor)
    def name(self):
        return self.__name # the double-underscore will 'namgle' the property
    @name.setter # the set method (the mutator)
    def name(self, new_name):
        ''' we can validate the name to be a non-empty string'''
        if type(new_name) == str and new_name != '':
            self.__name = new_name # mangled properties cannot be accessed outside the class
        else:
            raise TypeError('Name must be a non empty string') # this will cause an exception
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        '''age must be a positive int or float'''
        if type(new_age) in (int, float) and new_age >0:
            self.__age = new_age
        else:
            self.__age = 24 # choose a sensible default
    # challenge: write the get/set for 'email' which must be a non-empty string
    @property
    def email (self):
        return self.__email
    @email.setter
    def email(self, new_email):
        ''' email must be non-empty string'''
        if type(new_email) == str and new_email !='':
            self.__email = new_email
        else:  
            raise TypeError('Email must be a non-empty string')

# we can execise the code
if __name__ == '__main__':
    # we may create instances of our class
    g = Person('Gail', 42, 'gail@hmrc.gov.uk') # every time we make an instance, the __init__ will run
    # we may print the class members
    print( g.name, g.age, g.email )
    # me may mutate the name
    g.name = 'Galena' # this calls the setter method
    print(g.name)
    # we can also mutate the age
    g.age = -99 # this should use the default of 24
    print(g.age) # 24
    # play with the email
    g.email = 'galena@hmrc.gov.uk'
    print(g.email)

    # we often need to handle exceptions
    try:
        g.__name = 'Gertrude' # this should fail
        g.name = 55 # this should raise our TypeError
    except TypeError as te:
        print(te)
    except AttributeError as ae:
        print(ae)
    except Exception as err: # we always handle general exceptions last
        print('Something unexpected has gone wrong')
    finally:
        print('this code runs even if there is an exception')