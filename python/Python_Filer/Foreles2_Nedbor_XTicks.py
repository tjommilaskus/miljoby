from random import randint

import matplotlib.pyplot as py
import numpy as np
from mpl_toolkits.axes_grid1.axes_size import AxesX

mnd = np.linspace(1,365,12)
nedbor = [randint(150,450) for t in mnd]

fig = py.figure(figsize=(10,4))
ax = fig.add_subplot()
ax.plot(mnd, nedbor)

labels = ['J','F','M','A','M','J', 'J', 'A', 'S', 'O', 'N', 'D']
xticks =np.linspace(10, 340, len(labels))
ax.set_xticks(xticks)
ax.set_xticklabels(labels)
ax.set_title('Nedbør i Bergen (per mnd)')

py.show()