from evdev import InputDevice, categorize, ecodes
from utils.threaded import threaded


class Numpad:

    track_key_for_lcd = {}

    def __init__(self, number_device, lcd):
        self.device = InputDevice('/dev/input/event' + number_device)
        self.device.grab()
        self.lcd = lcd
        print('    ' + str(self.device))
        self.did_you_press_for_lcd()

    @threaded
    def did_you_press_for_lcd(self):
        for event in self.device.read_loop():
            if self.track_key_for_lcd:
                pressed = self.in_loop_is_key_down(event)
                for button in self.track_key_for_lcd:
                    if pressed == button:
                        print('   Button ' + str(button) + ' pressed')
                        self.lcd.write(self.track_key_for_lcd[button]())

    def get(self):
        for event in self.device.read_loop():
            return self.in_loop_is_key_down(event)

    def in_loop_is_key_down(self, event):
        if event.type == ecodes.EV_KEY:
            press = categorize(event)
            if press.key_down and press.keystate == 0:
                return self.convert(press.keycode)

    def signal_and_print(self, button, callback):
        self.track_key_for_lcd[button] = callback

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

    def convert(self, button):
        button = button.replace('KEY_', '').replace('KP', '')
        button = button.replace('ASTERISK', '*').replace('MINUS', '-')
        button = button.replace('SLASH', '/').replace('DOT', '.')
        button = button.replace('PLUS', '+')

        return button
