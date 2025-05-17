import numpy as np
import matplotlib.pyplot as plt
import re
x_points = np.array([-10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
user_input = input('Enter a quadratic equation (#x^2 + #x + #): ')
equation = list(user_input)
try:
    a = int(equation[0])
    b = int(equation[7])
    c = int(equation[12])
except IndexError:
    print('Invalid Response')
    quit()
try:
    y_points = a * x_points**2 + b * x_points + c
except ValueError:
    print('Invalid Response')
    quit()
plt.plot(x_points, y_points)
plt.grid()
plt.show()