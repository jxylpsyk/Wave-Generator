# Functions to create the 4 waves of the apocalypse

import numpy as np
import math

from constants import SAMPLE_RATE


# region Math functions
def __cot(val):
    if val == 0: return 0
    return (1 / math.tan(val))


def __sign(num):
    return -1 if num < 0 else 1


# endregion


# region Wave functions
def __triangle(x):
    return (2 / math.pi * math.asin(math.sin(2 * math.pi * x)))


def __sawtooth(x):
    return (-2 / math.pi * math.atan(__cot(math.pi * x)))


def __square(x):
    return (__sign(math.sin(2 * math.pi * x)))


# endregion


def make_default_wave(wave_type, freq, time):

    if wave_type.isalpha():

        base_arr = np.linspace(0, time, int(SAMPLE_RATE * time))

        if wave_type.lower() == 'sin':
            return [math.sin(i * freq * 2 * math.pi) for i in base_arr]

        elif wave_type.lower() == 'triangle':
            return [__triangle(i * freq) for i in base_arr]

        elif wave_type.lower() == 'sawtooth':
            return [__sawtooth(i * freq) for i in base_arr]

        elif wave_type.lower() == 'square':
            return [__square(i * freq) for i in base_arr]

        else:
            raise ValueError(
                'No default wave called', wave_type,
                '.\nChoose from sin, triangle, sawtooth and square')
    else:
        raise TypeError('First arguement should be of type str')


wave_type = "sin"    
make_default_wave(wave_type,1000,100)