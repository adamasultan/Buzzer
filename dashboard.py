# from typing import List
from neopixel import NeoPixel
from time import sleep
from machine import Pin

class Dashboard:
  def __init__(self, leds, color, pixels):
    self.__leds=leds
    self.__pixels = pixels
    self.__color = color
    #self.reset()

  def add_leds(self, arr):
    self.__leds += arr
  def blank(self):
    self.__pixels.fill((0,0,0))
    self.__pixels.write()
    sleep(0.05)
    self.__pixels.write()
    
  def set_white(self):
    self.__pixels.fill((75,75,75))
    self.__pixels.write()
    sleep(0.05)
    self.__pixels.write()
  def win(self):
    print("win")
    rainbow = [
    (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
    (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
    (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
    (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10)]
    
    
    self.blank()
    for index in self.__leds:
        self.__pixels[index] = self.__color
    #self.__pixels.fill(self.__color)
    self.__pixels.write()
    sleep(0.05)
    self.__pixels.write()
    sleep(2)
    count = 30
    while count >0 :
      rainbow = rainbow[-1:] + rainbow[:-1]
      for index in self.__leds:
        self.__pixels[index] = rainbow[index]
      self.__pixels.write()
      sleep(0.1)
      count = count - 1

  def reset(self):
    self.set_white()
 

  


  def neotest(self):
    rainbow = [
    (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
    (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
    (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
    (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10)]

    count = 5
    while count >0 :
      rainbow = rainbow[-1:] + rainbow[:-1]
      print(rainbow)
      for i in range(16):
        print(rainbow[i])
        self.__pixels[i] = rainbow[i]
      self.__pixels.write()
      sleep(0.1)
      count = count - 1
      print(count)