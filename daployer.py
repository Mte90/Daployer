#!/usr/bin/env python3
import configparser
import os
from utils.numpad import Numpad
from utils.lcd import LCD
from utils.buzzer import Buzzer
from utils.shutdown import Shutdown


print('Daployer started...')
if not os.path.exists('config.ini'):
    print('Config file not found')
    exit()

print('  Config loaded!')

config = configparser.RawConfigParser()
config.read('config.ini')

if config.has_option('pin', 'shutdown'):
    shutdown = Shutdown(config.get('pin', 'shutdown'))
    shutdown.start()
key = Numpad(config.get('numpad', 'device'))
buzzer = Buzzer(config.get('pin', 'buzzer'))
lcd = LCD()


messages = ['', '', '', '']
buzzer.twinkle_twinkle()
for count in range(0, 4):
    messages[count] += str(key.sentence())

lcd.write(messages)
