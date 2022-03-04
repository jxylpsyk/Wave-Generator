import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys

from App.applib.Core.wave_class import Wave
from App.applib.Core.constants import *
from App.applib.Core.default_waves import make_default_wave
from App.applib.Core.audio import play_audio
import App.applib.Core.harmonictest as ht

from App.applib.utils import Grapher, messenger, wav_saver, luminosity

# The main premise of the project is for the user to do manipulations on two sound waves
# Therefore, there are two waves for the user to play around with

# The two waves are set to A440 sine waves by default

# Make the button color user editable, after the move to GUI folder, import luminosity

focus_wave = Wave(make_default_wave('sin', DEFAULT_FREQ, 1), fund_freq=DEFAULT_FREQ)

#GUI
root = tk.Tk()
root.title("Wave Generator 0.6.9.420")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

canvas = tk.Canvas(
    root, height=WINDOW_HEIGHT+10, width=WINDOW_WIDTH+10, background=BG_COLOR
)  # ,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")

canvas.place(x=-5, y=-5)

grapher = Grapher.Grapher()

# region Classes
'''

class image:
    def __init__(self,relPth, x_codds, y_codds):
        self.x_codds = x_codds
        self.y_codds = y_codds
        self.graph = Image.open(relPth)
        self.graph = ImageTk.PhotoImage(graph)
        self.graph_label = tk.label(image=graph)
        self.graph_label.image = graph
        self.graph_label.place(x=self.x_codds, y=self.y_codds)

    
    def importImage(relPth, x_codds, y_codds):
        graph = Image.open(relPth)
        graph = ImageTk.PhotoImage(graph)
        graph_label = tk.label(image=graph)
        graph_label.image = graph
        graph_label.grid(column=x_codds, row=y_codds)

    '''

class DropDown:
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

        self.dd_button = tk.Button(self.text_frame, image=self.photo, compound='center', borderwidth=0, command=lambda: self.__toggle_list())
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

