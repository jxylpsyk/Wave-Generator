import tkinter as tk
from PIL import Image, ImageTk

from App.applib.Core.wave_class import Wave
from App.applib.Core.constants import *
from App.applib.Core.default_waves import make_default_wave
from App.applib.Core.audio import play_audio
from App.utils import Grapher, messenger

# The main premise of the project is for the user to do manipulations on two sound waves
# Therefore, there are two waves for the user to play around with

# DETECT OS is done in constants.py
# The two waves are set to A440 sine waves by default

user_wave1 = Wave(make_default_wave('sin', 440, 1))
user_wave2 = Wave(make_default_wave('sin', 440, 1))

focus_wave = user_wave1

#GUI
root = tk.Tk()
root.title("Wave Generator 0.6.9.420")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

canvas = tk.Canvas(
    root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, background="#ff8cad"
)  # ,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")

# canvas.grid(columnspan=WINDOW_WIDTH, rowspan=WINDOW_HEIGHT)
canvas.place(height=WINDOW_HEIGHT, width=WINDOW_WIDTH)


# region Classes

class image:
    def importImage(relPth, x_codds, y_codds):
        graph = Image.open(relPth)
        graph = ImageTk.PhotoImage(graph)
        graph_label = tk.label(image=graph)
        graph_label.image = graph
        graph_label.grid(column=x_codds, row=y_codds)


class GraphSelectionUtility3000:

    def __init__(self, pos_x , pos_y , grph_img):
        self.pos_x = pos_x
        self.pos_y = pos_y
        def WhenPressed():
            for i in ListA:
                Labela = tk.Label(root,Text=ListA[i])
        self.Buton = tk.Button(root,Text="click Me", command=lambda: WhenPressed(),width=BUTTON_WIDTH, height=2)
        self.poss_ = self.pos_y +20
        self.Labela.place(x=self.pos_x, y=self.poss_)
        self.Buton.place(x = self.pos_x, y = self.pos_y)

class DropDown():
    def __init__(self, pos_x, pos_y) -> None:
        self.drop_state = False
        self.user_wave_names = messenger.get_user_waves()

        self.selected_wave = ""

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.root_frame = tk.Frame(root)
        self.text_frame = tk.Frame(self.root_frame)
        self.text_frame.pack(side='top')

        self.photo = tk.PhotoImage(file='App/GUI/Media/arrow.png')

        self.dd_button = tk.Button(self.text_frame, image=self.photo, compound='center', borderwidth=0, command= lambda: self.__toggle_list())
        self.dd_button.pack(side='right')

        self.t_label = tk.Label(self.text_frame, text=self.user_wave_names[0], width=20)
        self.t_label.pack(side='left', fill='both')

        self.root_frame.place(x=pos_x, y=pos_y)

    def get_user_wave_name(self):
        return self.selected_wave

    def __toggle_list(self):
        self.drop_state = not self.drop_state

        if self.drop_state:
            self.__create_list()
        else:
            self.__destroy_list()

    
    def __destroy_list(self):
        for button in self.list_frame.winfo_children():
            button.pack_forget()
        
        self.list_frame.place_forget()


    def __create_list(self):
        if self.user_wave_names is not None:

            def __normalize_length(wave_list):
                new_wave_list = []
                for wave in wave_list:
                    if len(wave) < 19:
                        new_wave_list.append(wave + " "* (19 - len(wave)))
                    else:
                        new_wave_list.append(wave[:19])
                
                return new_wave_list
            

            
            self.list_frame = tk.Frame(root)

            def __change_label(wave_name):
                self.selected_wave = wave_name.strip()
                self.t_label['text'] = self.selected_wave
                self.__destroy_list()
                self.drop_state = not self.drop_state

            unindent_x =  self.dd_button.winfo_x() + self.pos_x - 179
            unindent_y =  self.dd_button.winfo_y() + self.pos_y + 24
            for i, wave in enumerate(__normalize_length(self.user_wave_names)):
                tk.Button(self.list_frame, width=19, text=wave, compound='top', borderwidth=0, command = lambda w_name=wave : __change_label(w_name)).pack()

            self.list_frame.place(x=unindent_x, y=unindent_y)
    
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


class Vertical_Slider:
    def __init__(self, pos_x, pos_y, Range_Start, Range_End):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.Slide = tk.Scale(root, from_=Range_Start, to=Range_End, length = 220)

        self.Slide.place(x=self.pos_x, y=self.pos_y)

class HarmonicsLabel:
    def __init__(self, num, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.num = num

        self.label = tk.Label(text= f"H{self.num} ", width=5, anchor='center')
        self.label.place(x=pos_x, y=pos_y)


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


def slydey():
    Vslide1 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*0) ,WINDOW_HEIGHT - 270, 200, 0)
    Vslide2 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*1) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide3 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*2) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide4 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*3) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide5 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*4) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide6 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*5) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide7 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*6) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide8 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*7) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide9 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*8) , WINDOW_HEIGHT - 270, 200, 0)
    Vslide10 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*9), WINDOW_HEIGHT - 270, 200, 0)
    Vslide11 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*10), WINDOW_HEIGHT - 270, 200, 0)
    Vslide12 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*11), WINDOW_HEIGHT - 270, 200, 0)
    Vslide13 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*12), WINDOW_HEIGHT - 270, 200, 0)
    Vslide14 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*13), WINDOW_HEIGHT - 270, 200, 0)
    Vslide15 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*14), WINDOW_HEIGHT - 270, 200, 0)
    Vslide16 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*15), WINDOW_HEIGHT - 270, 200, 0)
    Vslide17 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*16), WINDOW_HEIGHT - 270, 200, 0)
    Vslide18 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*17), WINDOW_HEIGHT - 270, 200, 0)
    Vslide19 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*18), WINDOW_HEIGHT - 270, 200, 0)
    Vslide20 = Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*19), WINDOW_HEIGHT - 270, 200, 0)

