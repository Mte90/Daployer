from evdev import InputDevice, categorize, ecodes
from utils.threaded import threaded
from time import sleep

class Numpad:

    track_key_for_lcd = {}
    enqueue = ''

    def __init__(self, number_device, lcd, launcher):
        self.device = InputDevice('/dev/input/event' + number_device)
        self.device.grab()
        self.lcd = lcd
        self.launcher = launcher
        print('    ' + str(self.device))
        self.run_device_loop()

    @threaded
    def run_device_loop(self):
        for event in self.device.read_loop():
            self.did_you_press_for_lcd(event)
            self.did_you_pick(event)

    def did_you_press_for_lcd(self, event):
        if self.track_key_for_lcd:
            pressed = self.in_loop_is_key_down(event)
            for button in self.track_key_for_lcd:
                if pressed == button:
                    print('   Button ' + str(button) + ' pressed')
                    self.lcd.write(self.track_key_for_lcd[button]())

    def did_you_pick(self, event):
        pressed = self.in_loop_is_key_down(event)
        for button in range(0, 9):
            if pressed == str(button):
                self.enqueue += str(button)
                self.lcd.write(['', 'Press the number:', self.enqueue, ''])
            elif pressed == 'ENTER':
                status, message = self.launcher.run(self.enqueue)
                self.lcd.write(message)
                if not status:
                    sleep(1)
                    self.lcd.write(self.get_page(1))

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
