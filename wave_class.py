from utils import messenger


class Wave:

    # constructor
    def __init__(self, audio_arr=[]):
        self.audio_arr = audio_arr

    def set_audio(self, audio_arr):
        self.audio_arr = audio_arr

    def save_audio(self, wave_name) -> None:
        messenger.save_wave(self.audio_arr, wave_name)

    def load_audio(self, wave_name) -> None:
        self.audio_arr = messenger.get_wave(wave_name)
