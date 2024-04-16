from cmath import sin
from cmath import pi
from cmath import cos
from cmath import tan
from cmath import exp
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

# scp pi@10.10.71.136:Documents/output.txt /Users/denniscolombo/git/Scientific-Programing-Project
    # Remember the IP Address is wrong!

vector = []

# Open the file in read mode ('r')
with open('output.txt', 'r') as f:
    # Read the file line by line
    start = float(f.readline().split('\t')[1]) # the first millisecond
    for line in f:
        # Convert the line to a number and append it to the list
        data = line.split('\t')
        number = float(data[0])
        ms = float(data[1])
        vector.append(number)
        x = ms - start
        y = number
        plt.scatter(x, y, c = "blue")

coefficients = np.polyfit(range(len(vector)), vector, 1)

line_of_best_fit = np.poly1d(coefficients)

x_values_for_line = range(len(vector))

polynomial = np.poly1d(coefficients)

derivative = polynomial.deriv()

derivative_str = str(derivative)

print('Derivative: ' + derivative_str)

plt.plot(x_values_for_line, line_of_best_fit(x_values_for_line), color='red', label='Line of best fit')

plt.xlabel('Time (milliseconds)')

plt.ylabel('Distance (centimeters)')

plt.title('Rangefinder data')

plt.subplots_adjust(right=0.7)

plt.legend()

plt.show()