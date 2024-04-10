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
plt.xlabel('Time (milliseconds)')

plt.ylabel('Distance (centimeters)')

plt.title('Rangefinder data')

plt.legend()

plt.show()