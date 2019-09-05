from inputs import get_gamepad
import serial as ser
import time
import os
import pdb

port = '/dev/ttyACM0'
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
    joy_threshold = 0.5
    joy_center = 128
    joy_max = 32767    

    right_trig = 0
    left_trig = 0
    left_joy = 0

    forward_requested = False
    reverse_requested = False
    joy_requested = False

    try:
        while True:
            clear = lambda: os.system("clear")
            s.flush()

            events = get_gamepad() 

            for event in events:
                if event.state != 0:
                                        
                    if event.code == "ABS_RZ": # Forward direction
                        forward_requested = True
                        right_trig = get_trigger_val(event.state, deadband, trigger_max)

                    if event.code == "ABS_Z": # Reverse direction
                        reverse_requested = True
                        left_trig = get_trigger_val(event.state, deadband, trigger_max)

                    if event.code == "ABS_X":
                        joy_requested = True
                        left_joy = get_joy_val(event.state, joy_center, joy_max)

                    if (forward_requested or left_joy >= 0.05) and joy_requested:
                        forward_lower_t1 = round((-joy_threshold * left_joy) + right_trig,2)
                        command = "flt1"
                        clear()
                        
                        if forward_lower_t1 > 0:
                            print("Command:", command, "Value:", forward_lower_t1)
                            forward_requested = False

                        joy_requested = False

                    elif (forward_requested or left_joy <= -0.05) and joy_requested:
                        forward_lower_t2 = round((joy_threshold * left_joy) + right_trig,2)
                        command = "flt2"
                        clear()

                        if forward_lower_t2 > 0:
                            print("Command:", command, "Value:", forward_lower_t2)
                            forward_requested = False

                        joy_requested = False


                    elif forward_requested:
                        forward_lower_null = right_trig
                        command = "fln"
                        clear()

                        print("Command:", command, "Value:", forward_lower_null)
                        forward_requested = False

        time.sleep(0.01)
    
    except KeyboardInterrupt:
        s.close()
        pass

if __name__ == "__main__":
    forward_data()
