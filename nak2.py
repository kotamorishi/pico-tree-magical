import time
import board
from rainbowio import colorwheel
import neopixel
import random

pixel_pin = board.GP1
num_pixels = 9

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (180, 180, 180)
colors = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE] #, WHITE]


while True:
    pixels.fill(OFF)
    for _ in range(random.randint(2, num_pixels - 3)):
        pixels[random.randint(0, num_pixels - 1)] = colors[random.randint(0, len(colors) - 1)]
    pixels.show()
    time.sleep((random.randint(2, 10) * 100) / 1000)
