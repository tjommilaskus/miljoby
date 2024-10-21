import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
from matplotlib.widgets import RectangleSelector
import random
from random import randint

# Generate random data for a year
def GenereateRandomYearDataList(intencity: float, seed: int = 0) -> list[int]:
    """
    :param intencity: Number specifying size, amplitude
    :param seed: If given, same data with seed is generated
    :return:
    """
    if seed != 0:
        random.seed(seed)
    centervals = [200, 150, 100, 75, 75, 75, 50, 75, 100, 150, 200, 250, 300]
    centervals = [x * intencity for x in centervals]
    nox = centervals[0]
    inc = True
    noxList = []
    for index in range(1, 365):
        if randint(1, 100) > 50:
            inc = not inc
        center = centervals[int(index / 30)]
        dx = min(2.0, max(0.5, nox / center))
        nox = nox + randint(1, 5) / dx if inc else nox - randint(1, 5) * dx
        nox = max(10, nox)
        noxList.append(nox)
    return noxList

_kron_nox = GenereateRandomYearDataList(intencity=1.0, seed=2)
_nord_nox = GenereateRandomYearDataList(intencity=.3, seed=1)

# Create figure and axes
fig = plt.figure(figsize=(13, 5))
axNok = fig.add_axes((0.05, 0.05, 0.45, 0.9))
axInterval = fig.add_axes((0.4, 0.5, 0.1, 0.25))
axBergen = fig.add_axes((0.5, 0.05, 0.5, 0.9))

coordinates_Nordnes = (400, 315)
coordinates_Kronstad = (1140, 1140)
days_interval = (1, 365)
marked_point = (0, 0)

def on_day_interval(kvartal):
    global days_interval, marked_point
    axNok.cla()
    days_interval = (1, 365)
    if kvartal == '1. Kvartal':
        days_interval = (1, 90)
    if kvartal == '2. Kvartal':
        days_interval = (90, 180)
    if kvartal == '3. Kvartal':
        days_interval = (180, 270)
    if kvartal == '4. Kvartal':
        days_interval = (270, 365)
    marked_point = (0, 0)
    plot_graph()

def on_click(event):
    global marked_point
    if event.inaxes == axBergen:
        marked_point = (event.xdata, event.ydata)
        plot_graph()

# Estimate NOX value based on the two measuring stations
def CalcPointValue(valN, valK):
    distNordnes = math.dist(coordinates_Nordnes, marked_point)
    distKronstad = math.dist(coordinates_Kronstad, marked_point)
    distNordnesKronstad = math.dist(coordinates_Nordnes, coordinates_Kronstad)
    val = (1 - distKronstad / (distKronstad + distNordnes)) * valK + (1 - distNordnes / (distKronstad + distNordnes)) * valN
    val = val * (distNordnesKronstad / (distNordnes + distKronstad)) ** 4
    return val

# Draw circles for measuring stations
def draw_circles_stations():
    circle = mpatches.Circle((coordinates_Nordnes), 50, color='blue')
    axBergen.add_patch(circle)
    circle = mpatches.Circle((coordinates_Kronstad), 50, color='red')
    axBergen.add_patch(circle)

# Draw labels and ticks
def draw_label_and_ticks():
    num_labels = 12
    xlabels = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
    xticks = np.linspace(15, 345, num_labels)
    if days_interval[1] == 90:
        xticks = [15, 45, 75]
        xlabels = ['Jan', 'Feb', 'Mars']
    if days_interval[1] == 180:
        xticks = [15, 45, 75]
        xlabels = ['April', 'Mai', 'Juni']
    if days_interval[1] == 270:
        xticks = [15, 45, 75]
        xlabels = ['July', 'Aug', 'Sept']
    if days_interval[0] == 270:
        xticks = [15, 45, 75]
        xlabels = ['Okt', 'Nov', 'Des']
    
    axNok.set_xticks(xticks)
    axNok.set_xticklabels(xlabels, color='white')
    axNok.tick_params(axis='y', colors='white')
    axNok.xaxis.label.set_color('white')
    axNok.yaxis.label.set_color('white')

