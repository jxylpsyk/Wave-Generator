import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-dark')

# this should be changed to selected wave array
# user_arr = np.linspace(0, 2, 44100 * 2)


def create_graph_image(user_arr, freq) -> None:
    single_osc = 44100 / freq

    # converts a float value to the integer above it
    if not single_osc.is_integer():
        single_osc = round(single_osc + 0.5)

    user_arr = user_arr[:int(single_osc)]
    # user_arr = np.sin(user_arr * freq * 2 * np.pi)

    plt.plot(user_arr)
    plt.savefig('Temp/graph_img.jpg')