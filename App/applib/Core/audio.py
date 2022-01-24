# Functions to play audio and create playable arrays

import numpy as np
import simpleaudio as sa

from .constants import SAMPLE_RATE


def normalize_audio(audio_arr):
    arr_copy = audio_arr
    # normalize to 16-bit range
    arr_copy *= 32767 / np.max(np.abs(arr_copy))  # highest value is in 16-bit range

    # convert to 16-bit data
    arr_copy = arr_copy.astype(np.int16)

    return arr_copy


# freq should be in hertz
def __make_audio(freq, time) -> np.ndarray:

    # time is note duration in seconds
    # Returns time * SAMPLE_RATE evenly spaced samples, calculated over the interval [0, T].
    t = np.linspace(0, time, int(SAMPLE_RATE * time), False)

    # generate sine wave notes
    # range(-1, 1)
    note = np.sin(freq * t * 2 * np.pi)  # freq in hertz
    return normalize_audio(note)


def play_note(freq, time) -> None:
    note = __make_audio(freq, time)

    play_obj = sa.play_buffer(note, 1, 2, SAMPLE_RATE)
    play_obj.wait_done()


def play_audio(audio_arr):
    play_obj = sa.play_buffer(normalize_audio(audio_arr), 1, 2, SAMPLE_RATE)
    play_obj.wait_done()
    return audio_arr


def play_chord(time, *args) -> None:
    note_list = [__make_audio(freq, time) for freq in args]

    for note in note_list:
        play_obj = sa.play_buffer(note, 1, 2, SAMPLE_RATE)

    play_obj.wait_done()