# Import correct libraries
import numpy as np
import simpleaudio as sa

# The Wave class is going to have all aspects of wave like frequency, amplitude, wave type and equation of wave
# This can be modified according to how external libraries work

from wave_class import Wave

# So the basic structure is to have a Wave object, on which all the computation/equations will be done.
# This is then passed to sa.play_buffer() as a sound which can then be heard.
# WE ARE DOING AS LESS LIBRARY-DEPENDENT COMPUTATION AS POSSIBLE. IMPERATIVE!!
'''
https://simpleaudio.readthedocs.io/en/latest/tutorial.html#playing-audio-directly
'''

SAMPLE_RATE = 44100

notes = {
    '5C': 440 * 2**(3 / 12),
    '5Csh': 440 * 2**(4 / 12),
    '5Db': 440 * 2**(4 / 12),
    '5D': 440 * 2**(5 / 12),
    '5Dsh': 440 * 2**(6 / 12),
    '5Eb': 440 * 2**(6 / 12),
    '5E': 440 * 2**(7 / 12),
    '5F': 440 * 2**(8 / 12),
    '5Fsh': 440 * 2**(9 / 12),
    '5Gb': 440 * 2**(9 / 12),
    '5G': 440 * 2**(10 / 12),
    '5Gsh': 440 * 2**(11 / 12),
    '5Ab': 440 * 2**(11 / 12),
    '5A': 440 * 2,
    '5Ash': 440 * 2**(13 / 12),
    '5Bb': 440 * 2**(13 / 12),
    '5B': 440 * 2**(14 / 12),
}


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
    play_note(notes['5Bb'] / 2, 0.1)
    play_note(notes['5C'], 0.1)
    play_note(notes['5Csh'], 0.1)
    play_note(notes['5Bb'] / 2, 0.1)
    play_note(notes['5F'], 0.4)
    play_note(notes['5F'], 0.4)
    play_note(notes['5Eb'], 0.5)

    play_note(notes['5Ab'] / 2, 0.1)
    play_note(notes['5Bb'] / 2, 0.1)
    play_note(notes['5C'], 0.1)
    play_note(notes['5Ab'] / 2, 0.1)
    play_note(notes['5Eb'], 0.4)
    play_note(notes['5Eb'], 0.4)
    play_note(notes['5Csh'], 0.5)


# play_chord(1, notes['5A'], notes['5A']/2, notes['5Csh'] / 2, notes['5E'] / 2)

# play_note(440 * 2**(-1 / 12), 1)

play_song()

# concatenate notes
# plays it one after the other
# audio = np.hstack(
#     (A_note, Csh_note, E_note))  # concatenates elements into list column wise