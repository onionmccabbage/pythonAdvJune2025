# we may retrieve from DB tabdle using 'SELECT'

import sqlite3

def readDB():
    '''Retrieve values from the zoo table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st   = '''
    SELECT *
    FROM zoo
    '''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        conn.close()
    except Exception as err:
        print(f'Something went wrong {err}')
    # we can nicely format the 'rows' to show the content of the database
    for animal in rows: # there may be zero or more records
        print(f'We have {animal[1]} {animal[0]} each costing {animal[2]}')


if __name__ == '__main__':
    readDB()