import time
from machine import Pin
from machine import PWM

class Buzzer():
  def __init__(self, song = 0):
    self.song = song
    self.buzzer = PWM(Pin(32, Pin.OUT))
    self.set_notes()

  def set_notes(self):
    self.c3 = 131
    self.c3sharp = 139
    self.d3 = 147
    self.d3sharp = 156
    self.e3 = 165
    self.f3 = 175
    self.f3sharp = 185
    self.g3 = 196
    self.g3sharp = 208
    self.a3 = 220
    self.a3sharp = 233
    self.b3 = 247
    self.c4 = 262
    self.c4sharp = 277
    self.d4 = 294
    self.d4sharp = 311
    self.e4 = 330
    self.f4 = 349
    self.f4sharp = 370
    self.g4 = 392
    self.g4sharp = 415
    self.a4 = 440
    self.a4sharp = 466
    self.b4= 494

  def play_jeopardy_song(self):
    self.buzzer.duty_u16(32768)
    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.d4)
    time.sleep(0.5)
    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.d3)
    time.sleep(0.5)

    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.d4)
    time.sleep(0.5)
    self.buzzer.freq(self.a3)
    time.sleep(1)

    #self.buzzer.freq(20)
    self.buzzer.duty_u16(0)
    time.sleep(0.05)
    self.buzzer.duty_u16(32768)

    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.d4)
    time.sleep(0.5)
    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.d4)
    time.sleep(0.5)


    self.buzzer.freq(self.f4sharp)
    time.sleep(0.6)

    self.buzzer.duty_u16(0)
    time.sleep(0.02)
    self.buzzer.duty_u16(32768)

    self.buzzer.freq(self.e4)
    time.sleep(0.25)
    self.buzzer.freq(self.d4)
    time.sleep(0.25)
    self.buzzer.freq(self.c4sharp)
    time.sleep(0.25)
    self.buzzer.freq(self.b3)
    time.sleep(0.25)
    self.buzzer.freq(self.a3sharp)
    time.sleep(0.25)

    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.d4)
    time.sleep(0.5)
    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.f3sharp)
    time.sleep(0.25)
    self.buzzer.freq(self.g3)
    time.sleep(0.25)

    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.d4)
    time.sleep(0.5)
    self.buzzer.freq(self.a3)
    time.sleep(1)

    self.buzzer.freq(self.d4)
    time.sleep(0.5)


    # self.buzzer.freq(self.d4)
    # time.sleep(0.35)

    self.buzzer.duty_u16(0)
    time.sleep(0.1)
    self.buzzer.duty_u16(32768)

    self.buzzer.freq(self.b3)
    time.sleep(0.25)
    self.buzzer.freq(self.a3)
    time.sleep(0.5)
    self.buzzer.freq(self.g3)
    time.sleep(0.5)

    self.buzzer.freq(self.f3sharp)
    time.sleep(0.5)
    self.buzzer.freq(self.e3)
    time.sleep(0.5)
    self.buzzer.freq(self.d3)
    time.sleep(0.5)
    self.buzzer.duty_u16(0)

#buzzer = Buzzer()
#buzzer.play_jeopardy_song()