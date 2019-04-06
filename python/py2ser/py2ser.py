from inputs import get_gamepad
import serial as ser
import time
import os

port = '/dev/ttyACM1'
s = ser.Serial(port,9600,timeout=5)
time.sleep(2)

def write_data(event_code,state):
  coded_data = "{},{}\r".format(event_code,state)
  s.write(coded_data.encode())
  s.flush()
  return coded_data

def get_trigger_val(state, deadband, trigger_max):

    if state <= deadband: # Correcting for deadband
        state = 0

    trig_val = round(state/trigger_max, 2)

    return trig_val

def get_joy_val(state, center, limit):

    joy_val = round((state - center)/(limit - center),2)

    if joy_val < -1.0: # Correcting for overshoot due to negative raw value
        joy_val = -1.0

    return joy_val

def forward_data():
    
    deadband = 31
    trigger_max = 255
    joy_center = 128
    joy_max = 32767

    try:
        while True:
            clear = lambda: os.system("clear")
            s.flush()

            events = get_gamepad()      
            for event in events:
                if event.state != 0:
                    
                    if event.code == "ABS_RZ":
                        right_trig = get_trigger_val(event.state, deadband, trigger_max)
                        data = write_data(event.code,right_trig)

                        clear()
                        print("ABS_RZ:", right_trig, ":")


                    if event.code == "ABS_Z":
                        left_trig = get_trigger_val(event.state, deadband, trigger_max)
                        data = write_data(event.code,left_trig)

                        clear()
                        print("ABS_Z:", left_trig, ":")

                    if event.code == "ABS_X":
                        
                        left_joy = get_joy_val(event.state, joy_center, joy_max)
                        data = write_data(event.code,left_joy)

                        clear()
                        print("ABS_X:", left_joy, ":")
    
    except KeyboardInterrupt:
        s.close()
        pass

if __name__ == "__main__":
    forward_data()
