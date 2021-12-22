# Functions to play audio and create playable arrays

import numpy as np
import simpleaudio as sa

from constants import SAMPLE_RATE


# freq should be in hertz
# might need to make this private
def make_audio(freq, time) -> np.ndarray:

    # time is note duration in seconds
    # Returns time * SAMPLE_RATE evenly spaced samples, calculated over the interval [0, T].
    t = np.linspace(0, time, int(SAMPLE_RATE * time), False)

    # generate sine wave notes
    # range(-1, 1)
    note = np.sin(freq * t * 2 * np.pi)  # freq in hertz
    audio = note

    # normalize to 16-bit range
    audio *= 32767 / np.max(np.abs(audio))  # highest value is in 16-bit range

    # convert to 16-bit data
    audio = audio.astype(np.int16)

    return audio


def play_note(freq, time) -> None:
    note = make_audio(freq, time)

    play_obj = sa.play_buffer(note, 1, 2, SAMPLE_RATE)
    play_obj.wait_done()


def play_chord(time, *args) -> None:
    note_list = [make_audio(freq, time) for freq in args]

    for note in note_list:
        play_obj = sa.play_buffer(note, 1, 2, SAMPLE_RATE)

    play_obj.wait_done()