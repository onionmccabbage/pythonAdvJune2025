# we may insert many values into a DB
import sqlite3


def populateDB():
    '''commit each member of a collection into the DB'''
    creatures_t = (
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    ) 
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # We may need to pass parameters into our SQL statement using ?
    st   = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    # iterte over our tuple
    for item in creatures_t:
        # we should do some validation here
        if type(item['creature'])==str:
            n = item['creature']
        else:
            raise TypeError('Creature name must be a string')
        if type( item['count'] )==int:
            c = item['count']
        else:
            raise TypeError('Count must be an integer')
        if type(item['cost'])==float:
            co = item['cost']
        else:
            raise TypeError('Cost must be a float')
        try:
            curs.execute(st, (n, c, co))
            conn.commit()
        except Exception as err:
            print(err)
    conn.close() # remember to tidy up



if __name__ == '__main__':
    populateDB()