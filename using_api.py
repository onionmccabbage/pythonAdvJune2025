# we may access data from API end-points over http(s)
import requests


def getData(n):
    url = f'https://jsonplaceholder.typicode.com/users/{n}'
    data = requests.get(url)
    # NB Python will intelligently convert the incoming data to a Python structure
    return data.json() # or data.xml() or data.text()

if __name__ == '__main__':
    r = getData(3) # pass in an argument to be used in the REST URL
    print(r)