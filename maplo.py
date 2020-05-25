"""
    matplotlib.pyplot is a python package used for 2D graphics
"""

import matplotlib.pyplot as plt 
from maplotlib import style

#x = [5, 10, 2]
#y = [19, 1, 6]

#plt.plot(x, y)
#plt.title('info')
#plt.xlabel('X axis')
#plt.ylabel('Y axis')
#plt.show()

#adding style

x1 = [5, 10, 2]
y1 = [19, 1, 6]

x2 = [6, 1, 2]
y2 = [20, 6, 10]

plt.plot(x1, y1, 'g', label='line 1', linewidth=5)
plt.plot(x2, y2, 'c', label='line 2', linewidth=5)
plt.title('info')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True,color='k')
plt.show()
