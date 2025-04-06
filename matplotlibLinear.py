import matplotlib.pyplot as plt
import numpy as np
import time
alpha_list = ['a', 'b', 'c', 'd', 'e' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
try:
    user_input = input('Enter linear equation in the form of (-)#variable (+ or -) #, use spaces: ')
    user_input_list = user_input.split()
except IndexError:
    print('Invalid response')
coefficient = list(user_input_list[0])

if coefficient[0] == '-':
    if coefficient[2] not in alpha_list:
        print('Invalid response')
        quit()
else:
    if coefficient[1] not in alpha_list:
        print('Invalid response')
        quit()
y_intercept = user_input_list[1] + user_input_list[2]
graph_yint = -1 * int(y_intercept[1]) if y_intercept[0] == '-' else int(y_intercept)
xpoints = np.array([0, 1])
ypoints = np.array([graph_yint, graph_yint + int(coefficient[0]) if coefficient[0] is not '-' else graph_yint + -1 * int(coefficient[1])])
plt.plot(xpoints, ypoints)
timer = 3
for x in range(3):
    print(f'Generating graph in {timer}')
    time.sleep(1)
    timer -= 1
plt.show()