# TODO: Add a frequency text box
class TextBox:
    def __init__(self, pos_x, pos_y, wdth, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.clspn = wdth
        self.textbox = tk.Text(
            root,
            width=wdth,
            height=height,
            background=FG_COLOR,
            foreground=LINE_COLOR,
        )

        self.textbox.place(x=self.pos_x, y=self.pos_y)

    def return_text(self):
        return self.textbox.get(1.0, "end-1c")

class Vertical_Slider:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.Slide = tk.Scale(root, from_=100, to=-100, length = 220)

        self.Slide.place(x=self.pos_x, y=self.pos_y)

    def set_val(self, value):
        self.Slide.set(value)

class HarmonicsLabel:
    def __init__(self, num, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.num = num

        self.label = tk.Label(text= f"H{self.num} ", width=5, anchor='center')
        self.label.place(x=pos_x, y=pos_y)

class WaveButton:
    # style = ttk.style()
    # style.configure('BW.TButton', foreground = '#ffffff', background = '#2610ff')
    def __init__(self, wave_name, position_x, position_y, freq):
        self.position_x = position_x
        self.position_y = position_y

        def __set_slider_val(index, value):
            slider_list[index].set_val(value)

        def __focus():
            # focus_wave.audio_arr = play_audio(make_default_wave(wave_name, freq, 1))
            
            if wave_name.lower() == 'sin':
                __set_slider_val(0, int(100 * 0))
                ht.freqassignfunc(0+2, 0)
                __set_slider_val(1, int(100 * 0))
                ht.freqassignfunc(1+2, 0)
                __set_slider_val(2, int(100 * 0))
                ht.freqassignfunc(2+2, 0)
                __set_slider_val(3, int(100 * 0))
                ht.freqassignfunc(3+2, 0)
                __set_slider_val(4, int(100 * 0))
                ht.freqassignfunc(4+2, 0)
                __set_slider_val(5, int(100 * 0))
                ht.freqassignfunc(5+2, 0)
                __set_slider_val(6, int(100 * 0))
                ht.freqassignfunc(6+2, 0)
                __set_slider_val(7, int(100 * 0))
                ht.freqassignfunc(7+2, 0)
                __set_slider_val(8, int(100 * 0))
                ht.freqassignfunc(8+2, 0)
                __set_slider_val(9, int(100 * 0))
                ht.freqassignfunc(9+2, 0)
                __set_slider_val(10, int(100 * 0))
                ht.freqassignfunc(10+2, 0)
                __set_slider_val(11, int(100 * 0))
                ht.freqassignfunc(11+2, 0)
                __set_slider_val(12, int(100 * 0))
                ht.freqassignfunc(12+2, 0)
                __set_slider_val(13, int(100 * 0))
                ht.freqassignfunc(13+2, 0)
                __set_slider_val(14, int(100 * 0))
                ht.freqassignfunc(14+2, 0)
                __set_slider_val(15, int(100 * 0))
                ht.freqassignfunc(15+2, 0)
                __set_slider_val(16, int(100 * 0))
                ht.freqassignfunc(16+2, 0)
                __set_slider_val(17, int(100 * 0))
                ht.freqassignfunc(17+2, 0)
                __set_slider_val(18, int(100 * 0))
                ht.freqassignfunc(18+2, 0)
                __set_slider_val(19, int(100 * 0))
                ht.freqassignfunc(19+2, 0)


            elif wave_name.lower() == 'square':
                __set_slider_val(0, int(100 * 0))
                ht.freqassignfunc(0+2, 0)
                __set_slider_val(1, int(100 * 0.3333333333333333))
                ht.freqassignfunc(1+2, 0.3333333333333333)
                __set_slider_val(2, int(100 * 0))
                ht.freqassignfunc(2+2, 0)
                __set_slider_val(3, int(100 * 0.2))
                ht.freqassignfunc(3+2, 0.2)
                __set_slider_val(4, int(100 * 0))
                ht.freqassignfunc(4+2, 0)
                __set_slider_val(5, int(100 * 0.142857142857))
                ht.freqassignfunc(5+2, 0.142857142857)
                __set_slider_val(6, int(100 * 0))
                ht.freqassignfunc(6+2, 0)
                __set_slider_val(7, int(100 * 0.1111111111111111))
                ht.freqassignfunc(7+2, 0.1111111111111111)
                __set_slider_val(8, int(100 * 0))
                ht.freqassignfunc(8+2, 0)
                __set_slider_val(9, int(100 * 0.0909090909090909))
                ht.freqassignfunc(9+2, 0.0909090909090909)
                __set_slider_val(10, int(100 * 0))
                ht.freqassignfunc(10+2, 0)
                __set_slider_val(11, int(100 * 0.0769230769))
                ht.freqassignfunc(11+2, 0.0769230769)
                __set_slider_val(12, int(100 * 0))
                ht.freqassignfunc(12+2, 0)
                __set_slider_val(13, int(100 * 0.0666666666666666))
                ht.freqassignfunc(13+2, 0.0666666666666666)
                __set_slider_val(14, int(100 * 0))
                ht.freqassignfunc(14+2, 0)
                __set_slider_val(15, int(100 * 0.0588235294118))
                ht.freqassignfunc(15+2, 0.0588235294118)
                __set_slider_val(16, int(100 * 0))
                ht.freqassignfunc(16+2, 0)
                __set_slider_val(17, int(100 * 0.0526315789474))
                ht.freqassignfunc(17+2, 0.0526315789474)
                __set_slider_val(18, int(100 * 0))
                ht.freqassignfunc(18+2, 0)
                __set_slider_val(19, int(100 * 0.047619047619))
                ht.freqassignfunc(19+2, 0.047619047619)


            elif wave_name.lower() == 'triangle':
                __set_slider_val(0, int(100 * 0))
                ht.freqassignfunc(0+2, 0)
                __set_slider_val(1, int(100 * 0.1111111111111111))
                ht.freqassignfunc(1+2, 0.1111111111111111)
                __set_slider_val(2, int(100 * 0))
                ht.freqassignfunc(2+2, 0)
                __set_slider_val(3, -int(100 * 0.04))
                ht.freqassignfunc(3+2, -0.04)
                __set_slider_val(4, int(100 * 0))
                ht.freqassignfunc(4+2, 0)
                __set_slider_val(5, int(100 * 0.0204081632653))
                ht.freqassignfunc(5+2, 0.0204081632653)
                __set_slider_val(6, int(100 * 0))
                ht.freqassignfunc(6+2, 0)
                __set_slider_val(7, -int(100 * 0.012345678901234567890123456789))
                ht.freqassignfunc(7+2, -0.012345678901234567890123456789)
                __set_slider_val(8, int(100 * 0))
                ht.freqassignfunc(8+2, 0)
                __set_slider_val(9, int(100 * 0.00826446280992))
                ht.freqassignfunc(9+2, 0.00826446280992)
                __set_slider_val(10, int(100 * 0))
                ht.freqassignfunc(10+2, 0)
                __set_slider_val(11, -int(100 * 0.00591715976331))
                ht.freqassignfunc(11+2, -0.00591715976331)
                __set_slider_val(12, int(100 * 0))
                ht.freqassignfunc(12+2, 0)
                __set_slider_val(13, int(100 * 0.0044444444444444444444444))
                ht.freqassignfunc(13+2, 0.0044444444444444444444444)
                __set_slider_val(14, int(100 * 0))
                ht.freqassignfunc(14+2, 0)
                __set_slider_val(15, -int(100 * 0.00346020761246))
                ht.freqassignfunc(15+2, -0.00346020761246)
                __set_slider_val(16, int(100 * 0))
                ht.freqassignfunc(16+2, 0)
                __set_slider_val(17, int(100 * 0.00277008310249))
                ht.freqassignfunc(17+2, 0.00277008310249)
                __set_slider_val(18, int(100 * 0))
                ht.freqassignfunc(18+2, 0)
                __set_slider_val(19, -int(100 * 0.00226757369615))
                ht.freqassignfunc(19+2, -0.00226757369615)


            elif wave_name.lower() == 'sawtooth':
                __set_slider_val(0, int(100 * 0.5))
                ht.freqassignfunc(0+2, 0.5)
                __set_slider_val(1, int(100 * 0.3333333333333333))
                ht.freqassignfunc(1+2, 0.3333333333333333)
                __set_slider_val(2, int(100 * 0.25))
                ht.freqassignfunc(2+2, 0.25)
                __set_slider_val(3, int(100 * 0.2))
                ht.freqassignfunc(3+2, 0.2)
                __set_slider_val(4, int(100 * 0.16666666666666))
                ht.freqassignfunc(4+2, 0.16666666666666)
                __set_slider_val(5, int(100 * 0.142857142857))
                ht.freqassignfunc(5+2, 0.142857142857)
                __set_slider_val(6, int(100 * 0.125))
                ht.freqassignfunc(6+2, 0.125)
                __set_slider_val(7, int(100 * 0.1111111111111111))
                ht.freqassignfunc(7+2, 0.1111111111111111)
                __set_slider_val(8, int(100 * 0.1))
                ht.freqassignfunc(8+2, 0.1)
                __set_slider_val(9, int(100 * 0.0909090909090909))
                ht.freqassignfunc(9+2, 0.0909090909090909)
                __set_slider_val(10, int(100 * 0.083333333333333))
                ht.freqassignfunc(10+2, 0.083333333333333)
                __set_slider_val(11, int(100 * 0.0769230769))
                ht.freqassignfunc(11+2, 0.0769230769)
                __set_slider_val(12, int(100 * 0.07142857142847142857))
                ht.freqassignfunc(12+2, 0.07142857142847142857)
                __set_slider_val(13, int(100 * 0.0666666666666666))
                ht.freqassignfunc(13+2, 0.0666666666666666)
                __set_slider_val(14, int(100 * 0.0626))
                ht.freqassignfunc(14+2, 0.0626)
                __set_slider_val(15, int(100 * 0.0588235294118))
                ht.freqassignfunc(15+2, 0.0588235294118)
                __set_slider_val(16, int(100 * 0.055555555555555))
                ht.freqassignfunc(16+2, 0.055555555555555)
                __set_slider_val(17, int(100 * 0.0526315789474))
                ht.freqassignfunc(17+2, 0.0526315789474)
                __set_slider_val(18, int(100 * 0.05))
                ht.freqassignfunc(18+2, 0.05)
                __set_slider_val(19, int(100 * 0.047619047619))
                ht.freqassignfunc(19+2, 0.047619047619)


            elif wave_name.lower() == 'impulse':
                __set_slider_val(0, -int(100 * 0.95))
                ht.freqassignfunc(0+2, -0.95)
                __set_slider_val(1, -int(100 * 0.9))
                ht.freqassignfunc(1+2, -0.9)
                __set_slider_val(2, int(100 * 0.85))
                ht.freqassignfunc(2+2, 0.85)
                __set_slider_val(3, int(100 * 0.8))
                ht.freqassignfunc(3+2, 0.8)
                __set_slider_val(4, -int(100 * 0.75))
                ht.freqassignfunc(4+2, -0.75)
                __set_slider_val(5, -int(100 * 0.7))
                ht.freqassignfunc(5+2, -0.7)
                __set_slider_val(6, int(100 * 0.65))
                ht.freqassignfunc(6+2, 0.65)
                __set_slider_val(7, int(100 * 0.6))
                ht.freqassignfunc(7+2, 0.6)
                __set_slider_val(8, -int(100 * 0.55))
                ht.freqassignfunc(8+2, -0.55)
                __set_slider_val(9, -int(100 * 0.5))
                ht.freqassignfunc(9+2, -0.5)
                __set_slider_val(10, int(100 * 0.45))
                ht.freqassignfunc(10+2, 0.45)
                __set_slider_val(11, int(100 * 0.4))
                ht.freqassignfunc(11+2, 0.4)
                __set_slider_val(12, -int(100 * 0.35))
                ht.freqassignfunc(12+2, -0.35)
                __set_slider_val(13, -int(100 * 0.3))
                ht.freqassignfunc(13+2, -0.3)
                __set_slider_val(14, int(100 * 0.25))
                ht.freqassignfunc(14+2, 0.25)
                __set_slider_val(15, int(100 * 0.2))
                ht.freqassignfunc(15+2, 0.2)
                __set_slider_val(16, -int(100 * 0.15))
                ht.freqassignfunc(16+2, -0.15)
                __set_slider_val(17, -int(100 * 0.1))
                ht.freqassignfunc(17+2, -0.1)
                __set_slider_val(18, int(100 * 0.05))
                ht.freqassignfunc(18+2, 0.05)
                __set_slider_val(19, int(100 * 0))
                ht.freqassignfunc(19+2, 0)

            focus_wave.audio_arr = ht.variabledef(focus_wave.freq)
            update_graph(focus_wave)
            play_audio(focus_wave.audio_arr)

        self.button = tk.Button(
            root,
            width=BUTTON_WIDTH,
            height=2,
            text=wave_name.capitalize(),
            highlightbackground=FG_COLOR,
            background=FG_COLOR,
            foreground=luminosity.black_or_white(FG_COLOR),
            command = __focus)

        self.button.place(x=self.position_x, y=self.position_y)

class UIButton:
    # style = ttk.style()
    # style.configure('BW.TButton', foreground = '#ffffff', background = '#2610ff')
    def __init__(self, name, position_x, position_y, lambda_func):
        self.position_x = position_x
        self.position_y = position_y

        self.button = tk.Button(root,
                                width=BUTTON_WIDTH,
                                height=2,
                                text=name.capitalize(),
                                highlightbackground=FG_COLOR,
                                background=FG_COLOR,
                                foreground=luminosity.black_or_white(FG_COLOR),
                                command=lambda_func)

        self.button.place(x=self.position_x, y=self.position_y)


def update_graph(user_wave):
    main_graph = FigureCanvasTkAgg(grapher.create_graph_image(user_wave), root).get_tk_widget()
    # main_graph = temp
    # temp.destroy()
    main_graph.place(x=0, y=0)

def HoverBind(widget, slider_no):

    def enter(event):
        ht.freqassignfunc(slider_no, widget.get() / 100)
        
    def leave(event):
        ht.freqassignfunc(slider_no, widget.get() / 100)
        focus_wave.audio_arr = ht.variabledef(focus_wave.freq)
        update_graph(focus_wave)

    widget.bind('<B1-Motion>', enter)
    widget.bind('<1>', enter)
    widget.bind('<B2-Motion>', enter)
    widget.bind('<2>', enter)
    widget.bind('<ButtonRelease-1>', leave)
    widget.bind('<ButtonRelease-2>', leave)

def render_sliders():

    Slider_List = [] # [1, 2, 3, 4, …]

    for i in range(19, -1, -1):
        Slider_List.append(Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*i)  , WINDOW_HEIGHT - 270))
        HarmonicsLabel( 21-i, WINDOW_WIDTH - 120 - (MyNewCuteConstant*i) , WINDOW_HEIGHT - 300)

        HoverBind (Slider_List[19-i].Slide, 21-i)
    
    return Slider_List

