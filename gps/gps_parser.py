import serial
import pynmea2 as nmea

def create_ser(port, baud_rate):
    return lambda ser : serial.serial(port, baud_rate)

def filter_data(ser):
    gps_data = str(ser.readline())
    
    if gps_data.find('$GPGGA'):
        parsed_gps_data = nmea.parse(gps_data)

    return parsed_gps_data

if __name__ == "__main__":
    ser = create_ser('/dev/ttyUSB0', 4800)
    filter_data(ser)
