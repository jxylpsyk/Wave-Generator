# Import correct libraries
import simpleaudio as sa

# The Wave class is going to have all aspects of wave like frequency, amplitude, wave type and equation of wave
# This can be modified according to how external libraries work

from wave_class import Wave

# So the basic structure is to have a Wave object, on which all the computation/equations will be done.
# This is then passed to sa.play_buffer() as a sound which can then be heard.
# WE ARE DOING AS LESS LIBRARY-DEPENDENT COMPUTATION AS POSSIBLE. IMPERATIVE!!
'''
idk examine later
https://simpleaudio.readthedocs.io/en/latest/tutorial.html#playing-audio-directly

import numpy as np
import simpleaudio as sa

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.25
t = np.linspace(0, T, T * sample_rate, False)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)

# concatenate notes
audio = np.hstack((A_note, Csh_note, E_note))
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()
'''
