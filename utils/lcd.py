from utils.analogzero import lcddriver


class LCD:

    def __init__(self):
        self.lcd = lcddriver.lcd()
        self.clear()

    def write(self, messages):
        if messages is not False:
            messages = self.sanitize(messages)
            self.lcd.lcd_display_string('{:^20}'.format(messages[0]), 1)
            self.lcd.lcd_display_string('{:^20}'.format(messages[1]), 2)
            self.lcd.lcd_display_string('{:^20}'.format(messages[2]), 3)
            self.lcd.lcd_display_string('{:^20}'.format(messages[3]), 4)

    def sanitize(self, messages):
        while len(messages) < 4:
            messages.append('')
        return messages

    def clear(self):
        self.lcd.lcd_clear()
