# Used to visualize the wave function

import matplotlib.pyplot as plt

# TODO: Implement interface module

# To avoid circular imports
from ..Core import constants
from .luminosity import black_or_white
from .analyser import AudioDetector

# custom colors?
# plt.style.use('seaborn-dark')

# this should be changed to selected wave array


def create_graph_image(user_arr) -> None:
    freq = AudioDetector().find_highest_probable_frequency(user_arr)

    single_osc = constants.SAMPLE_RATE / freq

    # converts a float value to the integer above it
    if not single_osc.is_integer():
        single_osc = round(single_osc + 0.5)

    cut_arr = user_arr[:int(single_osc)]
    
    fig = plt.figure(facecolor=constants.BG_COLOR)

    plot1 = fig.add_subplot(111)
    plot1.plot(cut_arr, color= constants.LINE_COLOR)

    ax = fig.axes[0]
    ax.set_facecolor(constants.FG_COLOR)

    [t.set_color(black_or_white(constants.BG_COLOR)) for t in ax.xaxis.get_ticklabels()]
    [t.set_color(black_or_white(constants.BG_COLOR)) for t in ax.yaxis.get_ticklabels()]

    # plt.savefig('Images/graph_img.jpg', bbox_inches='tight')
    # plt.close()

    return fig