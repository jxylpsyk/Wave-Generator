import tkinter as tk
from PIL import Image, ImageTk  #, ImageDraw

from App.applib.Core.wave_class import Wave
from App.applib.Core.constants import *
from App.applib.Core.default_waves import make_default_wave
from App.applib.Core.audio import play_audio
from App.applib.Core.Detective import *

# The main premise of the project is for the user to do manipulations on two sound waves
# Therefore, there are two waves for the user to play around with

# DETECT OS is done in constants.py
# The two waves are set to A440 sine waves by default
# TODO: on startup, make the waves initialize to the last saved wave

user_wave1 = Wave(make_default_wave('sin', 440, 1))
user_wave2 = Wave(make_default_wave('sin', 440, 1))
focus_wave = user_wave1  #YOLO
#Detected Frequency

#GUI
root = tk.Tk()
root.title("Wave Generator 0.6.9.420")
left_box = tk.Canvas(
    root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, background="#ff8cad"
)  # ,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
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


class image:
    def importImage(relPth, x_codds, y_codds):
        graph = Image.open(relPth)
        graph = ImageTk.PhotoImage(graph)
        graph_label = tk.label(image=graph)
        graph_label.image = graph
        graph_label.grid(column=x_codds, row=y_codds)


# class sliders:
# to be continued (P.S spelling error)


class textBox:
    def __init__(self, pos_x, pos_y, wdth):
        # karma
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

        self.textbox.place(x=self.pos_x, y=self.pos_y)

    def return_text(self):
        return self.textbox.get(1.0, "end-1c")


class blueWaveButton:
    # style = ttk.style()
    # style.configure('BW.TButton', foreground = '#ffffff', background = '#2610ff')
    def __init__(self, wave_name, position_x, position_y, freq):
        self.position_x = position_x
        self.position_y = position_y

        self.button = tk.Button(
            root,
            width=BUTTON_WIDTH,
            height=2,
            text=wave_name.capitalize(),
            highlightbackground='#2610ff',
            background='#2610ff',
            foreground="#ffffff",
            command=lambda: play_audio(make_default_wave(wave_name, freq, 1)))

        self.button.place(x=self.position_x, y=self.position_y)


class blueButton:
    # style = ttk.style()
    # style.configure('BW.TButton', foreground = '#ffffff', background = '#2610ff')
    def __init__(self, name, position_x, position_y, lambda_func):
        self.position_x = position_x
        self.position_y = position_y

        self.button = tk.Button(root,
                                width=BUTTON_WIDTH,
                                height=2,
                                text=name.capitalize(),
                                highlightbackground='#2610ff',
                                background='#2610ff',
                                foreground="#ffffff",
                                command=lambda_func)

        self.button.place(x=self.position_x, y=self.position_y)


class FreqDetectButtons:
    def __init__(self, name, pos_x, pos_y, lambda_func):
        self.pos_y = pos_y
        self.pos_x = pos_x

        self.button = tk.Button(root,
                                width=BUTTON_WIDTH,
                                height=2,
                                text=name.capitalize(),
                                highlightbackground='#004d00',
                                background='#004d00',
                                foreground='#ffffff',
                                command=lambda_func)
        self.button.place(x=self.pos_x, y=self.pos_y)


if SYSTEM_OS == "Darwin":
    '''!!!OsX!!!'''

    txtinp = textBox(WINDOW_WIDTH - 580, 130, 50)

    saveBx1 = blueButton(
        'Save', WINDOW_WIDTH - 160, 130,
        lambda: focus_wave.save_audio(txtinp.return_text())
        if txtinp.return_text() != '' else 0)

    txtbx1 = blueWaveButton('sawtooth', WINDOW_WIDTH - 580, 50, 200)

    txtbx2 = blueWaveButton('square', WINDOW_WIDTH - 440, 50, 200)

    txtbx3 = blueWaveButton('sin', WINDOW_WIDTH - 300, 50, 200)

    txtbx4 = blueWaveButton('triangle', WINDOW_WIDTH - 160, 50, 200)

    frqbx1 = FreqDetectButtons('Frequency Detector', WINDOW_WIDTH - 580, 200,
                               lambda: print(12345))

elif SYSTEM_OS == "Linux":
    '''!!!LINUX!!!'''

    txtinp = textBox(WINDOW_WIDTH - 580, 350, 50)

    saveBx1 = blueButton('Save', WINDOW_WIDTH - 160, 350,
                         lambda: print(txtinp.return_text()))

    txtbx1 = blueWaveButton('sawtooth', WINDOW_WIDTH - 580, 50, 200)

    txtbx2 = blueWaveButton('square', WINDOW_WIDTH - 440, 50, 200)

    txtbx3 = blueWaveButton('sin', WINDOW_WIDTH - 300, 50, 200)

    txtbx4 = blueWaveButton('triangle', WINDOW_WIDTH - 160, 50, 200)

    frqbx1 = FreqDetectButtons('Frequency Detector 50000', 580, 200,
                               print(12345))

elif SYSTEM_OS == "Windows":
    txtinp = textBox(WINDOW_WIDTH - 650, 143, 49)

    saveBx1 = blueButton(
        'Save', WINDOW_WIDTH - 200, 140,
        lambda: focus_wave.save_audio(txtinp.return_text())
        if txtinp.return_text() != '' else 0)

    txtbx1 = blueWaveButton('sawtooth', WINDOW_WIDTH - 650, 50, 200)

    txtbx2 = blueWaveButton('square', WINDOW_WIDTH - 500, 50, 200)

    txtbx3 = blueWaveButton('sin', WINDOW_WIDTH - 350, 50, 200)

    txtbx4 = blueWaveButton('triangle', WINDOW_WIDTH - 200, 50, 200)

    frqbx1 = FreqDetectButtons('Frequency Detector 50000', WINDOW_WIDTH - 650, 250,
                               print(12345))
    lambe = tk.Label(foreground='#ffffff',highlightbackground='#004d00',
                     background='#004d00',text= DetectedFrequency)


else:
    print('Please use a valid Opperating system [Windows,MacOS,Linux]')

root.mainloop()

# region Testing GUI ig

# tsxt1 = tk.Label(
#     text="Wave Generatorrrrrr",
#     height=0,
#     background="#ff8cad",
# )
# txt1s.grid(row=1)

# =============================================================================

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
# endregion