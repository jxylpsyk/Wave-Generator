# Import correct libraries
import numpy as np
import simpleaudio as sa

from lib.Core.wave_class import Wave
from lib.Core.octave_5 import OCTAVE_5_NOTES

# So the basic structure is to have a Wave object, on which all the computation/equations will be done.
# This is then passed to sa.play_buffer() as a sound which can then be heard.
# WE ARE DOING AS LESS LIBRARY-DEPENDENT COMPUTATION AS POSSIBLE. IMPERATIVE!!

SAMPLE_RATE = 44100

notes = OCTAVE_5_NOTES
print(notes)


# freq should be in hertz
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


def play_song():
    play_note(notes['Bb'] / 2, 0.1)
    play_note(notes['C'], 0.1)
    play_note(notes['Csh'], 0.1)
    play_note(notes['Bb'] / 2, 0.1)
    play_note(notes['F'], 0.4)
    play_note(notes['F'], 0.4)
    play_note(notes['Eb'], 0.5)

    play_note(notes['Ab'] / 2, 0.1)
    play_note(notes['Bb'] / 2, 0.1)
    play_note(notes['C'], 0.1)
    play_note(notes['Ab'] / 2, 0.1)
    play_note(notes['Eb'], 0.4)
    play_note(notes['Eb'], 0.4)
    play_note(notes['Csh'], 0.5)


play_song()

# concatenate notes
# plays it one after the other
# audio = np.hstack(
#     (A_note, Csh_note, E_note))  # concatenates elements into list column wise