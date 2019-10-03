from socket import socket, AF_INET, SOCK_STREAM
# import controller.data_serializer as ds
# Socket config
HOST = '172.17.42.153'  # The server's hostname or IP address; post deployment, use laptop ip
PORT = 5005        # The port used by the server

# Serial config
SERIAL_PORT = '/dev/ttyACM0'
BAUDRATE = 9600

with socket(AF_INET, SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        # ds.create_serial(SERIAL_PORT, BAUDRATE)
        while True:            
            data = s.recv(4096)                 # Blocking

            if data == b"('BTN_MODE', 1)":
                s.send(b'kill_server')
                print("stopping client")
                break
            else:
                s.send(b'working')


            print(data)
            decoded_data = data.decode('utf-8').strip("()")
            event, state = decoded_data.split(',') 
            print(type(decoded_data), event, state)
            # ds.forward_data(event, state)

    except KeyboardInterrupt:
        print("\nexiting")
