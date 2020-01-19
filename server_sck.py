import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = [] #connection objects will land here from ACCEPT function
all_address = [] #addresses(ip, port) will land here from ACCEPT function

def create_socket():
    try:
        print("Creating the socket!")
        global host
        global port
        global s
        host = "127.0.0.1"
        port = 9999
        s = socket.socket() # (socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as msg:
        print("Socket creation error: ", msg)

def bind_socket():
    try:
        print("Binding the port: ", port)
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print(f"Socket binding error: {msg}, Retrying...")
        bind_socket() #recursion

def socket_accept():
    print("Socket is now accepting connections!")
    conn, addr = s.accept() # yeni connection olana qeder block edir, sonra ise (conn, addr) tuplesine return edir
    print(f"Connection has been established {addr[0]} and on port {addr[1]}")
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8') # you can use str.decode()
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()


