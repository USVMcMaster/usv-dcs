from inputs import get_gamepad

# ABS_Y: Left stick up/down
# ABS_RY: Right stick up/down
# ABS_Z: Left trigger
# ABS_RZ: Right trigger
# BTN_TL: Left button
# BTN_TR: Right button

joystick_events = ['ABS_Y', 'ABS_RY']
trigger_events = ['ABS_Z', 'ABS_RZ']
button_events = ['BTN_TL', 'BTN_TR', 'BTN_MODE']

joy_rest_value = 128
joy_neg_limit = -32767
joy_pos_limit = 32768

trigger_deadband = 31
trigger_limit = 255

def get_joy_val(joy_input, joy_rest_value, joy_neg_limit, joy_pos_limit):

    if joy_input > 0:
        return round((joy_input - joy_rest_value)/(joy_pos_limit - joy_rest_value),2)

    else:
        return round((joy_input - joy_rest_value)/(joy_neg_limit - joy_rest_value),2) *-1

def get_trig_val(trig_input, trigger_deadband, trigger_limit):
    
    if trig_input < trigger_deadband:
        return 0.00

    else:
        return round((trig_input/trigger_limit),2)

def get_data():
    
    events = get_gamepad()

    for event in events:

        if event.code in joystick_events:
            return event.code, get_joy_val(event.state*-1, joy_rest_value, joy_neg_limit, joy_pos_limit)

        elif event.code in trigger_events:
            return event.code, get_trig_val(event.state, trigger_deadband, trigger_limit)

        elif event.code in button_events:
            return event.code, event.state

if __name__ == "__main__":
    
    try:
        while True:
            data = get_data()
            if data is not None:
                print(type(data), data)
    except KeyboardInterrupt:
        print("\nexiting")