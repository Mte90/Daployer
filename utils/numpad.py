from evdev import InputDevice, categorize, ecodes
from utils.threaded import threaded


class Numpad:

    def __init__(self, number_device, lcd):
        self.device = InputDevice('/dev/input/event' + number_device)
        self.device.grab()
        self.lcd = lcd
        print('    ' + str(self.device))

    def get(self, key=False):
        for event in self.device.read_loop():
            if event.type == ecodes.EV_KEY:
                press = categorize(event)
                if press.key_down and press.keystate == 0:
                    button = press.keycode.replace('KEY_', '').replace('KP', '')
                    button = button.replace('ASTERISK', '*').replace('MINUS', '-')
                    button = button.replace('SLASH', '/').replace('DOT', '.')
                    if key is not False:
                        if button is key:
                            return True
                        else:
                            return False

                    if key is False:
                        return button

    @threaded
    def signal_and_print(self, button, callback):
        items = self.signal(button, callback)
        print(items)
        #self.lcd.write(items)

    @threaded
    def signal(self, button, callback):
        while self.get(button):
            pass
        return callback()

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
