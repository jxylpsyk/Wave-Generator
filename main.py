import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from App.applib.Core.wave_class import Wave
from App.applib.Core.constants import *
from App.applib.Core.default_waves import make_default_wave
from App.applib.Core.audio import play_audio
import App.applib.Core.harmonictest as ht

from App.applib.utils import Grapher, messenger, wav_saver, luminosity

# The main premise of the project is for the user to do manipulations on two sound waves
# Therefore, there are two waves for the user to play around with

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

    def __toggle_list(self):
        self.__refresh_list()
        self.drop_state = not self.drop_state

        if self.drop_state:
            self.__create_list()
        else:
            self.__destroy_list()

    def __refresh_list(self):
        self.user_wave_names = messenger.get_user_waves()

    
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

            # * IMPORTANT
            def __change_label(wave_name):
                self.selected_wave = wave_name.strip()
                self.t_label['text'] = self.selected_wave
                self.__destroy_list()
                self.drop_state = not self.drop_state

                everything_from_list(focus_wave.return_list(self.selected_wave)) # !!!!!!!!!!!SDAKJNSKJDCNd



            unindent_x =  self.dd_button.winfo_x() + self.pos_x - 179
            unindent_y =  self.dd_button.winfo_y() + self.pos_y + 24
            for i, wave in enumerate(__normalize_length(self.user_wave_names)):
                tk.Button(self.list_frame, width=19, text=wave, compound='top', borderwidth=0, command = lambda w_name=wave : __change_label(w_name)).pack()

            self.list_frame.place(x=unindent_x, y=unindent_y)

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
    
    def clear_text(self):
        self.textbox.delete('1.0', tk.END)

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
    def __init__(self, wave_name, position_x, position_y, freq):
        self.position_x = position_x
        self.position_y = position_y
        self.sldr_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        def __focus():
            if wave_name.lower() == 'sin':

                self.sldr_list[0] = 0
                self.sldr_list[1] = 0
                self.sldr_list[2] = 0
                self.sldr_list[3] = 0
                self.sldr_list[4] = 0
                self.sldr_list[5] = 0
                self.sldr_list[6] = 0
                self.sldr_list[7] = 0
                self.sldr_list[8] = 0
                self.sldr_list[9] = 0
                self.sldr_list[10] = 0
                self.sldr_list[11] = 0
                self.sldr_list[12] = 0
                self.sldr_list[13] = 0
                self.sldr_list[14] = 0
                self.sldr_list[15] = 0
                self.sldr_list[16] = 0
                self.sldr_list[17] = 0
                self.sldr_list[18] = 0
                self.sldr_list[19] = 0

            
            elif wave_name.lower() == 'square':
                self.sldr_list[0] = 0
                self.sldr_list[1] = 0.3333333333333333
                self.sldr_list[2] = 0
                self.sldr_list[3] = 0.2
                self.sldr_list[4] = 0
                self.sldr_list[5] = 0.142857142857
                self.sldr_list[6] = 0
                self.sldr_list[7] = 0.1111111111111111
                self.sldr_list[8] = 0
                self.sldr_list[9] = 0.0909090909090909
                self.sldr_list[10] = 0
                self.sldr_list[11] = 0.0769230769
                self.sldr_list[12] = 0
                self.sldr_list[13] = 0.0666666666666666
                self.sldr_list[14] = 0
                self.sldr_list[15] = 0.0588235294118
                self.sldr_list[16] = 0
                self.sldr_list[17] = 0.0526315789474
                self.sldr_list[18] = 0
                self.sldr_list[19] = 0.047619047619

            
            elif wave_name.lower() == 'triangle':
                self.sldr_list[0] = 0
                self.sldr_list[1] = 0.1111111111111111
                self.sldr_list[2] = 0
                self.sldr_list[3] = -0.04
                self.sldr_list[4] = 0
                self.sldr_list[5] = 0.0204081632653
                self.sldr_list[6] = 0
                self.sldr_list[7] = -0.012345678901234567890123456789
                self.sldr_list[8] = 0
                self.sldr_list[9] = 0.00826446280992
                self.sldr_list[10] = 0
                self.sldr_list[11] = -0.00591715976331
                self.sldr_list[12] = 0
                self.sldr_list[13] = 0.0044444444444444444444444
                self.sldr_list[14] = 0
                self.sldr_list[15] = -0.00346020761246
                self.sldr_list[16] = 0
                self.sldr_list[17] = 0.00277008310249
                self.sldr_list[18] = 0
                self.sldr_list[19] = -0.00226757369615

            
            elif wave_name.lower() == 'sawtooth':
                self.sldr_list[0] = 0.5
                self.sldr_list[1] = 0.3333333333333333
                self.sldr_list[2] = 0.25
                self.sldr_list[3] = 0.2
                self.sldr_list[4] = 0.16666666666666
                self.sldr_list[5] = 0.142857142857
                self.sldr_list[6] = 0.125
                self.sldr_list[7] = 0.1111111111111111
                self.sldr_list[8] = 0.1
                self.sldr_list[9] = 0.0909090909090909
                self.sldr_list[10] = 0.083333333333333
                self.sldr_list[11] = 0.0769230769
                self.sldr_list[12] = 0.07142857142847142857
                self.sldr_list[13] = 0.0666666666666666
                self.sldr_list[14] = 0.0626
                self.sldr_list[15] = 0.0588235294118
                self.sldr_list[16] = 0.055555555555555
                self.sldr_list[17] = 0.0526315789474
                self.sldr_list[18] = 0.05
                self.sldr_list[19] = 0.047619047619

            
            elif wave_name.lower() == 'impulse':
                self.sldr_list[0] = -0.95
                self.sldr_list[1] = -0.9
                self.sldr_list[2] = 0.85
                self.sldr_list[3] = 0.8
                self.sldr_list[4] = -0.75
                self.sldr_list[5] = -0.7
                self.sldr_list[6] = 0.65
                self.sldr_list[7] = 0.6
                self.sldr_list[8] = -0.55
                self.sldr_list[9] = -0.5
                self.sldr_list[10] = 0.45
                self.sldr_list[11] = 0.4
                self.sldr_list[12] = -0.35
                self.sldr_list[13] = -0.3
                self.sldr_list[14] = 0.25
                self.sldr_list[15] = 0.2
                self.sldr_list[16] = -0.15
                self.sldr_list[17] = -0.1
                self.sldr_list[18] = 0.05
                self.sldr_list[19] = 0

            everything_from_list(self.sldr_list)



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

    return 1

