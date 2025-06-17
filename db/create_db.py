# we may create a database and a table like this

import sqlite3 # or any other DB connection tool

def accessDB():
    '''access a database'''
    # we need a connection object and a cursor
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # then we need an SQL statement
    st = 'CREATE TABLE zoo ( creature VARCHAR(32) PRIMARY KEY, count INT, cost FLOAT )'
    # usually we wrap this in try...except
    curs.execute(st) # at this point the SQL is sent to the DB
    conn.commit()    # here the SQL is implemented and the DB may change
    conn.close()     # always tidy up when done


if __name__ == '__main__':
    accessDB()