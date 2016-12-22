#!/usr/bin/env python3

from ev3dev.ev3 import Sound

s = Sound.speak("This is a test of the sound system")
s.wait()

Sound.speak("All the numbers from 0 to 5").wait()
for i in range(0, 6):
    val = "Number {0}".format(i)
    Sound.speak(val).wait()

Sound.speak("Just the even numbers").wait()
for i in range(0, 6):
    if i % 2 == 0:
        Sound.speak(val="Number {0}".format(i)).wait()

Sound.speak("Just the odd numbers").wait()
for i in range(0, 6):
    if i % 2 == 1:
        Sound.speak("Number {0}".format(i)).wait()
