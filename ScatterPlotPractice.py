from cmath import sin
from cmath import pi
from cmath import cos
from cmath import tan
from cmath import exp
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

plt.subplots_adjust(right=0.7)

plt.xlabel('X-Axis')

plt.ylabel('Y-Axis')

plt.subplots_adjust(right=0.7)

plt.title('Scatter Plot Practice')

plt.legend()

# Note: np.random.uniform(a, b, c) generates c random numbers between a and b

x = np.random.uniform(-10, 10, 100)
import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.random.uniform(-10, 10, 100)
y = 3 * x + 2 + np.random.normal(0, 5, 100)  # y = 3x + 2 + noise

# Calculate the coefficients of the line of best fit
coefficients = np.polyfit(x, y, 1)

# Create a function that represents the line of best fit
line_of_best_fit = np.poly1d(coefficients)

# Generate some x values for the line of best fit
x_values_for_line = np.linspace(-10, 10, 100)

plt.plot(x_values_for_line, line_of_best_fit(x_values_for_line), color='red', label='Line of best fit')

y = np.random.uniform(-10, 10, 100)

plt.scatter(x, y, c = "blue")

text_string = f'Line of Best Fit: {line_of_best_fit}'

# Calculate the derivative of the line of best fit
line_of_best_fit_derivative = line_of_best_fit.deriv()

# Convert the derivative to a string
line_of_best_fit_derivative_str = str(line_of_best_fit_derivative)

text_string2 = f'Derivative of Best Fit: {line_of_best_fit_derivative_str}'

print(text_string2)

plt.text(1.1, 0.5, text_string + '\n' + text_string2, fontsize=12, color='black', transform=plt.gca().transAxes)

plt.show()