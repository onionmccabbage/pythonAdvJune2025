# we may write content into our database

import sqlite3

def writeDB():
    '''commit a data member into the database table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st   = '''
    INSERT INTO zoo
    VALUES ('Penguin', 18, 0.62)
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(f'Something went wrong {err}')


if __name__ == '__main__':
    writeDB()