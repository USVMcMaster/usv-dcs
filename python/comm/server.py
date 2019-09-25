from socket import socket, AF_INET, SOCK_STREAM
import controller.controller_input as ci            # use for full rollout
from inputs import get_gamepad
# SOCK_STREAM is for TCP. Alternatively use import SOCK_DGRAM for UDP


HOST = '0.0.0.0'      	# Accept all ip
PORT = 5005             # Arbritary port > 1024


with socket(AF_INET, SOCK_STREAM) as s:     # Auto close socket, no need to use s.close
    
    s.bind((HOST, PORT))                    # AF_INET (IPv4)
    s.listen()                              # Monitor socket

    conn, addr = s.accept()                 # Blocking while waiting for connection. 
                                            # Returns socket object on connection

    with conn:
        print('Connected by', addr)

        while True:
            # ci.get_inputs()
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
