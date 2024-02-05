from cmath import sin
from cmath import pi
from cmath import cos
from cmath import tan
from cmath import exp
import matplotlib.pyplot as plt
import numpy as np
#plt.show (this shows the graph)
#plt.plot (this plots the points)
# x = np.arange(0,2(np.pi), 0.1) (creates the x coordinates which will be graphed)
# y = np.sin(x) (This calcualtes the y values, so just put our function in here)
# x-axis label -> plt.xlabel('WORDS GO HERE') (labels x-axis)
# frequency label -> plt.ylabel('OTHER WORDS GO HERE') (labels y-axis)
# plot title -> plt.title('EVEN MORE WORDS GO HERE') (creates a title)
# showing legend -> plt.legend() (displays all of those words)

x = np.arange(0, 2*(np.pi), 0.1)

y = np.sin(x)

dx = 0.1  # Define the value of dx

z = np.gradient(y, dx)  # Calculate the gradient using np.gradient

plt.plot(x, z)

plt.plot(x, y)

plt.xlabel('X-Axis') 

plt.ylabel('Y-Axis')

plt.title('Graph')

plt.legend()

plt.show()