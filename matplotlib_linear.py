import matplotlib.pyplot as plt
import numpy as np
import time
import re
try:
    user_input = input("Enter a linear equation in the form of '#x + #' (with spaces): ")
    user_input_list = user_input.split()
except IndexError:
    print('Invalid response')
xpoints = np.array([0, 10])
alpha_list = ['a', 'b', 'c', 'd', 'e' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def linear(alpha_list, user_input, xpoints):

    slope_term = user_input_list[0]
    match = re.match(r"(-?\d+)([a-zA-Z])", slope_term)

    if not match or match.group(2) not in alpha_list:
        print("Invalid format for slope")
        quit()

    slope = int(match.group(1))

    try:
        sign = user_input_list[1]
        intercept = int(user_input_list[2])
        y_intercept = -intercept if sign == '-' else intercept
    except (IndexError, ValueError):
        print("Invalid y-intercept format")
        quit()

    return slope * xpoints + y_intercept



ypoints = linear(alpha_list, user_input, xpoints)
plt.plot(xpoints, ypoints)
print('Generating graph...')
time.sleep(1)
plt.xlabel('x-axis', color = 'r')
plt.ylabel('y-axis', color = 'r')
plt.title('Linear Graph', color = 'b')
plt.grid()
plt.show()


