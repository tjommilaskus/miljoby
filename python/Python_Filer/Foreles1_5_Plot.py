
import matplotlib.pyplot as plt

x = list(range(1,50))
y = [n*n for n in x]

fig = plt.figure(figsize=(13, 6))
axis = fig.add_axes((.1, .1, .8, .8))
axis.plot(x, y)
plt.show()

