#/dev/ttyACM0 is a USB communication device (CDC) of sub-type "abstract control model" (ACM). That is what the USB GPS reciever device is. 
#$GPRMC - Recommended minimum specific GPS/Transit data

import serial

gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)

while True: 
	line = gps.readline()
	data = line.split(",")
	if data[0] == "$GPRMC":
		if data [2] == "A":
			print "Latitude: %s" % ( data[3] ) 
			print "Longitude: %s" % ( data [5] )

