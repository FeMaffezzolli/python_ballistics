import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

# GLOBALS
g = 9.80665
time_frame_seconds = 180
frames = 900
time_vector = np.linspace(0, time_frame_seconds, frames)
v0_max = 45
alfa_init = 76

def y_t(v0, alfa, t):
    return v0 * math.sin(math.radians(alfa)) * t - (g * (t**2) / 2)

def x_t(v0, alfa, t):
    return v0 * math.cos(math.radians(alfa)) * t

x_pos, y_pos = [], []
for t in time_vector:
    if (y_t(v0_max, alfa_init, t) > 0):
        x_pos.append(x_t(v0_max, alfa_init, t))
        y_pos.append(y_t(v0_max, alfa_init, t))

plt.figure('Launch')
plt.plot(x_pos, y_pos)
plt.scatter(x_pos, y_pos)
