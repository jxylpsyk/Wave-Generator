from numpy import array as nparray

from ..utils import messenger as mss

# Wave objects hold all wave-related info


class Wave:

    # constructor
    def __init__(self, audio_arr = None, fund_freq = 440):
        if audio_arr is None:
            audio_arr = []
        self.audio_arr = audio_arr
        self.freq = fund_freq

    # Call this to set a pre-defined audio array to the Wave object instead of creating one
    def set_audio(self, audio_arr):
        self.audio_arr = audio_arr

    def set_freq(self, freq):
        self.freq = freq

    # Call this to save the current wave
    def save_audio(self, wave_name) -> None:

        # since ndarray is not json serializable, the array is cast into a list
        mss.save_info(list(self.audio_arr), wave_name)

    # Call this when user selects a saved wave
    def load_audio(self, wave_name) -> None:

        # since array is stored as a list, when fetching, the data is cast to an ndarray
        self.audio_arr = nparray(mss.get_info(wave_name))
