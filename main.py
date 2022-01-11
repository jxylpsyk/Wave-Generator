import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np

from App.applib.Core.wave_class import Wave
from App.applib.Core.constants import SAMPLE_RATE
from App.applib.Core.default_waves import make_default_wave
from App.applib.Core.audio import play_audio

# The main premise of the project is for the user to do manipulations on two sound waves
# Therefore, there are two waves for the user to play around with

# The two waves are set to A440 sine waves by default
# TODO: on startup, make the waves initialize to the last saved wave

user_wave1 = Wave(make_default_wave('sin', 440, 1))
user_wave2 = Wave(make_default_wave('sin', 440, 1))

#GUI
'''
colours pinkish red #ff8cad
mellow yellow #ffff8c
Pretty purple #c800ff
Bratty blue #2600ff
Plain Blanc #ffffff

!!!ALWAYS KEEP MIN ROW AS 1
'''


class blueButton:
    def __init__(self, wave_name, position_x, position_y, freq):
        self.position_x = position_x
        self.position_y = position_y

        self.button = tk.Button(
            root,
            width=12,
            height=2,
            text=wave_name.capitalize(),
            highlightbackground='#2610ff',
            foreground="#ffffff",
            command=lambda: play_audio(make_default_wave(wave_name, freq, 1)))

    def display_button(self):
        self.button.grid(column=self.position_x, row=self.position_y)


root = tk.Tk()
root.title("Wave Generator 0.6.9.420")

left_box = tk.Canvas(
    root, height=900, width=300, background="#ff8cad"
)  #,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
left_box.grid(columnspan=15, rowspan=100)

canvas = tk.Canvas(root, height=900, width=1200, background="#ffff8c")
canvas.grid(column=15, row=1, columnspan=100, rowspan=100)

tsxt1 = tk.Label(
    text="Wave Generatorrrrrr",
    height=0,
    background="#ff8cad",
)
tsxt1.grid(row=1)

txtbx1 = blueButton('sawtooth', 106, 2, 200)
txtbx1.display_button()

txtbx2 = blueButton('square', 110, 2, 200)
txtbx2.display_button()

txtbx3 = blueButton('sin', 104, 2, 200)
txtbx3.display_button()

txtbx4 = blueButton('triangle', 108, 2, 200)
txtbx4.display_button()

# v2 = tk.DoubleVar()

# def show2():

#     sel = "Vertical Scale Value = " + str(v2.get())
#     l2.config(text=sel, font=("Courier", 14))

# s2 = tk.Scale(root, variable=v2, from_=50, to=1, orient='vertical')

# l4 = tk.Label(root, text="Vertical Scaler")

# b2 = tk.Button(root,
#                text="Display Vertical",
#                command=show2,
#                bg="purple",
#                fg="white")

# l2 = tk.Label(root)

# s2.pack(anchor='center')
# l4.pack()
# b2.pack()
# l2.pack()

root.mainloop()