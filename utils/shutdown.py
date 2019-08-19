from gpiozero import Button
from threading import Thread


class Shutdown(Thread):

    def __init__(self, pin):
        Thread.__init__(self)
        while True:
            pulsante = Button(pin, pull_up=True)
            if pulsante.is_pressed:
                exit()
