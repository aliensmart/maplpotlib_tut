"""
    matplotlib.pyplot is a python package used for 2D graphics
"""


import matplotlib.pyplot as plt 

x = [5, 10, 2]
y = [19, 1, 6]

plt.plot(x, y)
plt.title('info')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()