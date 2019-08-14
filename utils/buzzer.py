from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.tools import sin_values
from time import sleep


class Buzzer:

    def __init__(self, pin):
        self.buzzer = TonalBuzzer(pin)

    def beep(self):
        print('  Beep!')
        self.buzzer.play(Tone("A4"))

    def no(self):
        self.buzzer.stop()

    def siren(self):
        print('  Siren!')
        self.buzzer.source = sin_values()

    def scale(self, pick=1):
        music = ''
        pause = 1
        print('  Scale ' + pick + '!')
        if pick == 1:
            music = 'C4 D4 E4 F4 G4 A4 B4 C5'
            pause = 0.5
        elif pick == 2:
            music = 'G4 C4 A4 F4 E4 C4 D4'
        for note in music.split():
            tone = Tone(note)
            self.buzzer.play(tone)
            sleep(pause)
            self.no()

    # from https://www.raspberrypi.org/magpi/hack-electronics-gpio-zero-1-5/
    def pinkpanther(self):
        print('  Pink Panther!')
        tune = [('C#4', 0.2), ('D4', 0.2), (None, 0.2),
                ('Eb4', 0.2), ('E4', 0.2), (None, 0.6),
                ('F#4', 0.2), ('G4', 0.2), (None, 0.6),
                ('Eb4', 0.2), ('E4', 0.2), (None, 0.2),
                ('F#4', 0.2), ('G4', 0.2), (None, 0.2),
                ('C4', 0.2), ('B4', 0.2), (None, 0.2),
                ('F#4', 0.2), ('G4', 0.2), (None, 0.2),
                ('B4', 0.2), ('Bb4', 0.5), (None, 0.6),
                ('A4', 0.2), ('G4', 0.2), ('E4', 0.2),
                ('D4', 0.2), ('E4', 0.2)]

        for note, duration in tune:
            self.buzzer.play(note)
            sleep(float(duration))
        self.no()

    # https://github.com/junhaoliao/raspi/blob/master/tonalBuzzer.py
    def twinkle_twinkle(self):
        print('  Twinkle Twinkle!')
        tune = [
            "C4", "C4", "G4", "G4", "A4", "A4", "G4",
            "F4", "F4", "E4", "E4", "D4", "D4", "C4",

            "G4", "G4", "F4", "F4", "E4", "E4", "D4",
            "G4", "G4", "F4", "F4", "E4", "E4", "D4",

            "C4", "C4", "G4", "G4", "A4", "A4", "G4",
            "F4", "F4", "E4", "E4", "D4", "D4", "C4",
        ]

        cnt = 0
        for note in tune:
            self.buzzer.play(note)
            sleep(0.15)
            self.no()
            sleep(0.03)
            cnt += 1
            if (cnt == 7):
                cnt = 0
                sleep(0.15)
                self.no()

    def for_seconds(self, seconds, sound='beep'):
        print('  Beep for ' + seconds + '!')
        if sound == 'beep':
            self.beep()
        else:
            self.siren()
        sleep(seconds)
        self.no()
