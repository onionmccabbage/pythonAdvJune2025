import sqlite3 # built in database that comes with Python

def main():
    conn = sqlite3.connect('my_db') # create the database if not exist
    curs = conn.cursor()
    # in this database I intend to store 'post' items
    # userID integer
    # id integer (and primary key)
    # title is a string
    # completed is boolean (SQL uses true/false)
    st = '''CREATE TABLE IF NOT EXISTS posts 
    (userID int,
    id INT PRIMARY KEY,
    title VARCHAR(32),
    body VARCHAR(256)
    );'''
    # we can execute the statement
    curs.execute(st)
    # commit and close the connection
    conn.commit() # without this the xchanges will not persist in the db
    conn.close()

if __name__ == '__main__':
    main()