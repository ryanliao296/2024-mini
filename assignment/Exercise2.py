#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

NOTE_B4 = 493.883
NOTE_E5 = 659.255
NOTE_G5 = 783.99
NOTE_FS5 = 739.989
NOTE_B5 = 987.77
NOTE_A5 = 880
NOTE_EF5 = 622.25
NOTE_F5 = 698.46


durations = [
    0.4, 0.8, 0.4, 0.4, 0.8, 0.4, 1.2, 1.2,   # Longer hold on the D5
    0.6, 0.4, 0.4, 0.8, 0.4, 1.2   # Adjust timing to match melody better
]
#duration: float = .6  # seconds

melody = [
    NOTE_B4, NOTE_E5, NOTE_G5, NOTE_FS5, NOTE_E5, NOTE_B5, NOTE_A5, NOTE_FS5,  # Opening part
    NOTE_E5, NOTE_G5, NOTE_FS5, NOTE_EF5, NOTE_F5, NOTE_B4,  # Continuing part
]

print("Playing frequency (Hz):")

for i in range(len(melody)):
    playtone(int(melody[i]), durations[i])

# Turn off the PWM
quiet()