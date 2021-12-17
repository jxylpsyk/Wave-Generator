import applib.Core.constants as const

from applib.Core.wave_class import Wave
from applib.Core.audio import *

# The basic structure is to have a Wave object, on which all the computation/equations will be done.
# This is then passed to sa.play_buffer() as a sound which can then be heard.
# WE ARE DOING AS LESS LIBRARY-DEPENDENT COMPUTATION AS POSSIBLE. IMPERATIVE!!

notes = const.OCTAVE_5_NOTES


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