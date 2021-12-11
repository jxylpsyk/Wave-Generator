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


# freq should be in hertz
def make_audio(freq, time):
    # get timesteps for each sample, T is note duration in seconds
    SAMPLE_RATE = 44100

    # Returns T * SAMPLE_RATE evenly spaced samples, calculated over the interval [0, T].
    t = np.linspace(0, time, SAMPLE_RATE * time, False)

    # generate sine wave notes
    # range(-1, 1)
    note = np.sin(freq * t * 2 * np.pi)  # freq in hertz
    audio = note

    # concatenate notes
    # audio = np.hstack(
    #     (A_note, Csh_note, E_note))  # concatenates elements into list column wise

    # normalize to 16-bit range
    audio *= 32767 / np.max(np.abs(audio))
    # convert to 16-bit data
    audio = audio.astype(np.int16)

    return audio


audio = make_audio(440, 2)
# start playback
play_obj = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)

# wait for playback to finish before exiting
play_obj.wait_done()

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2**(4 / 12)
E_freq = A_freq * 2**(7 / 12)

# make an array 1 second long, cut of duplicate the elements according to the time given
