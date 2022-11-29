# this code is based
#
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
import random

pixel_pin = board.GP1
num_pixels = 9

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

low = 3
high = 50

#index
r = 0
g = 1
b = 2

# init color array for 9 pixels
color = [[10,10,10],[10,10,10],[10,10,10],[10,10,10],[10,10,10],[10,10,10],[10,10,10],[10,10,10],[10,10,10]]
step  = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]] 


while True:
    pixIdx = random.randint(0, num_pixels - 1)
    
    for i in range(3):
        color[pixIdx][i] = color[pixIdx][i] + step[pixIdx][i]
        if color[pixIdx][i] > high:
            step[pixIdx][i] = -1
        if color[pixIdx][i] < low:
            step[pixIdx][i] = random.randint(1, 3)
            
    #for i in range(num_pixels):
    #    pixels[i] = (color[i][r], color[i][g], color[i][b])
    pixels[pixIdx] = (color[pixIdx][r], color[pixIdx][g], color[pixIdx][b])
    pixels.show()
    time.sleep(0.01)

    

    


