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
#x1 = [5, 10, 2]
#y1 = [19, 1, 6]
#
#x2 = [6, 1, 2]
#y2 = [20, 6, 10]
#
#plt.plot(x1, y1, 'g', label='line 1', linewidth=5)
#plt.plot(x2, y2, 'c', label='line 2', linewidth=5)
#plt.title('info')
#plt.xlabel('X axis')
#plt.ylabel('Y axis')
#plt.legend()
#plt.grid(True,color='k')
#plt.show()

#Bar Graph
x1 = [0.25,1.25,2.25,3.25,4.25]
height1 = [50,40,70,80,20]

x2 = [.75,1.75,2.75,3.75,4.75]
height2 = [80,20,20,50,60]
plt.bar(x1, height1, width=.5, label="BMW")
plt.bar(x2, height2, width=.5, label="Audit")
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance(kms)')
plt.title('Information')
plt.show()


