from socket import socket, AF_INET, SOCK_STREAM

HOST = 'localhost'  # The server's hostname or IP address; post deployment, use laptop ip
PORT = 5005        # The port used by the server

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'test')
