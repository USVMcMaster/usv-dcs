from socket import socket, AF_INET, SOCK_STREAM

HOST = '10.42.0.1'  # The server's hostname or IP address; post deployment, use laptop ip
PORT = 5000        # The port used by the server

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', str(data))
# print('Received', repr(data))
