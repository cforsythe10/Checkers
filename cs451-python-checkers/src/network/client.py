import socket
from network import Network

#game code goes here plus implementation of network object

def main ():
    network = Network()
    network.connect()
    while(1):
        response = network.send("hello")#This is where gameboard needs to send
        # do thing about checkerboard here
        print('response was "%s"' % response)
        network.wait()

if __name__ == '__main__':
    main()
