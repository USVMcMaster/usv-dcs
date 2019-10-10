import serial
def create_serial(port, baudrate):
    return serial.Serial(port, baudrate)


def forward_state(ser, event, state):
    data = "{},{}\r".format(event, state)
    ser.write(data.encode())
    ser.flush()
