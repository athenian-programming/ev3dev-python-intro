#!/usr/bin/env python3

import time

from ev3dev.ev3 import Leds
from ev3dev.ev3 import Sound

Sound.speak("Flashing lights").wait()

Sound.speak("The long way").wait()

Leds.set_color(Leds.LEFT, Leds.GREEN)
Leds.set_color(Leds.RIGHT, Leds.RED)
time.sleep(.5)

Leds.set_color(Leds.LEFT, Leds.RED)
Leds.set_color(Leds.RIGHT, Leds.GREEN)
time.sleep(.5)

Leds.set_color(Leds.LEFT, Leds.GREEN)
Leds.set_color(Leds.RIGHT, Leds.RED)
time.sleep(.5)

Leds.set_color(Leds.LEFT, Leds.RED)
Leds.set_color(Leds.RIGHT, Leds.GREEN)
time.sleep(.5)

Sound.speak("The short way").wait()

for i in range(0, 4):
    Leds.set_color(Leds.LEFT, (Leds.GREEN, Leds.RED)[i % 2])
    Leds.set_color(Leds.RIGHT, (Leds.RED, Leds.GREEN)[i % 2])
    time.sleep(.5)

# Reset the lights to Green
Leds.set_color(Leds.LEFT, Leds.GREEN)
Leds.set_color(Leds.RIGHT, Leds.GREEN)
