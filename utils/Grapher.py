# Used to visualize the wave function

import matplotlib.pyplot as plt

from applib.Core.constants import SAMPLE_RATE

# custom colors?
plt.style.use('seaborn-dark')

# this should be changed to selected wave array
# user_arr = np.linspace(0, 2, 44100 * 2)


def create_graph_image(user_arr, freq) -> None:
    single_osc = SAMPLE_RATE / freq

    # converts a float value to the integer above it
    if not single_osc.is_integer():
        single_osc = round(single_osc + 0.5)

    cut_arr = user_arr[:int(single_osc)]
    # user_arr = np.sin(user_arr * freq * 2 * np.pi)

    plt.plot(cut_arr)
    plt.savefig('Temp/graph_img.jpg')