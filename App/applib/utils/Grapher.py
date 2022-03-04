# Used to visualize the wave function

import matplotlib.pyplot as plt
import numpy as np

# TODO: Implement interface module

# To avoid circular imports
from ..Core import constants
from .luminosity import black_or_white
from .analyser import AudioDetector

# custom colors?
# plt.style.use('seaborn-dark')

# this should be changed to selected wave array

class Grapher:

    def __init__(self) -> None:
        self.fig = plt.figure(facecolor=constants.BG_COLOR)
        self.plot1 = self.fig.add_subplot(111)

        ax = self.fig.axes[0]
        ax.set_facecolor(constants.FG_COLOR)

        plt.tight_layout()

    def create_graph_image(self, user_wave) -> None:
        # freq = AudioDetector().find_highest_probable_frequency(user_arr)
        freq = user_wave.freq

        user_arr = user_wave.audio_arr

        single_osc = constants.SAMPLE_RATE / freq

        # converts a float value to the integer above it
        if not single_osc.is_integer():
            single_osc = round(single_osc + 0.5)

        if np.max(user_arr) > 1:
            user_arr = user_arr/np.max(user_arr)

        cut_arr = user_arr[:int(single_osc)]
        plt.cla()

        ax = self.fig.axes[0]

        [t.set_color(black_or_white(constants.BG_COLOR)) for t in ax.xaxis.get_ticklabels()]
        [t.set_color(black_or_white(constants.BG_COLOR)) for t in ax.yaxis.get_ticklabels()]

        self.plot1.plot(cut_arr, color= constants.LINE_COLOR)

        return self.fig

   

    # plt.savefig('Images/graph_img.jpg', bbox_inches='tight')
    # plt.close()

    