# Plot the graph
def plot_graph():
    axNok.cla()
    axBergen.cla()
    noxN = _nord_nox[days_interval[0]:days_interval[1]]
    noxK = _kron_nox[days_interval[0]:days_interval[1]]
    days = len(noxN)
    noxS = [(noxN[i] + noxK[i]) / 2 for i in range(days)]
    list_days = np.linspace(1, days, days)

    # Draw the marked point and the orange graph
    if marked_point != (0, 0):
        nox_point = [CalcPointValue(noxN[i], noxK[i]) for i in range(days)]
        axNok.plot(list_days, nox_point, 'darkorange')
        circle = mpatches.Circle((marked_point[0], marked_point[1]), 50, color='orange')
        axBergen.add_patch(circle)

    axNok.plot(list_days, noxN, color='#00ffff', linewidth=2, alpha=0.9, label='Nordnes')
    axNok.plot(list_days, noxK, color='#ff3366', linewidth=2, alpha=0.9, label='Kronstad')
    axNok.plot(list_days, noxS, color='#2cff05', linewidth=2, alpha=0.9, label='Gjennomsnitt')

    axNok.fill_between(list_days, noxN, color='#00ffff', alpha=0.2)
    axNok.fill_between(list_days, noxK, color='#ff3366', alpha=0.2)
    axNok.fill_between(list_days, noxS, color='#2cff05', alpha=0.2)

    axNok.set_facecolor('#212946')
    axBergen.set_facecolor('#212946')
    axNok.figure.set_facecolor('#212946')

    axNok.set_title("NOX verdier", color='0.9')
    axInterval.set_title("Intervall", color='0.9')

    axNok.legend(["Nordnes", "Kronstad", "Gjennomsnitt"])
    axNok.grid(linestyle='-', color='#2A3459', linewidth=0.6)
    draw_label_and_ticks()

    # Plot map of Bergen
    axBergen.axis('off')
    img = mpimg.imread('map.jpg')
    axBergen.imshow(img)
    axBergen.set_title("Kart Bergen")
    draw_circles_stations()
    plt.draw()

plot_graph()

# RectangleSelector behavior
def onselect(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"Start position: ({x1}, {y1})")
    print(f"End position: ({x2}, {y2})")
    print(f"Width: {abs(x2 - x1)}, Height: {abs(y2 - y1)}")

# Toggle RectangleSelector
def toggle_selector(event):
    if event.key in ['Q', 'q'] and rect_selector.active:
        print('RectangleSelector deactivated.')
        rect_selector.set_active(False)
    elif event.key in ['A', 'a'] and not rect_selector.active:
        print('RectangleSelector activated.')
        rect_selector.set_active(True)

# Initialize RectangleSelector
rect_selector = RectangleSelector(axBergen, onselect,
                                  interactive=True, button=[1],
                                  minspanx=5, minspany=5)

# Connect the toggle selector to the keypress event
plt.connect('key_press_event', toggle_selector)

# Connect the on_click event
plt.connect('button_press_event', on_click)

# Draw radio button interval
listFonts = [12] * 5
listColors = ['yellow'] * 5
radio_button = RadioButtons(axInterval, ('År','1. Kvartal','2. Kvartal','3. Kvartal','4. Kvartal'),
                            label_props={'color': listColors, 'fontsize': listFonts},
                            radio_props={'facecolor': listColors, 'edgecolor': listColors})
axInterval.set_facecolor('#00FFFF')

# Customize the box around the radio button interval
for spine in axInterval.spines.values():
    spine.set_edgecolor('0.9')
    spine.set_linewidth(2)

radio_button.on_clicked(on_day_interval)

# Show the plot with the selector enabled
plt.show()
