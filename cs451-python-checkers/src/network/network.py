import socket
import time
import json

class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This input will want to be intergrated with the UI if possible
        # print("Please enter the IP that the Server owner provides")
        self.server = ip#(socket.gethostbyname(socket.gethostname()))
        self.address = (self.server, 1234)
        self.pos = self.connect()
        #self.client.setblocking(0)

    def set_board(self, _board):
        self.board = _board

    def get_board(self):
        return self.board

    def get_pos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            json_string = json.dumps(data)
            print(json_string)
            self.client.send(json_string.encode())
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send_text(self, data):
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)



    def wait(self):
        print("waiting....")
        time.sleep(1)
