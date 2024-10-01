
import matplotlib.pyplot as plt
import numpy as ny
from math import sin, cos


x = ny.linspace(0.0,10,101)
y = [sin(t) for t in x]
z = [cos(t) for t in x]
fig = plt.figure(figsize=(13, 6))
axis = fig.add_axes((.1, .1, .8, .8))

axis.set_title("Velkommen til Sinus og Cosinus - Nå er du igang")
axis.plot(x, y, x, z)
plt.show()

