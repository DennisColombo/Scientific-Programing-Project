from cmath import sin
from cmath import pi
from cmath import cos
from cmath import tan
from cmath import exp
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import numpy as np

# ***USE sp NOT np FOR SYMPY***

#plt.show (this shows the graph)
#plt.plot (this plots the points)
# x = np.arange(0,2(np.pi), 0.1) (creates the x coordinates which will be graphed)
# y = np.sin(x) (This calcualtes the y values, so just put our function in here)
# x-axis label -> plt.xlabel('WORDS GO HERE') (labels x-axis)
# frequency label -> plt.ylabel('OTHER WORDS GO HERE') (labels y-axis)
# plot title -> plt.title('EVEN MORE WORDS GO HERE') (creates a title)
# showing legend -> plt.legend() (displays all of those words)

z = np.arange(0, 2 * np.pi, 0.1) # This creates the x coordinates which will be graphed

f = np.sin(z) # This is the function which is actually graphed

x = sp.symbols('x') # This is the variable

y = sp.sin(x) # This is the function

y_prime = sp.diff(y, x) # This is the derivative of the function

y_prime_str = sp.printing.latex(y_prime) # This converts the derivative to a string

plt.plot(z, f) # Plots the points which we see on the graph

plt.xlabel('X-Axis') # Labels the x-axis

plt.ylabel('Y-Axis') # Labels the y-axis

plt.subplots_adjust(right=0.7) # This moves the graph to the right

plt.title('Graph') # The title

plt.legend() # This displays the legend, later on it will show which line is which (if there are multiple lines)

text_string = f'Derivative: ${y_prime_str}$' # Computes the derivative

plt.text(1.1, 0.5, text_string, fontsize=12, color='black', transform=plt.gca().transAxes) # Displays the derivative

plt.show() # This shows the graph

#Tasks for the day:
    # Figure out the derivative
    # Figure out text (and more importantly how to display the derivative to the side of the graph)

#Tasks for the future:
    # Figure out how to make the graph extend into infinity on both sides