from inputs import get_gamepad

# TODO: Convert script to class to allow to be interfaced with motors


# class Controller:
    # def __init__(self):
    #     self.events = get_gamepad()


def get_inputs():
    while 1:
        events = get_gamepad()

        for event in events:
            print(event.ev_type, event.code, event.state)

if __name__ == "__main__":
    # c = Controller()
    # c.get_inputs()
    get_inputs()