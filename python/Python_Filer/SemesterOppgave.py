import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import random
from random import randint

# Generate random data for a year
def GenerateRandomYearDataList(intencity=1.0, seed=0):
    """
    :param intencity: Number specifying size, amplitude
    :param seed: If given, same data with seed is generated
    :return: List of generated NOX values for the year
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


_kron_nox = GenerateRandomYearDataList(intencity=1.0, seed=2)
_nord_nox = GenerateRandomYearDataList(intencity=0.3, seed=1)

# Create figure and 3 axes
fig = plt.figure(figsize=(13, 5))
axNok = fig.add_axes((0.05, 0.05, 0.45, 0.9))
axInterval = fig.add_axes((0.4, 0.5, 0.1, 0.25))
axBergen = fig.add_axes((0.5, 0.05, 0.5, 0.9))

# Set futuristic color schemes
axNok.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
axInterval.grid(False)  # No grid for the interval selector
axBergen.grid(False)

# Set alpha transparency for axInterval
axInterval.patch.set_alpha(0.6)

coordinates_Nordnes = (400, 315)
coordinates_Kronstad = (1140, 1140)
days_interval = (1, 365)
marked_point = (0, 0)


# Day interval for radio buttons
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


# Handle mouse click events for the map
def on_click(event):
    global marked_point
    if ax := event.inaxes:
        if ax == axBergen:
            marked_point = (event.xdata, event.ydata)
            plot_graph()


# Estimate NOX value based on stations
def CalcPointValue(valN, valK):
    distNordnes = math.dist(coordinates_Nordnes, marked_point)
    distKronstad = math.dist(coordinates_Kronstad, marked_point)
    distNordnesKronstad = math.dist(coordinates_Nordnes, coordinates_Kronstad)
    val = (1 - distKronstad / (distKronstad + distNordnes)) * valK + \
          (1 - distNordnes / (distKronstad + distNordnes)) * valN
    val = val * (distNordnesKronstad / (distNordnes + distKronstad)) ** 4
    return val


# Draw circles for the stations
def draw_circles_stations():
    circle = mpatches.Circle((coordinates_Nordnes), 50, color='#39FF14', alpha=0.8)  # Neon Green for Nordnes
    axBergen.add_patch(circle)
    circle = mpatches.Circle((coordinates_Kronstad), 50, color='#FF3366', alpha=0.8)  # Neon Pink for Kronstad
    axBergen.add_patch(circle)


# Customize axis labels and ticks
def draw_label_and_ticks():
    num_labels = 12
    xlabels = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
    xticks = np.linspace(15, 345, num_labels)
    if days_interval[1] == 90:
        xticks = [15, 45, 75]
        xlabels = ['Jan', 'Feb', 'Mars']
    elif days_interval[1] == 180:
        xticks = [15, 45, 75]
        xlabels = ['April', 'Mai', 'Juni']
    elif days_interval[1] == 270:
        xticks = [15, 45, 75]
        xlabels = ['July', 'Aug', 'Sept']
    elif days_interval[0] == 270:
        xticks = [15, 45, 75]
        xlabels = ['Okt', 'Nov', 'Des']

    axNok.set_xticks(xticks)
    axNok.set_xticklabels(xlabels, color='white')

    axNok.tick_params(axis='y', colors='white')
    axNok.xaxis.label.set_color('white')
    axNok.yaxis.label.set_color('white')


# Main plot function
def plot_graph():
    axNok.cla()
    axBergen.cla()
    noxN = _nord_nox[days_interval[0]:days_interval[1]]
    noxK = _kron_nox[days_interval[0]:days_interval[1]]
    days = len(noxN)
    list_days = np.linspace(1, days, days)

    # Calculate the average of the two datasets
    nox_avg = [(noxN[i] + noxK[i]) / 2 for i in range(days)]

    # Draw the marked point & orange line
    l3 = None
    if marked_point != (0, 0):
        nox_point = [CalcPointValue(noxN[i], noxK[i]) for i in range(days)]
        l3, = axNok.plot(list_days, nox_point, color='darkorange', linewidth=2, alpha=0.9)
        circle = mpatches.Circle((marked_point[0], marked_point[1]), 50, color='orange', alpha=0.6)
        axBergen.add_patch(circle)

    # Main lines for Nordnes and Kronstad
    l1, = axNok.plot(list_days, noxN, color='#39FF14', linewidth=2, alpha=0.9, label='Nordnes')  # Neon Green
    l2, = axNok.plot(list_days, noxK, color='#FF3366', linewidth=2, alpha=0.9, label='Kronstad')  # Neon Pink

    # Plot the average line (Neon Blue for contrast)
    l_avg, = axNok.plot(list_days, nox_avg, color='#00FFFF', linestyle='--', linewidth=2, alpha=0.9, label='Gjennomsnitt')  # Neon Blue

    # Transparent fill for futuristic glow
    axNok.fill_between(list_days, noxN, color='#39FF14', alpha=0.2)  # Neon Green for fill
    axNok.fill_between(list_days, noxK, color='#FF3366', alpha=0.2)  # Neon Pink for fill

    # Set the background to black
    axNok.set_facecolor('black')
    axBergen.set_facecolor('black')
    axNok.figure.set_facecolor('black')

    # Set title and legend
    axNok.set_title("NOX verdier", color='white', fontsize=14)
    axInterval.set_title("Intervall", color='white', fontsize=12)

    # Legend showing Nordnes, Kronstad, and the Average
    lines = [l1, l2, l_avg] if l3 is None else [l1, l2, l_avg, l3]
    axNok.legend(lines, ["Nordnes", "Kronstad", "Gjennomsnitt", "Markert plass"] if l3 else ["Nordnes", "Kronstad", "Gjennomsnitt"],
                 facecolor='black', framealpha=0.8)

    axNok.grid(linestyle='--', color='white')
    draw_label_and_ticks()

    # Plot Map of Bergen
    axBergen.axis('off')
    img = mpimg.imread('map.jpg')
    axBergen.imshow(img)
    axBergen.set_title("Kart Bergen", color='white', fontsize=14)
    draw_circles_stations()
    plt.draw()


plot_graph()

# Create futuristic styled radio buttons for interval
listFonts = [14] * 5
listColors = ['#FF3366'] * 5
radio_button = RadioButtons(axInterval, ('År', '1. Kvartal', '2. Kvartal', '3. Kvartal', '4. Kvartal'),
                            label_props={'color': listColors, 'fontsize': listFonts},
                            radio_props={'facecolor': listColors, 'edgecolor': listColors})
axInterval.set_facecolor('#00FFFF')
radio_button.on_clicked(on_day_interval)

# Connect click event for map interaction
plt.connect('button_press_event', on_click)

plt.show()
