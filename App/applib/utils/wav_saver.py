import wave
from tkinter import filedialog

from ..Core import constants
from ..Core import audio

def save_as_wav(user_arr):
    file = filedialog.asksaveasfilename(title="Save", filetypes=(("audio file", "*.wav"), ("all files", "*.*")), defaultextension=".wav")

    # TODO: label error msg saying 'please enter a valid name'
    if file is None:
        return

    wave_file = wave.open(file, 'wb')
    wave_file.setnchannels(constants.CHANNELS)
    wave_file.setsampwidth(constants.FORMAT)
    wave_file.setframerate(constants.SAMPLE_RATE)
    wave_file.writeframes(audio.normalize_audio(user_arr))
    wave_file.close()