def lables():
    HarmonicsLabels1  = HarmonicsLabel( 20, WINDOW_WIDTH - 120 - (MyNewCuteConstant*0) , WINDOW_HEIGHT - 300)
    HarmonicsLabels2  = HarmonicsLabel( 19, WINDOW_WIDTH - 120 - (MyNewCuteConstant*1) , WINDOW_HEIGHT - 300)
    HarmonicsLabels3  = HarmonicsLabel( 18, WINDOW_WIDTH - 120 - (MyNewCuteConstant*2) , WINDOW_HEIGHT - 300)
    HarmonicsLabels4  = HarmonicsLabel( 17, WINDOW_WIDTH - 120 - (MyNewCuteConstant*3) , WINDOW_HEIGHT - 300)
    HarmonicsLabels5  = HarmonicsLabel( 16, WINDOW_WIDTH - 120 - (MyNewCuteConstant*4) , WINDOW_HEIGHT - 300)
    HarmonicsLabels6  = HarmonicsLabel( 15, WINDOW_WIDTH - 120 - (MyNewCuteConstant*5) , WINDOW_HEIGHT - 300)
    HarmonicsLabels7  = HarmonicsLabel( 14, WINDOW_WIDTH - 120 - (MyNewCuteConstant*6) , WINDOW_HEIGHT - 300)
    HarmonicsLabels8  = HarmonicsLabel( 13, WINDOW_WIDTH - 120 - (MyNewCuteConstant*7) , WINDOW_HEIGHT - 300)
    HarmonicsLabels9  = HarmonicsLabel( 12, WINDOW_WIDTH - 120 - (MyNewCuteConstant*8) , WINDOW_HEIGHT - 300)
    HarmonicsLabels10 = HarmonicsLabel( 11, WINDOW_WIDTH - 120 - (MyNewCuteConstant*9),  WINDOW_HEIGHT - 300)
    HarmonicsLabels11 = HarmonicsLabel( 10, WINDOW_WIDTH - 120 - (MyNewCuteConstant*10), WINDOW_HEIGHT - 300)
    HarmonicsLabels12 = HarmonicsLabel( 9,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*11), WINDOW_HEIGHT - 300)
    HarmonicsLabels13 = HarmonicsLabel( 8,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*12), WINDOW_HEIGHT - 300)
    HarmonicsLabels14 = HarmonicsLabel( 7,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*13), WINDOW_HEIGHT - 300)
    HarmonicsLabels15 = HarmonicsLabel( 6,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*14), WINDOW_HEIGHT - 300)
    HarmonicsLabels16 = HarmonicsLabel( 5,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*15), WINDOW_HEIGHT - 300)
    HarmonicsLabels17 = HarmonicsLabel( 4,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*16), WINDOW_HEIGHT - 300)
    HarmonicsLabels18 = HarmonicsLabel( 3,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*17), WINDOW_HEIGHT - 300)
    HarmonicsLabels19 = HarmonicsLabel( 2,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*18), WINDOW_HEIGHT - 300)
    HarmonicsLabels20 = HarmonicsLabel( 1,  WINDOW_WIDTH - 120 - (MyNewCuteConstant*19), WINDOW_HEIGHT - 300)
# endregion

if SYSTEM_OS == "Darwin":
    '''!!!OsX!!!'''

    txtinp = textBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 50)

    saveBx1 = blueButton(
        'Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
        lambda: focus_wave.save_audio(txtinp.return_text())
        if txtinp.return_text() != '' else 0)

    txtbx1 = blueWaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, 200)

    txtbx2 = blueWaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, 200)

    txtbx3 = blueWaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, 200)

    txtbx4 = blueWaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, 200)

    slydey()
    lables()

    dd = DropDown(200, 200)

    Grapher.create_graph_image(focus_wave.audio_arr, 440)
    # vsm = GraphSelectionUtility3000(300, 100, 27)

elif SYSTEM_OS == "Linux":
    '''!!!LINUX!!!'''

    txtinp = textBox(WINDOW_WIDTH - 580, 130, 50)

    saveBx1 = blueButton('Save', WINDOW_WIDTH - 160, 130,
                         lambda: print(txtinp.return_text()))

    txtbx1 = blueWaveButton('sawtooth', WINDOW_WIDTH - 580, 50, 200)

    txtbx2 = blueWaveButton('square', WINDOW_WIDTH - 440, 50, 200)

    txtbx3 = blueWaveButton('sin', WINDOW_WIDTH - 300, 50, 200)

    txtbx4 = blueWaveButton('triangle', WINDOW_WIDTH - 160, 50, 200)

    slydey()
    lables()
    Grapher.create_graph_image(focus_wave.audio_arr, 440)

    dd = DropDown(200, 200)
    # vsm = GraphSelectionUtility3000(300,100,27)

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

    slydey()
    lables()
    Grapher.create_graph_image(focus_wave.audio_arr, 440)


else:
    print('Please use a valid Opperating system [Windows,MacOS,Linux]')

root.mainloop()

