import matplotlib_linear
import matplotlib_quadratic
from matplotlib_linear import linear
from matplotlib_quadratic import quadratic
from matplotlib_quadratic import parse_coeff
import matplotlib.pyplot as plt
import numpy as np
import time
import re
xpoints_linear = np.array([0, 10])
xpoints_quadratic = np.array(range(-10, 10), dtype=float)
alpha_list = ['a', 'b', 'c', 'd', 'e' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
user_input = input('Enter either a linear (#x + #) or quadratic (#x^2 + #x + #) equation').replace(" ", "")
equation = list(user_input)
equation_type = re.findall('x', user_input)
if len(equation_type) == 2:
    quadratic(xpoints_quadratic, equation)
    y_points = quadratic(xpoints_quadratic, equation)
    plt.plot(xpoints_quadratic, y_points)
    plt.xlabel('x-axis', color = 'r')
    plt.ylabel('y-axis', color = 'r')
    plt.title('Quadratic Graph', color = 'b')
    plt.grid()
    plt.show()
elif len(equation_type) == 1:
    linear(xpoints_linear, alpha_list, user_input)
    ypoints = linear(alpha_list, user_input, xpoints_linear)
    plt.plot(xpoints_linear, ypoints)
    timer = 3
    for x in range(3):
        print(f'Generating graph in {timer}')
        time.sleep(1)
        timer -= 1
    plt.xlabel('x-axis', color = 'r')
    plt.ylabel('y-axis', color = 'r')
    plt.title('Linear Graph', color = 'b')
    plt.grid()
    plt.show()
