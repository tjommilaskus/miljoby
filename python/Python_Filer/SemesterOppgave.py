import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
from matplotlib.widgets import RectangleSelector
import random
from random import randint

# Generer tilfeldige data for et år
def GenereateRandomYearDataList(intencity: float, seed: int = 0) -> list[int]:
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

# Generer tilfeldig asfaltstøv data for et år

def generateRandomAsfaltstøvlist(intencity: float, seed: int = 0) -> list[int]:
    if seed != 0:
        random.seed(seed)

    centervals_alsfatstøv = [150, 130, 100, 80, 60, 50, 40, 50, 60, 90, 120, 150, 180]
    centervals_alsfatstøv = [x * intencity for x in centervals_alsfatstøv]
    
    asf = centervals_alsfatstøv[0]
    inc = True
    asfList = []

    for index in range(1, 365):
        if randint(1, 100) > 50:
            inc = not inc

        center = centervals_alsfatstøv[int(index / 30) % len(centervals_alsfatstøv)] 
        dx = min(2.0, max(0.5, asf / center))
        asf = asf + randint(1, 5) / dx if inc else asf - randint(1, 5) * dx
        asf = max(10, asf)
        asfList.append(asf)

    return asfList

# Data for NOx og Asfaltstøv
_kron_nox = GenereateRandomYearDataList(intencity=1.0, seed=2)
_nord_nox = GenereateRandomYearDataList(intencity=.3, seed=1)
_nygård_nox = GenereateRandomYearDataList(intencity=.5, seed=3)

_kron_asf = generateRandomAsfaltstøvlist(intencity=1.0, seed=2)
_nord_asf = generateRandomAsfaltstøvlist(intencity=.3, seed=1)
_nygård_asf = generateRandomAsfaltstøvlist(intencity=.5, seed=3)

# Initialiser figur og akser
fig = plt.figure(figsize=(13, 5))
axNok = fig.add_axes((0.05, 0.05, 0.45, 0.9))
axInterval = fig.add_axes((0.4, 0.05, 0.1, 0.25))
axBergen = fig.add_axes((0.5, 0.05, 0.5, 0.9))

coordinates_Nordnes = (400, 315)
coordinates_Kronstad = (1140, 1140)
coordinates_Nygård = (800, 800)
days_interval = (1, 365)
marked_point = (0, 0)
current_graph_type = 'NOx'  # Initialiser denne variabelen

# Funksjon for å håndtere intervallvalg
def on_day_interval(kvartal):
    global days_interval, marked_point
    if kvartal == '1. Kvartal':
        days_interval = (1, 90)
    elif kvartal == '2. Kvartal':
        days_interval = (90, 180)
    elif kvartal == '3. Kvartal':
        days_interval = (180, 270)
    elif kvartal == '4. Kvartal':
        days_interval = (270, 365)
    else:
        days_interval = (1, 365)
    marked_point = (0, 0)
    plot_graph()

# Funksjon for klikkehendelse på kartet
def on_click(event):
    global marked_point
    if event.inaxes == axBergen:
        marked_point = (event.xdata, event.ydata)
        plot_graph()

# Beregn punktverdi basert på avstander til stasjonene
def CalcPointValue(valNy, valK, valN):
    # Calculate distances between points
    distNygård = math.dist(coordinates_Nygård, marked_point)
    distKronstad = math.dist(coordinates_Kronstad, marked_point)
    distNordnes = math.dist(coordinates_Nordnes, marked_point)

    if distNygård == 0:
        return valNy
    if distKronstad == 0:
        return valK
    if distNordnes == 0:
        return valN


    inv_distNy = 1 / distNygård
    inv_distK = 1 / distKronstad
    inv_distN = 1 / distNordnes

    
    total_inv_dist = inv_distNy + inv_distK + inv_distN

  
    weighted_val = (inv_distNy * valNy + inv_distK * valK + inv_distN * valN) / total_inv_dist
    
    return weighted_val

# Tegn sirkler rundt stasjonene

def draw_circles_stations():
    circle = mpatches.Circle((coordinates_Nordnes), 50, color='blue')
    axBergen.add_patch(circle)
    circle = mpatches.Circle((coordinates_Kronstad), 50, color='red')
    axBergen.add_patch(circle)
    circle = mpatches.Circle((coordinates_Nygård), 50, color='green')
    axBergen.add_patch(circle)

# Tegn etiketter og ticks
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

