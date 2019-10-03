from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import controller.controller_parser as cp 
import time

# Use SOCK_STREAM for TCP
# Use SOCK_DGRAM for UDP

# socket config
HOST = '0.0.0.0'        # Accept all ip
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
                data = cp.get_data()
                
                if data is not None:
                    print(data)
                    conn.send(bytes(str(data), encoding='utf8'))
                
                else:
                    continue

                status = conn.recv(1024)
                if status == b'kill_server':
                    print("stopping server")
                    break

                time.sleep(0.015)
        except KeyboardInterrupt:
            print("\nexiting")
        # conn.send(b"test")
        # print("sent")

        # while True:
        #     # ci.get_data()
        #     data = conn.recv(1024)
        #     if not data:
        #         break
            # conn.sendall(data)

