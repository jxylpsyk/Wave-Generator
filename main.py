import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np

from App.applib.Core.wave_class import Wave
from App.applib.Core.constants import *
from App.applib.Core.default_waves import make_default_wave
from App.applib.Core.audio import play_audio

# The main premise of the project is for the user to do manipulations on two sound waves
# Therefore, there are two waves for the user to play around with

# The two waves are set to A440 sine waves by default
# TODO: on startup, make the waves initialize to the last saved wave

user_wave1 = Wave(make_default_wave('sin', 440, 1))
user_wave2 = Wave(make_default_wave('sin', 440, 1))

#GUI

root = tk.Tk()
root.title("Wave Generator 0.6.9.420")
left_box = tk.Canvas(
    root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, background="#ff8cad"
)  #,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
left_box.grid(columnspan=WINDOW_WIDTH, rowspan=WINDOW_HEIGHT)

# canvas = tk.Canvas(root, height=900, width=1200, background="#ffff8c")
# canvas.grid(column=15, row=1, columnspan=100, rowspan=100)
'''
colours pinkish red #ff8cad
mellow yellow #ffff8c
Pretty purple #c800ff
Bratty blue #2600ff
Plain Blanc #ffffff

!!!ALWAYS KEEP MIN ROW AS 1
'''
"""
class coordinatesConversion:
    def __init__(self ,x_codds,y_codds):
        
        self.x1 = x_codds * 15
        self.y1 = y_codds * 9
DUDE i dont think it is possible as it doesnt seem to be working, i checked the web and the only input options are in terms of column and row and the width is defined in terms of pixels 
so yea... maybe another method can work.      
"""


class image:
    def importImage(self, relPth, x_codds, y_codds):
        graph = Image.open(relPth)
        graph = ImageTk.PhotoImage(graph)
        graph_label = tk.label(image=graph)
        graph_label.image = graph
        graph_label.grid(column=x_codds, row=y_codds)


#class sliders:
#to be continued (P.S spelling error)


class textBoxs:
    def __init__(self, pos_x, pos_y, wdth):
        #karma
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.clspn = wdth
        self.textbox = tk.Text(
            root,
            width=wdth,
            height=2,
            background='#000000',
            foreground='#FFFFFF',
        )

    def display_textbox(self):
        self.textbox.place(x=self.pos_x, y=self.pos_y)


class blueWaveButton:
    def __init__(self, wave_name, position_x, position_y, freq):
        self.position_x = position_x
        self.position_y = position_y

        self.button = tk.Button(
            root,
            width=12,
            height=2,
            text=wave_name.capitalize(),
            highlightbackground='#2610ff',
            background='#2610ff',
            foreground="#ffffff",
            command=lambda: play_audio(make_default_wave(wave_name, freq, 1)))

    def display_button(self):
        self.button.place(x=self.position_x, y=self.position_y)


class blueButton:
    def __init__(self, name, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

        self.button = tk.Button(root,
                                width=12,
                                height=2,
                                text=name.capitalize(),
                                highlightbackground='#2610ff',
                                background='#2610ff',
                                foreground="#ffffff")
        #command=lambda: play_audio(make_default_wave(wave_name, freq, 1))

    def display_button(self):
        self.button.place(x=self.position_x, y=self.position_y)


# tsxt1 = tk.Label(
#     text="Wave Generatorrrrrr",
#     height=0,
#     background="#ff8cad",
# )
#txt1s.grid(row=1)

txtinp = textBoxs(WINDOW_WIDTH - 600, 425, 50)
txtinp.display_textbox()

saveBx1 = blueButton('Save', WINDOW_WIDTH - 200, 425)
saveBx1.display_button()

txtbx1 = blueWaveButton('sawtooth', WINDOW_WIDTH - 600, 50, 200)
txtbx1.display_button()

txtbx2 = blueWaveButton('square', WINDOW_WIDTH - 500, 50, 200)
txtbx2.display_button()

txtbx3 = blueWaveButton('sin', WINDOW_WIDTH - 300, 50, 200)
txtbx3.display_button()

txtbx4 = blueWaveButton('triangle', WINDOW_WIDTH - 200, 50, 200)
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