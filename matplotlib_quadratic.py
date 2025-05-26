import numpy as np
import matplotlib.pyplot as plt
import re
def parse_coeff(s):
        if s in (" ", "+"):
            return 1
        elif s == '-':
            return -1
        return int(s)
x_points = np.array(range(-10, 10), dtype=float)
user_input = input('Enter a quadratic equation (#x^2 + #x + #): ').replace(" ", "")
def quadratic(x_points, user_input):
    equation = list(user_input)
    match = re.fullmatch(r'([+-]?\d*)x\^2([+-]?\d*)x([+-]?\d+)', user_input)
    if not match:
        print('Invalid input. Enter in format ax^2 + bx + c')
        quit()
    a = parse_coeff(match.group(1))
    b = parse_coeff(match.group(2))
    c = int(match.group(3))
    return (a * x_points ** 2) + (b * x_points) + c



y_points = quadratic(x_points, user_input)
plt.plot(x_points, y_points)
plt.grid()
plt.show()