# Plot grafen
def plot_graph():
    axNok.cla()
    axBergen.cla()

    if current_graph_type == 'NOx':
        asfN = _nord_nox[days_interval[0]:days_interval[1]]
        asfK = _kron_nox[days_interval[0]:days_interval[1]]
        asfNy = _nygård_nox[days_interval[0]:days_interval[1]]
        data_label = "NOx verdier"
    else:
        asfN = _nord_asf[days_interval[0]:days_interval[1]]
        asfK = _kron_asf[days_interval[0]:days_interval[1]]
        asfNy = _nygård_asf[days_interval[0]:days_interval[1]]
        data_label = "Asfaltstøv verdier"

    days = len(asfN)
    asfS = [(asfN[i] + asfK[i] + asfNy[i]) / 3 for i in range(days)]
   
    list_days = np.linspace(1, days, days)

    if marked_point != (0, 0):
        asf_point = [CalcPointValue(asfN[i], asfK[i], asfNy[i]) for i in range(days)]
        axNok.plot(list_days, asf_point, color='orange', linewidth=2, alpha=0.9, label='Markert')
        asfS = [(asfN[i] + asfK[i] + asfNy[i] + asf_point[i]) / 4 for i in range(days)]
        circle = mpatches.Circle((marked_point[0], marked_point[1]), 50, color='orange')
        axBergen.add_patch(circle)

    
    lineN, = axNok.plot(list_days, asfN, color='blue', linewidth=2, alpha=0.9, label='Nordnes')
    lineK, = axNok.plot(list_days, asfK, color='red', linewidth=2, alpha=0.9, label='Kronstad')
    lineNy, = axNok.plot(list_days, asfNy, color='green', linewidth=2, alpha=0.9, label='Nygård')
    lineS, = axNok.plot(list_days, asfS, color='cyan', linewidth=2, alpha=0.9, label='Gjennomsnitt')

    
    axNok.fill_between(list_days, asfN, color='blue', alpha=0.2)
    axNok.fill_between(list_days, asfK, color='red', alpha=0.2)
    axNok.fill_between(list_days, asfNy, color='green', alpha=0.2)
    axNok.fill_between(list_days, asfS, color='cyan', alpha=0.2)

    axNok.set_facecolor('#212946')
    axBergen.set_facecolor('#212946')
    axNok.figure.set_facecolor('#212946')

    axNok.set_title(data_label, color='0.9')
    axInterval.set_title("Intervall", color='0.9')

    
    axNok.legend(handles=[lineN, lineK, lineNy, lineS], loc="upper right")
    
    axNok.grid(linestyle='-', color='#2A3459', linewidth=0.6)
    draw_label_and_ticks()

    axBergen.axis('off')
    img = mpimg.imread('python/Python_Filer/map.jpg')
    axBergen.imshow(img)
    setfo = 'lightgrey'
    axBergen.set_title("Kart Bergen", color='lightgrey')
    draw_circles_stations()
    plt.draw()


plot_graph()

# Endre graf type basert på valg
def on_graph_type_change(label):
    global current_graph_type
    current_graph_type = label
    plot_graph()

# Oppførsel for RectangleSelector
def onselect(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"Start position: ({x1}, {y1})")
    print(f"End position: ({x2}, {y2})")
    print(f"Width: {abs(x2 - x1)}, Height: {abs(y2 - y1)}")

# Zoom function
def zoom(event):
    base_scale = 1.2  
    ax = event.inaxes  
    if ax is None:
        return  

    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()

    xdata = event.xdata
    ydata = event.ydata

    if event.button == 'up':  
        scale_factor = 1 / base_scale
    elif event.button == 'down':  
        scale_factor = base_scale
    else:
        return  

    new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
    new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

    relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
    rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

    ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * relx])
    ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * rely])

    ax.figure.canvas.draw() 

# Toggle selector
def toggle_selector(event):
    if event.key in ['Q', 'q'] and rect_selector.active:
        print('RectangleSelector deactivated.')
        rect_selector.set_active(False)
    elif event.key in ['A', 'a'] and not rect_selector.active:
        print('RectangleSelector activated.')
        rect_selector.set_active(True)

rect_selector = RectangleSelector(axBergen, onselect, interactive=True, button=[1], minspanx=5, minspany=5)

# Radio button for graph type selection
axGraphType = fig.add_axes((0.8, 0.7, 0.15, 0.2))
set_color = 'lighgrey'
radio_button_graph = RadioButtons(axGraphType, ('NOx', 'Asfaltstøv'),
                                   activecolor='green')
radio_button_graph.on_clicked(on_graph_type_change)

# Connect toggle selector, click, and zoom events
plt.connect('key_press_event', toggle_selector)
plt.connect('button_press_event', on_click)
plt.connect('scroll_event', zoom)

# Radio button for interval selection
listFonts = [12] * 5
listColors = ['yellow'] * 5
radio_button = RadioButtons(axInterval, ('År', '1. Kvartal', '2. Kvartal', '3. Kvartal', '4. Kvartal'),
                            label_props={'color': listColors, 'fontsize': listFonts},
                            radio_props={'facecolor': listColors, 'edgecolor': listColors})
axInterval.set_facecolor('#212946')
radio_button.on_clicked(on_day_interval)

# Show the plot with the selector enabled
plt.show()
