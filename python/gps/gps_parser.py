import serial
import pynmea2 as nmea

def create_ser(port, baud_rate):
    ser = serial.Serial(port, baud_rate)
    return ser

def serial_nmea_parser(ser, verbose = False):

    gps_data = ser.readline()

    if b'$GPGGA' in gps_data[0:6]:
        parsed_data = nmea.parse(gps_data.decode('utf-8'))

        if verbose:
            show_output(parsed_data)

        return parsed_data

def show_output(data):
    # Numeric representation
    print("lat:", data.lat, data.lat_dir,
          "lon:", data.lon, data.lon_dir)

    # NMEA format
    print("\nlatitude:", '%02d°%02d′%07.4f″' % (data.latitude,
                                              data.latitude_minutes,
                                              data.latitude_seconds))

    print("longitude:", '%02d°%02d′%07.4f″\n' % (data.longitude,
                                               data.longitude_minutes,
                                               data.longitude_seconds))


if __name__ == "__main__":
    ser = create_ser('/dev/ttyUSB0', 4800)
    try:
        while True:
            data = serial_nmea_parser(ser, True)
    except KeyboardInterrupt:
        print('stopping')
