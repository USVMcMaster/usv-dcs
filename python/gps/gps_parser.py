import serial
import pynmea2 as nmea
import time
import pdb

def create_ser(port, baud_rate):
    ser = serial.Serial(port, baud_rate)
    return ser

def filter_data(ser):

    gps_data = ser.readline()
    print("raw data:", gps_data)
    # # gps_data = gps_data.decode("utf-8")
    # # print("gps_data:", gps_data)


    # print("data: ", gps_data.decode("utf-8"))
    # # pdb.set_trace()

    parsed_gps_data = ''
    if gps_data.find(b'$GPGGA', 0, 8):
        print("valid data found")
        # parsed_gps_data = nmea.parse(gps_data)
        parsed_gps_data = gps_data
        print(parsed_gps_data)
    else:
        print("no valid data, trying again")
        filter_data(ser)
    return parsed_gps_data

if __name__ == "__main__":
    ser = create_ser('/dev/ttyUSB0', 4800)
    # ser.open()
    try:
        # while True:
        print(filter_data(ser))
        time.sleep(0.25)
        ser.close()
    except KeyboardInterrupt:
        print("exiting")
        ser.close()
