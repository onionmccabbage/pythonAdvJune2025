# we write a simple socket client
import sys
import socket 

def client():
    '''This client will make requests to our socket server'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9876)
    # we need to make a request connection to our server
    sock.connect( port_t )
    # if there are any extra system argument variables  send them to the server
    if len(sys.argv)>1:
        message = ' '.join(sys.argv[1:]) # use slicing to send all but ember zero
    # otherwise send a generic message
    else:
        message = 'hello'

    sock.send(message.encode()) # we are obliged to encode all communication over http

if __name__ == '__main__':
    client()