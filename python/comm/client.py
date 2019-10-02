from socket import socket, AF_INET, SOCK_STREAM

HOST = 'localhost'  # The server's hostname or IP address; post deployment, use laptop ip
PORT = 5005        # The port used by the server

with socket(AF_INET, SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        while True:            
            data = s.recv(4096)        

            if data == b"stop_client":
                break

            print(data)
    except KeyboardInterrupt:
        print("\nexiting")