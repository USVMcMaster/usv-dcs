import serial
def create_serial(port, baudrate)
    return serial.Serial(port, baudrate)


def forward_state(event, state):
    data = "{},{}\r".format(event, state)
    s.write(data.encode())
    s.flush()
