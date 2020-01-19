import socket
import os
import subprocess
import time

class client:

    def __init__(self, host, port):
        self.sck = None
        self.host = host
        self.port = port
        print("Client object has been created!")

    def create_socket(self):
        self.sck = socket.socket()

    def connect(self):
        try:
            self.create_socket()
            self.sck.connect((self.host, self.port))
            print(f"connected to the server {self.host} on port {self.port} successfully")
        except Exception as e:
            print(f"OOPS Something gone wrong! {e}. Retrying...")
            time.sleep(3)
            self.connect()

    def receiveData(self):
        while True:
            data = self.sck.recv(2)
            data_decoded = data.decode('utf-8')
            print(data_decoded)


client1 = client("0.0.0.0", 9999)
client1.connect()
client1.receiveData()

