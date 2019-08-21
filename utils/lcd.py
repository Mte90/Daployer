from utils.analogzero import lcddriver
from utils.threaded import threaded


class LCD:

    def __init__(self):
        self.lcd = lcddriver.lcd()
        self.clear()

    def write(self, messages):
        if messages is not False:
            while len(messages) < 4:
                messages.append('')
            self.clear()
            self.lcd.lcd_display_string('{:^20}'.format(messages[0]), 1)
            self.lcd.lcd_display_string('{:^20}'.format(messages[1]), 2)
            self.lcd.lcd_display_string('{:^20}'.format(messages[2]), 3)
            self.lcd.lcd_display_string('{:^20}'.format(messages[3]), 4)

    @threaded
    def clear(self):
        self.lcd.lcd_clear()
