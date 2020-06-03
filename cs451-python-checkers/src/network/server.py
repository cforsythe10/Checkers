import socket
from _thread import *
import sys
import json

class Server:
    def grab_ip(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect(('10.0.222.111', 1))
            ip = sock.getsockname()[0]
        except:
            ip = '127.0.0.1'
        finally:
            sock.close()
        return ip

    def thread_client(self,clientsocket, player_num):
        clientsocket.send(str.encode("Connected"))
        msg = ""
        while True:
            try:
                data = clientsocket.recv(2048)
                msg = data.decode("utf-8")

                if not data:
                    print("Disconnected")
                    break
                else:
                    print("Received", msg)

                    print("Sending", msg)
                clientsocket.sendall(str.encode(msg)) #sends encoded message to client
            except:
                print("Error")
                break
        print ("Connection Terminated")
        clientsocket.close()

    def send_text(self, data):
        try:
            self.clientsocket.send(str.encode(data))
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return self.clientsocket.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            json_string = json.dumps(data)
            print(json_string)
            self.clientsocket.send(json_string.encode())
        except socket.error as e:
            print(e)

    def get_ip(self):
        return self.grab_ip()

    def run_server(self, server):
        # server = self.grab_ip()#(socket.gethostbyname(socket.getfqdn())) #gets current IP automatically. NOTE clients must be on the same network
        print(server)

        #creation of socket object uses IPV4 connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # binds socket to a ip and port number
            s.bind((server, 1234))

        #if it does not work error printed to console
        except socket.error as e:
            str(e)

        s.listen(2) #opens port for up to 2 clients
        print("Awaiting connection...")


        player_num = 0 #used to track which player is moving
        #while True:
        clientsocket, address = s.accept()
        self.clientsocket = clientsocket
        self.address = address
        print("Conncection made to:", address)
        #self.thread_client(clientsocket, player_num)
        #start_new_thread(self.thread_client, (clientsocket, player_num)) #thread allows for the program to continue while the function executes
        player_num += 1
        self.clientsocket.send(str.encode("Connected"))

    def get_board(self):
        return self.board

    def set_board(self, _board):
        self.board = _board

    def get_server(self):
        serv = start_new_thread(self.run_server, ())
        return self

    def __init__(self):
        print("")