def everything_from_list(slider_list_ll):
    for i, val in enumerate(slider_list_ll):
        slider_list[i].set_val( int(val * 100) )
        ht.freqassignfunc(i+2, val)
    
    focus_wave.audio_arr = ht.variabledef(focus_wave.freq)
    update_graph(focus_wave)
    play_audio(focus_wave.audio_arr)

# bind events to sliders
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

# make sliders
def render_sliders():

    Slider_List = [] # [1, 2, 3, 4, …]

    for i in range(19, -1, -1):
        Slider_List.append(Vertical_Slider(WINDOW_WIDTH -118- (MyNewCuteConstant*i)  , WINDOW_HEIGHT - 270))
        HarmonicsLabel( 21-i, WINDOW_WIDTH - 120 - (MyNewCuteConstant*i) , WINDOW_HEIGHT - 300)

        HoverBind (Slider_List[19-i].Slide, 21-i)
    
    return Slider_List

# update frequencies
def set_freq():
    if freq_box.return_text().strip() != '':
        freq = int(freq_box.return_text())
        focus_wave.freq = freq
        focus_wave.audio_arr = ht.variabledef(focus_wave.freq)

        update_graph(focus_wave)

def save_necessities():
    
    focus_wave.save_audio(ht.return_sldr_list(), txtinp.return_text() if txtinp.return_text().strip() != '' else dd.selected_wave) #!?!?!?!?!?!?!??!?!?!?!!?!?!?!?!?!
    txtinp.clear_text()

