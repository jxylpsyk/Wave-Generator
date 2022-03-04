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

    # Call this to save the current wave
    def save_audio(self, slider_list, wave_name) -> None:

        # since ndarray is not json serializable, the array is cast into a list
        mss.save_info(slider_list, wave_name)

    # Call this when user selects a saved wave
    def return_list(self, wave_name) -> None:

        # since array is stored as a list, when fetching, the data is cast to an ndarray
        # self.audio_arr = nparray(mss.get_info(wave_name))

        return mss.get_info(wave_name)

    def delete_list(self, wave_name):
        mss.del_info(wave_name)
