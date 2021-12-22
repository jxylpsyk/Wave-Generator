import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import math
import simpleaudio
from ..applib.Core.constants import SAMPLE_RATE
from ..applib.Core.default_waves import *
from ..applib.Core.audio import play_audio
#CODE FROM SISTER FILES IS STORED IN THE COMMENT BELLOW!!!
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
txtbx1.grid(column=1, row=35)

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