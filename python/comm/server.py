from socket import socket, AF_INET, SOCK_STREAM

# SOCK_STREAM is for TCP. Alternatively use import SOCK_DGRAM for UDP


HOST = 'localhost'      # 127.0.0.1
PORT = 5000             # Arbritary port > 1024


with socket(AF_INET, SOCK_STREAM) as s:     # Auto close socket, no need to use s.close
    
    s.bind((HOST, PORT))                    # AF_INET (IPv4)
    s.listen()                              # Monitor socket

    conn, addr = s.accept()                 # Blocking while waiting for connection. 
                                            # Returns socket object on connection

    with conn:
        print('Connected by', addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)