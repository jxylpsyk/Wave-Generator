# Functions to create the 4 waves of the apocalypse

import numpy as np
import math

from .constants import SAMPLE_RATE


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

    if not wave_type.isalpha():

        raise TypeError('First arguement should be of type str')

    base_arr = np.linspace(0, time, int(SAMPLE_RATE * time))

    if wave_type.lower() == 'sin':
        for index, i in enumerate(base_arr):
            base_arr[index] = math.sin(i * freq * 2 * math.pi)
        return base_arr

    elif wave_type.lower() == 'triangle':
        for index, i in enumerate(base_arr):
            base_arr[index] = __triangle(i * freq)
        return base_arr

    elif wave_type.lower() == 'sawtooth':
        for index, i in enumerate(base_arr):
            base_arr[index] = __sawtooth(i * freq)
        return base_arr

    elif wave_type.lower() == 'square':
        for index, i in enumerate(base_arr):
            base_arr[index] = __square(i * freq)
        return base_arr

    else:
        raise ValueError('No default wave called', wave_type,
                         '.\nChoose from sin, triangle, sawtooth and square')
