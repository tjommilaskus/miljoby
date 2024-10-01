import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.widgets import Button

x = np.linspace(0,5, 50)
y = [0] * len(x)

fig = figure(figsize=(6,5))
ax1 = fig.add_axes((0.1,0.3,0.8,0.5))
ax1.title.set_text('Graphs')

line, = plt.plot(x, y, color='red')

def plot1(event):
    line.set_ydata(x**2)
    ax1.set_ylim(0, 64)
    plt.draw()

axButn1 = plt.axes((0.1, 0.1, 0.3, 0.1))
btn1 = Button(    axButn1, label="Y=X**2", color='lightblue', hovercolor='tomato')
btn1.on_clicked(plot1)

def plot2(event):
    line.set_ydata(.5*x ** 3)
    ax1.set_ylim(0, 64)
    plt.draw()

axButn2 = plt.axes((0.6, 0.1, 0.3, 0.1))
btn2 = Button( axButn2, label="Y=0.5*X**3", color='lightblue', hovercolor='tomato')
btn2.on_clicked(plot2)
plot1(None)
plt.show()