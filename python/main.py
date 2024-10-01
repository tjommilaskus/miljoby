import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [2,4,1,4,6,4,5,4,3,2,4,4,]

plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Iox ')

# function to show the plot
plt.show()
