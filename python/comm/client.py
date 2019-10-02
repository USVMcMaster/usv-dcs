from socket import socket, AF_INET, SOCK_STREAM

HOST = '192.168.100.180'  # The server's hostname or IP address; post deployment, use laptop ip
PORT = 5005        # The port used by the server

with socket(AF_INET, SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        while True:            
            data = s.recv(4096)        

            if data == b"('Key', 'BTN_MODE', 1)":
                s.send(b'kill_server')
                break
            else:
                s.send(b'working')

            print(data)
    except KeyboardInterrupt:
        print("\nexiting")
