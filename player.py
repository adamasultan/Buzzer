from machine import Pin

class Player():
    def __init__(self, number, button_pin, color_pin):
        self.number = number
        self.button_pin = button_pin
        self.color_pin = color_pin
    