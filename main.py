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

focus_wave = Wave(make_default_wave('sin', 440, 1))

FREQ = 440 # default

#GUI
root = tk.Tk()
root.title("Wave Generator 0.6.9.420")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

canvas = tk.Canvas(
    root, height=WINDOW_HEIGHT+10, width=WINDOW_WIDTH+10, background=BG_COLOR
)  # ,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")

canvas.place(x=-5, y=-5)

# converts plt.Figure to a tk.Canvas
main_graph = FigureCanvasTkAgg(Grapher.create_graph_image(focus_wave.audio_arr), root).get_tk_widget()
main_graph.place(x=0, y=0)

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
        self.Slide = tk.Scale(root, from_=100, to=0, length = 220)

        self.Slide.place(x=self.pos_x, y=self.pos_y)

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

        def __focus():
            focus_wave.audio_arr = play_audio(make_default_wave(wave_name, freq, 1))

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

# ! Not used
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

def update_graph(user_arr):
    temp = FigureCanvasTkAgg(Grapher.create_graph_image(user_arr), root).get_tk_widget()
    main_graph.destroy()
    # main_graph = temp
    # temp.destroy()
    temp.place(x=0, y=0)

def HoverBind(widget, slider_no):

    labeleyo = tk.Label(root, text='hahahano')

    def enter(event):
        labeleyo['text'] = slider_no
        labeleyo.place(x=100, y=100)
        # print(widget.get())
        # TODO: call function to update harmonics, pass in widget.get()
        # widget.get()
        ht.freqassignfunc(slider_no, widget.get())
        
    def leave(event):
        labeleyo.place(x=200, y=50)
        labeleyo.place_forget()
        # print('hello')
        # TODO: call function to update graph shape
        focus_wave.audio_arr = ht.make_arr()
        update_graph(focus_wave.audio_arr)

    widget.bind('<B1-Motion>', enter)
    widget.bind('<ButtonRelease-1>', leave)

def render_sliders():

    Slider_List = [] # [1, 2, 3, 4, …]

    for i in range(19, -1, -1):
        Slider_List.append(Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*i)  , WINDOW_HEIGHT - 270))
        HarmonicsLabel( 21-i, WINDOW_WIDTH - 120 - (MyNewCuteConstant*i) , WINDOW_HEIGHT - 300)

        HoverBind (Slider_List[19-i].Slide, 21-i)

if SYSTEM_OS == "Darwin":
    '''!!!OsX!!!'''

    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 54, 2)

    freq_box = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, 6, 1)
    # freq_set_btn = UIButton('Set', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, lambda: FREQ = int(freq_box.return_text()))

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                            lambda: focus_wave.save_audio(txtinp.return_text())
                            if txtinp.return_text() != '' else 0)
    
    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 590,
                            lambda: wav_saver.save_as_wav(focus_wave.audio_arr))

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, 440)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, 440)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, 440)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, 440)

    dd = DropDown(200, 200)


    render_sliders()













elif SYSTEM_OS == "Linux":
    '''!!!LINUX!!!'''

    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 54, 2)

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                            lambda: focus_wave.save_audio(txtinp.return_text())
                            if txtinp.return_text() != '' else 0)

    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 590,
                            lambda: wav_saver.save_as_wav(focus_wave))

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, 440)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, 440)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, 440)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, 440)

    dd = DropDown(200, 200)

    render_sliders()

elif SYSTEM_OS == "Windows":
    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 50, 2)

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                            lambda: focus_wave.save_audio(txtinp.return_text())
                            if txtinp.return_text() != '' else 0)
    
    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 590,
                        lambda: wav_saver.save_as_wav(focus_wave))

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, 440)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, 440)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, 440)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, 440)

    dd = DropDown(200, 200)

    render_sliders()

else:
    print('Please use a valid Opperating system [Windows ,MacOS, Linux]')

root.mainloop()

