from evdev import InputDevice, categorize, ecodes


class Numpad:

    def __init__(self, number_device):
        self.device = InputDevice('/dev/input/event' + number_device)
        self.device.grab()
        print('    ' + str(self.device))

    def get(self):
        for event in self.device.read_loop():
            if event.type == ecodes.EV_KEY:
                press = categorize(event)
                if press.key_down and press.keystate == 0:
                    button = press.keycode.replace('KEY_', '').replace('KP', '')
                    button = button.replace('ASTERISK', '*').replace('MINUS', '-')
                    button = button.replace('SLASH', '/').replace('DOT', '.')
                    return button

    def get_clean(self):
        button = self.get()
        button = button.replace('NUMLOCK', '')
        return button

    def sentence(self):
        looping = True
        strings = ''
        while looping:
            button = self.get_clean()
            if button == 'ENTER':
                return strings
            if button == 'BACKSPACE':
                strings = strings[:-1]
            elif button == 'TAB':
                strings = ''
            else:
                strings += button