def set_freq():
    if freq_box.return_text().strip() != '':
        freq = int(freq_box.return_text())
        focus_wave.freq = freq
        focus_wave.audio_arr = ht.variabledef(focus_wave.freq)

        update_graph(focus_wave)






if SYSTEM_OS == "Darwin":
    '''!!!OsX!!!'''

    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 54, 2)

    freq_box = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, 6, 1)
    freq_set_btn = UIButton('Set', WINDOW_WIDTH - 520, WINDOW_HEIGHT - 600, set_freq)

    # load_btn = UIButton('Load', WINDOW_WIDTH - 500, WINDOW_HEIGHT - 700)  

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                            lambda: focus_wave.save_audio(txtinp.return_text())
                            if txtinp.return_text() != '' else 0)
    
    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 590,
                            lambda: wav_saver.save_as_wav(focus_wave.audio_arr))

    slider_list = render_sliders()

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, focus_wave.freq)
    
    txtbx5 = WaveButton('impulse', WINDOW_WIDTH - 70, WINDOW_HEIGHT - 750, focus_wave.freq)

    dd = DropDown(200, 200)



    update_graph(focus_wave)





elif SYSTEM_OS == "Linux":
    '''!!!LINUX!!!'''

    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 54, 2)

    freq_box = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, 6, 1)
    freq_set_btn = UIButton('Set', WINDOW_WIDTH - 520, WINDOW_HEIGHT - 600, set_freq)

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                            lambda: focus_wave.save_audio(txtinp.return_text())
                            if txtinp.return_text() != '' else 0)

    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 590,
                            lambda: wav_saver.save_as_wav(focus_wave))

    slider_list = render_sliders()

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx5 = WaveButton('impulse', WINDOW_WIDTH - 70, WINDOW_HEIGHT - 750, focus_wave.freq)

    dd = DropDown(200, 200)


    update_graph(focus_wave)


elif SYSTEM_OS == "Windows":
    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 50, 2)

    freq_box = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, 6, 1)
    freq_set_btn = UIButton('Set', WINDOW_WIDTH - 520, WINDOW_HEIGHT - 600, set_freq)

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                            lambda: focus_wave.save_audio(txtinp.return_text())
                            if txtinp.return_text() != '' else 0)
    
    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 590,
                        lambda: wav_saver.save_as_wav(focus_wave))

    slider_list = render_sliders()

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx5 = WaveButton('impulse', WINDOW_WIDTH - 70, WINDOW_HEIGHT - 750, focus_wave.freq)

    dd = DropDown(200, 200)


    update_graph(focus_wave)


else:
    print('Please use a valid Opperating system [Windows ,MacOS, Linux]')

root.mainloop()

