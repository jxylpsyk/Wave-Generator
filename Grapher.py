import matplotlib

import matplotlib.pyplot as plt
import numpy as np

user_arr = np.linspace(0, 2, 44100 * 2)
freq = 4000
graph_cut = 44100 / freq

# converts a float value to the integer above it
if not graph_cut.is_integer():
    graph_cut = round(graph_cut + 0.5)

user_arr = user_arr[:int(graph_cut)]
user_arr = np.sin(user_arr * freq * 2 * np.pi)

plt.style.use('seaborn-dark')
plt.plot(user_arr)

x = 129.0
print(x.is_integer())