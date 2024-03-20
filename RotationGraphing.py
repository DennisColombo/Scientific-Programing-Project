from cmath import sin
from cmath import pi
from cmath import cos
from cmath import tan
from cmath import exp
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

#To get the data I need to run the command below in the terminal to get the latest version of output.txt (CONTINUES ON NEXT LINE)
#into the project folder, and do note that the file named output.txt in the project will update automatically

# '%Y-%m-%d %H:%M:%S' <- This is the format for the time stamp

#This is where I process all the data I get from the raspberry pi
#IMPORTANT: scp pi@10.10.71.136:Documents/output.txt /Users/denniscolombo/git/Scientific-Programing-Project (Use this in terminal)
#Remember the password is robots1234

# When I start collecting more complex data I will need:
    #Derivative calculator / display function
    #Line of best fit calculator / display function

plt.subplots_adjust(right=0.7)

plt.xlabel('Time (Milliseconds)')

plt.ylabel('Y-Axis (Degrees)')

plt.title('Data')

plt.legend()

# Initialize empty lists
vector = []
x_values = []

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
        x_values.append(x)

# Calculate the coefficients of the line of best fit
coefficients = np.polyfit(x_values, vector, 1) # 1 is the degree of the polynomial (the one makes it linear)

# Create a function that represents the line of best fit
line_of_best_fit = np.poly1d(coefficients)

# Generate some x values for the line of best fit
x_values_for_line = np.linspace(0, x_values[-1], len(x_values))

# Plot the line of best fit
plt.plot(x_values_for_line, line_of_best_fit(x_values_for_line), color='red')

# Derivative of line of best fit
line_of_best_fit_derivative = line_of_best_fit.deriv()

# Displays values for line of best fit and its derivative
text_string = f'Line of Best Fit: {line_of_best_fit}'
text_string2 = f'Derivative of Best Fit: {line_of_best_fit_derivative}'
plt.text(1.1, 0.5, text_string + '\n' + text_string2, fontsize=12, color='black', transform=plt.gca().transAxes)

plt.show()

#Display Sensor:
    #Display the data from the sensor on the screen:

    #Button toggle function (most likely will use a counter to make it work):