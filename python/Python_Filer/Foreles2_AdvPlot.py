#Multiple axis
import matplotlib.pyplot as plt
import numpy as ny
import math

fig = plt.figure(figsize=(8,4))
ax1 = fig.add_axes((0.05,0.55,0.4, 0.35))
ax2 = fig.add_axes((0.5,0.55,0.4, 0.35))
ax3 = fig.add_axes((0.05,0.1, 0.85,0.3))

x = ny.linspace(0.0,10,101)
y1 = [math.sin(t) for t in x]
y2 = [math.cos(t) for t in x]
ax1.plot(x,y1)
ax2.plot(x,y2)
ax1.set_title("sinus")
ax2.set_title("cosinus")

ax3.set_title("sinus & cosinus")
ax3.plot(x,y1,x,y2)

plt.show()