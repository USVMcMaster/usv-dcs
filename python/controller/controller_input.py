from inputs import get_gamepad

def get_inputs():

        events = get_gamepad()

        for event in events:
            data = event.ev_type, event.code, event.state

        return data

if __name__ == "__main__":

    try:
        while True:
            print(get_inputs())
    except KeyboardInterrupt:
        pass