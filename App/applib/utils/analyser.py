# Used by grapher to calculate the frequency of the entered array

import numpy as np

from ..Core import constants

class AudioDetector:
    def __init__(self):
        self.most_probable_frequency = 0
    

    def find_highest_probable_frequency(self, noisy_array) -> int:
        array_length = len(noisy_array)

        f_hat = np.fft.fft(noisy_array, constants.SAMPLE_RATE)

        PSD = (f_hat * np.conj(f_hat)) / array_length
        PSD = np.real(PSD)
        PSD = PSD[:array_length // 2]

        self.most_probable_frequency = np.argmax(PSD)

        return self.most_probable_frequency