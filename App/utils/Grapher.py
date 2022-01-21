# Used to visualize the wave function

import matplotlib.pyplot as plt

# TODO: Implement interface module

# To avoid circular imports
from ..applib.Core import constants
from .luminosity import black_or_white

# custom colors?
# plt.style.use('seaborn-dark')

# this should be changed to selected wave array

def create_graph_image(user_arr, freq) -> None:
    single_osc = constants.SAMPLE_RATE / freq

    # converts a float value to the integer above it
    if not single_osc.is_integer():
        single_osc = round(single_osc + 0.5)

    cut_arr = user_arr[:int(single_osc)]
    # user_arr = np.sin(user_arr * freq * 2 * np.pi)
    
    plt.figure(facecolor=constants.BG_GRAPH)

    ax = plt.axes()
    ax.set_facecolor(constants.FG_COLOR)

    [t.set_color(black_or_white(constants.BG_GRAPH)) for t in ax.xaxis.get_ticklabels()]
    [t.set_color(black_or_white(constants.BG_GRAPH)) for t in ax.yaxis.get_ticklabels()]

    plt.plot(cut_arr, color = constants.LINE_COLOR)
    plt.savefig('Temp/graph_img.jpg', bbox_inches='tight')