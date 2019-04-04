from inputs import get_gamepad
import serial as ser
import time
import os

port = '/dev/ttyACM0'
s = ser.Serial(port,9600,timeout=5)
time.sleep(2)

def write_data(code,state):
	coded_data = "{},{}\r".format(code,state)
	s.write(coded_data.encode())
	s.flush()
	return coded_data

def forward_data():
	left_joy = 0
	right_trig = 0
	left_trig = 0
    
	try:
		while True:
			clear = lambda: os.system("clear")
			s.flush()

			events = get_gamepad()		
			for event in events:
				if event.state != 0:
					if event.state > 0:
						max_Ver = 32767
					else:                    
						max_Ver = 32768

					if event.code == "ABS_RZ":
						right_trig = event.state
						data = write_data(event.code,event.state)
						clear()
						print(data)

					if event.code == "ABS_Z":
						left_trig = event.state
						data = write_data(event.code,event.state)
						clear()
						print("ABS_Z:", left_trig)

					if event.code == "ABS_X":
						left_joy = event.state
						data = write_data(event.code,event.state)
						clear()
						print("ABS_X:", left_joy)
	
	except KeyboardInterrupt:
		s.close()
		pass

if __name__ == "__main__":
    forward_data()
