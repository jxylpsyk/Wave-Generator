from utils import messenger


class Wave:

    # constructor
    def __init__(self, audio_arr=[]):
        self.audio_arr = audio_arr

    # Call this to set a pre-defined audio array to the Wave object instead of creating one
    def set_audio(self, audio_arr):
        self.audio_arr = audio_arr

    # Call this to save the current wave
    def save_audio(self, wave_name) -> None:
        messenger.save_info(self.audio_arr, wave_name)

    # Call this when user selects a saved wave
    def load_audio(self, wave_name) -> None:
        self.audio_arr = messenger.get_info(wave_name)
