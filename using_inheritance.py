# classes may inherit from a parent (super)

class Parliamentarian():
    def __init__(self, name):
        self.name = name

class MP(Parliamentarian):
    '''We will also encode which party'''
    def __init__(self, name, party):
        # if we choose to pas the Class specifically we must also pass 'self'
        Parliamentarian.__init__(self, name)
        self.party = party

class CivilServant(Parliamentarian):
    '''we will encode the role'''
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

if __name__ == '__main__':
    # use our classes
    betty = Parliamentarian('Betty Boothroyd')
    lloyd = MP('Lloyd George', 'Liberal')
    humph = CivilServant('Humphrey', 'AI')
