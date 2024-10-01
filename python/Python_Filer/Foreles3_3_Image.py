#Plot Map of Bergen
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig = plt.figure(figsize=(6,5))
axBergen = fig.add_axes((0.1, 0.1, 0.2, 0.20))
axBergen2 = fig.add_axes((0.3, 0.3, 0.6, 0.60))

axBergen.axis('off')
axBergen.set_title("Kart Bergen")

img = mpimg.imread('Bergen.jpg')
axBergen.imshow(img)
axBergen2.imshow(img)
axBergen2.axis('off')
axBergen2.set_title("Stort Kart Bergen")

plt.show()