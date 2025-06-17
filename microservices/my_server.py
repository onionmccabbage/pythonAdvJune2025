# Microservices let us separate code into modules that interact over HTTP
import socket # this enables socket programming (i.e. microservices)

def server():
    '''this microservice will listen for requests on a port and respond'''
    # NB this has no security features - it is meant ot be isolated interally
    # we make a server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sensible choices for most cases
    # we need to dclare a port and an IP address
    port_t = ('localhost', 9876) # localhost ALWAYS means 127.0.0.1, i.e. your own local machine
    server.bind(port_t) # now our server has an IP address and a port to use
    # we can now start our server
    server.listen() # allow the server to accept requests from clients
    print(f'Server is running on {port_t[0]} port {port_t[1]}')
    # we need a run-loop to keep our server operating
    while True:
        # handle any requests from any client
        (client, addr) = server.accept() # unpack the accept object into a tuple of values
        # now we can begin to read whatever the client sent in the request
        buf = client.recv(1024) # choose to receive just the first bytes of the request
        print(f'Server received {buf}')
        if buf == b'quit': # b means we are expecting a byte-string
            # close our server
            server.close()
            client.close()
            break # this will break out of the run loop



if __name__ == '__main__':
    # run our server
    server()
