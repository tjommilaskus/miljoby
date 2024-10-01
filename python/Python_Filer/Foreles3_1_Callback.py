from random import randint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons

def GenerateGraph(_xval, startval):
    kurs = []
    for x in _xval:
        val = randint(-9,10) + startval
        kurs.append(val)
        startval = val
    return kurs

xvalA = np.linspace(1,365,365)
kursA = GenerateGraph(xvalA, 100)
kursB = GenerateGraph(xvalA, 130)
fig = plt.figure(figsize=(8,5))

ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
axRadio = fig.add_axes((0.7, 0.8, 0.2, 0.2))
axBV = fig.add_axes((0.1, 0.05, 0.2, 0.075))
axBC = fig.add_axes((0.7, 0.05, 0.2, 0.075))

x0 = 0
def MoveX(dx):
    global x0
    x0 += dx
    ax.set_xlim([x0, x0+30])
    plt.draw()
def on_button_forward(Any):
    MoveX(30)
def on_button_back(Any):
    MoveX(-30)

button1 = Button(axBV, "50 +", color="red")
button2 = Button(axBC, "50 -", color="lightblue")
button1.on_clicked(on_button_forward)
button2.on_clicked(on_button_back)

lines = ax.plot(xvalA, kursA)

ax.set_xlim([x0, x0+30])
ax.set_ylim([50, 300])
ax.set_title("Aksjer 2024")
def on_velg(aksje):
    if aksje == 'Firma A':
        lines[0].set_ydata(kursA)
        lines[0].set_color('blue')
    if aksje == 'Firma B':
        lines[0].set_ydata(kursB)
        lines[0].set_color('red')
    plt.draw()
radio_button = RadioButtons(axRadio, ('Firma A', 'Firma B'),
                            label_props={'color': ['blue', 'red'], 'fontsize' : [10,10]},
                            radio_props={'facecolor':  ['blue', 'red'],
                                         'edgecolor': ['blue', 'red']}
                            )
radio_button.on_clicked(on_velg)
plt.show()