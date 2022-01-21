from typing import final
import App.applib.Core.constants as const
import random

from App.applib.Core.wave_class import Wave
from App.applib.Core.audio import play_note

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


def simple_perlin(target_l, num_elements):
    final_l = []
    random_index = random.randrange(0, len(target_l) - 1)
    final_l.append(target_l[random_index])

    for _ in range(num_elements):
        random_index += 1 if random.random() >= 0.5 else -1
        if random_index > len(target_l) - 1:
            random_index -= 1
        if random_index < 0:
            random_index += 1

        final_l.append(target_l[random_index])

    return final_l


def continuity_test():
    key_list = list(notes.keys())

    for key1 in simple_perlin(key_list, 55):
        play_note(notes[key1], 0.03)
        play_note(notes[key1], 0.02)


# continuity_test()

play_song()

# concatenate notes
# plays it one after the other
# audio = np.hstack(
#     (A_note, Csh_note, E_note))  # concatenates elements into list column wise