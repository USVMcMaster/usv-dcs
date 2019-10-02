from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import controller.controller_input as ci            # use for full rollout
from inputs import get_gamepad

# Use SOCK_STREAM for TCP
# Use SOCK_DGRAM for UDP

HOST = 'localhost'      # Accept all ip
PORT = 5005             # Arbritary port > 1024

with socket(AF_INET, SOCK_STREAM) as s:     # Auto close socket, no need to use s.close
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))                    # AF_INET (IPv4)
    s.listen()                              # Monitor socket

    conn, addr = s.accept()                 # Blocking while waiting for connection. 
                                            # Returns socket object on connection
    with conn:
        print('Connected by', addr)
        print("sending")

        try:
            while True:
                data = ci.get_inputs()
                conn.send(bytes(str(data), encoding='utf8'))

                status = conn.recv(1024)
                # if status == b"('Key', 'BTN_MODE', 1)":
                #     break
        except KeyboardInterrupt:
            print("\nexiting")
        # conn.send(b"test")
        # print("sent")

        # while True:
        #     # ci.get_inputs()
        #     data = conn.recv(1024)
        #     if not data:
        #         break
            # conn.sendall(data)

