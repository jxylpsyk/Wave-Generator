import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import math
import simpleaudio
from ..applib.Core.constants import SAMPLE_RATE
from ..applib.Core.default_waves import *
from ..applib.Core.audio import play_audio
#CODE FROM SISTER FILES IS STORED IN THE COMMENT BELLOW!!!


# Last updated on 22nd of December, Two Thousand Twenty One years after the birth of Christ


"""
wave_class.py 

# Wave objects hold all wave-related info

from utils import messenger as mss


class Wave:

    # constructor
    def __init__(self, audio_arr=[]):
        self.audio_arr = audio_arr

    # Call this to set a pre-defined audio array to the Wave object instead of creating one
    def set_audio(self, audio_arr):
        self.audio_arr = audio_arr

    # Call this to save the current wave
    def save_audio(self, wave_name) -> None:
        mss.save_info(self.audio_arr, wave_name)

    # Call this when user selects a saved wave
    def load_audio(self, wave_name) -> None:
        self.audio_arr = mss.get_info(wave_name)

"""


"""
wave_opperations.py 

from constants import SAMPLE_RATE


def avg_wave(audio_arr1, audio_arr2):
    return (audio_arr1 + audio_arr2) / 2

"""
'''
audio.py


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


def play_audio(audio_arr):
    # normalize to 16-bit range
    audio_arr *= 32767 / np.max(
        np.abs(audio_arr))  # highest value is in 16-bit range

    # convert to 16-bit data
    audio_arr = audio_arr.astype(np.int16)

    play_obj = sa.play_buffer(audio_arr, 1, 2, SAMPLE_RATE)
    play_obj.wait_done()


def play_chord(time, *args) -> None:
    note_list = [make_audio(freq, time) for freq in args]

    for note in note_list:
        play_obj = sa.play_buffer(note, 1, 2, SAMPLE_RATE)

    play_obj.wait_done()
'''
'''
Constants
'''
'''
SAMPLE_RATE = 44100

OCTAVE_5_NOTES = {
    'C': 440 * 2**(3 / 12),
    'Csh': 440 * 2**(4 / 12),
    'Db': 440 * 2**(4 / 12),
    'D': 440 * 2**(5 / 12),
    'Dsh': 440 * 2**(6 / 12),
    'Eb': 440 * 2**(6 / 12),
    'E': 440 * 2**(7 / 12),
    'F': 440 * 2**(8 / 12),
    'Fsh': 440 * 2**(9 / 12),
    'Gb': 440 * 2**(9 / 12),
    'G': 440 * 2**(10 / 12),
    'Gsh': 440 * 2**(11 / 12),
    'Ab': 440 * 2**(11 / 12),
    'A': 440 * 2,
    'Ash': 440 * 2**(13 / 12),
    'Bb': 440 * 2**(13 / 12),
    'B': 440 * 2**(14 / 12),
}
'''
'''
 Default wave functions   
'''
'''
# Functions to create the 4 waves of the apocalypse



# region Math functions

def __cot(val):
    return (1 / math.tan(val))


def __sign(num):
    return -1 if num < 0 else 1


# endregion


# region Wave functions

def __triangle(x):
    return (2 / math.pi * math.asin(math.sin(2 * math.pi * x)))


def __sawtooth(x):
    return (-2 / math.pi * math.atan(__cot(math.pi * x)))


def __square(x):
    return (__sign(math.sin(2 * math.pi * x)))


# endregion


def make_default_wave(wave_type, freq, time):

    if wave_type.isalpha():

        base_arr = np.linspace(0, time, int(SAMPLE_RATE * time))

        if wave_type.lower() == 'sin':
            return [math.sin(i * freq * 2 * math.pi) for i in base_arr]

        elif wave_type.lower() == 'triangle':
            return [__triangle(i * freq) for i in base_arr]

        elif wave_type.lower() == 'sawtooth':
            return [__sawtooth(i * freq) for i in base_arr]

        elif wave_type.lower() == 'square':
            return [__square(i * freq) for i in base_arr]

        else:
            raise ValueError(
                'No default wave called', wave_type,
                '.\nChoose from sin, triangle, sawtooth and square')
    else:
        raise TypeError('First arguement should be of type str')
 
make_default_wave('sin',)
'''
times = 1

#GUI
'''
colours pinkish red #ff8cad
mellow yellow #ffff8c
Pretty purple #c800ff
Bratty blue #2600ff
Plain Blanc #ffffff
!!!ALWAYS KEEP MIN ROW AS 1
'''


def a1():
    print('hello world')


root = tk.Tk()
root.title("Wave Generator 4.0.0.734")
canvas = tk.Canvas(
    root, height=900, width=300, background="#ff8cad"
)  #,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
canvas.grid(columnspan=15, rowspan=100)
box = tk.Canvas(root, height=900, width=1200, background="#ffff8c")
box.grid(column=15, row=1, columnspan=100, rowspan=100)

tsxt1 = tk.Label(
    text="Wave Generator",
    height=0,
    background="#ff8cad",
)
tsxt1.grid(row=1)

txtbx1 = tk.Button(
    root,
    width=12,
    height=2,
    text="Square",
    background='#2600ff',
    foreground="#ffffff",
    command=lambda: play_audio(make_default_wave('square', 200, 1)))
txtbx1.grid(column=1, row=32)

txtbx1 = tk.Button(
    root,
    width=12,
    height=2,
    text="SawTooth",
    background='#2600ff',
    foreground="#ffffff",
    command=lambda: play_audio(make_default_wave('sawtooth', 200, 1)))
txtbx1.grid(column=9, row=32)

txtbx1 = tk.Button(
    root,
    width=12,
    height=2,
    text="Triangle",
    background='#c800ff',
    foreground="#ffffff",
    command=lambda: play_audio(make_default_wave('triangle', 200, 1)))
txtbx1.grid(column=100, row=1)

txtbx1 = tk.Button(
    root,
    width=12,
    height=2,
    text="Sine",
    background='#c800ff',
    foreground="#ffffff",
    command=lambda: play_audio(make_default_wave('sin', 200, 1)))
txtbx1.grid(column=9, row=35)

v2 = tk.DoubleVar()
  
def show2():
      
    sel = "Vertical Scale Value = " + str(v2.get()) 
    l2.config(text = sel, font =("Courier", 14))
  
s2 = tk.Scale( root, variable = v2,
           from_ = 50, to = 1,
           orient = 'VERTICAL') 
  
l4 = tk.Label(root, text = "Vertical Scaler")
  
b2 = tk.Button(root, text ="Display Vertical",
            command = show2,
            bg = "purple", 
            fg = "white")
  
l2 = tk.Label(root)
  
s2.pack(anchor = 'CENTER') 
l4.pack()
b2.pack()
l2.pack()

root.mainloop()