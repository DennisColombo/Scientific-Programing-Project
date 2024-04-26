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
Xvalues = []

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
        Xvalues.append(x)
        Yint = vector[0]

coefficients = np.polyfit(Xvalues, vector, 1)

# The coefficients represent the slope and y-intercept of the line of best fit
slope, y_intercept = coefficients

rounded1 = round(slope, 4)
rounded2 = round(y_intercept, 4)

xline = np.linspace(min(Xvalues), max(Xvalues), len(Xvalues))

yline = slope * xline + y_intercept

plt.plot(xline, yline, color='red', label='Line of best fit')

textString = f"The line of best fit is y = {rounded1} * x + {rounded2}"

plt.text(1.1, 0.5, textString, color='black', transform=plt.gca().transAxes)

plt.xlabel('Time (milliseconds)')

plt.ylabel('Distance (centimeters)')

plt.title('Rangefinder data')

plt.subplots_adjust(right=0.7)

plt.legend()

plt.show()