if SYSTEM_OS == "Darwin":
    '''!!!OsX!!!'''

    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 54, 2)

    freq_box = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, 6, 1)
    freq_set_btn = UIButton('Set', WINDOW_WIDTH - 479, WINDOW_HEIGHT - 600, set_freq)

    # load_btn = UIButton('Load', WINDOW_WIDTH - 500, WINDOW_HEIGHT - 700)
    dd = DropDown(600, 200)

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                       lambda: save_necessities())

    del_btn = UIButton('Delete', WINDOW_WIDTH - 379, WINDOW_HEIGHT - 600,
                       lambda: focus_wave.delete_list(dd.selected_wave) if dd.selected_wave != '' else 0)

    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 600,
                            lambda: wav_saver.save_as_wav(focus_wave.audio_arr))

    slider_list = render_sliders()

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 479, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 379, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 269, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx5 = WaveButton('impulse', WINDOW_WIDTH - 159, WINDOW_HEIGHT - 750, focus_wave.freq)

    play_btn = UIButton('Play', WINDOW_WIDTH - 269, WINDOW_HEIGHT - 600, lambda: play_audio(focus_wave.audio_arr))

    update_graph(focus_wave)




elif SYSTEM_OS == "Linux":
    '''!!!LINUX!!!'''

    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 54, 2)

    freq_box = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, 6, 1)
    freq_set_btn = UIButton('Set', WINDOW_WIDTH - 479, WINDOW_HEIGHT - 600, set_freq)

    # load_btn = UIButton('Load', WINDOW_WIDTH - 500, WINDOW_HEIGHT - 700)
    dd = DropDown(600, 200)

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 130, WINDOW_HEIGHT - 670,
                       lambda: save_necessities())

    del_btn = UIButton('Delete', WINDOW_WIDTH - 379, WINDOW_HEIGHT - 600,
                       lambda: focus_wave.delete_list(dd.selected_wave) if dd.selected_wave != '' else 0)

    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 600,
                            lambda: wav_saver.save_as_wav(focus_wave.audio_arr))

    slider_list = render_sliders()

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 479, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 379, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 269, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx5 = WaveButton('impulse', WINDOW_WIDTH - 159, WINDOW_HEIGHT - 750, focus_wave.freq)

    play_btn = UIButton('Play', WINDOW_WIDTH - 269, WINDOW_HEIGHT - 600, lambda: play_audio(focus_wave.audio_arr))

    update_graph(focus_wave)



elif SYSTEM_OS == "Windows":
    txtinp = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 670, 50, 2)

    freq_box = TextBox(WINDOW_WIDTH - 580, WINDOW_HEIGHT - 600, 6, 1)
    freq_set_btn = UIButton('Set', WINDOW_WIDTH - 520, WINDOW_HEIGHT - 600, set_freq)

    saveBx1 = UIButton('Save', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 670,
                            lambda: focus_wave.save_audio(txtinp.return_text())
                            if txtinp.return_text() != '' else 0)
    
    save_wav_btn = UIButton('Save as .wav', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 600,
                        lambda: wav_saver.save_as_wav(focus_wave))

    slider_list = render_sliders()

    txtbx1 = WaveButton('sawtooth', WINDOW_WIDTH - 580, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx2 = WaveButton('square', WINDOW_WIDTH - 440, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx3 = WaveButton('sin', WINDOW_WIDTH - 300, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx4 = WaveButton('triangle', WINDOW_WIDTH - 160, WINDOW_HEIGHT - 750, focus_wave.freq)

    txtbx5 = WaveButton('impulse', WINDOW_WIDTH - 70, WINDOW_HEIGHT - 750, focus_wave.freq)

    play_btn = UIButton('Play', 500, 500, lambda: play_audio(focus_wave.audio_arr))

    dd = DropDown(200, 200)


    update_graph(focus_wave)


else:
    print('Please use a valid Opperating system [Windows ,MacOS, Linux]')

root.mainloop()

