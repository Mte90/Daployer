#!/usr/bin/env python3
import configparser
import os
from utils.numpad import Numpad
from utils.lcd import LCD
from utils.buzzer import Buzzer
from utils.shutdown import Shutdown
from utils.launcher import Launcher

version = '1.0.0 alpha'

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
lcd = LCD()
launcher = Launcher()
key = Numpad(config.get('numpad', 'device'), lcd, launcher)
buzzer = Buzzer(config.get('pin', 'buzzer'))
lcd.clear()

messages = ['Welcome to Daployer', version, '', 'Loading in progress']
lcd.write(messages)
buzzer.for_seconds(1)

lcd.write(launcher.get_page(1))

key.signal_and_print('+', launcher.next_page)
key.signal_and_print('-', launcher.previous_page)

# To let the program still running with the other stuff async
while True:
    pass
