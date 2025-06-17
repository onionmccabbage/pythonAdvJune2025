import sqlite3
import json
import requests

def getAPIData():
    '''fetch JSON from API'''
    apiURL = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(apiURL)
    posts = response.json()
    return posts

def loadJSON():
    '''load JSON from a file'''
    fin = open('review2/posts.json', 'rt')
    with fin:
        posts_j = fin.read() # we now have some JSON
    posts_l = json.loads(posts_j) # convert the JSON to a list
    return posts_l
    

def main():
    # get data from API or from a file
    try:
        # attempt to get from API
        posts_l = getAPIData()
    except Exception as err:
        # if we can't get from API then load from a local file
        posts_l = loadJSON()
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # iterate over our structure
    # use '?' as a placeholder in SQL statements
    st = '''
    INSERT INTO posts
    VALUES (?, ?, ?, ?);
    '''
    for item in posts_l:
        try:
            curs.execute(st, (item['userId'], item['id'],item['title'], item['body']))
            conn.commit()
        except Exception as err:
            print('There was a problem:{}'.format(err))
        finally:
            pass
    # when done, we need to close our connection    
    conn.close() # always make sure the connection is closed

if __name__ == '__main__':
    main()