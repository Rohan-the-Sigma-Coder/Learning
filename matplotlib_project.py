import matplotlib.pyplot as plt
import numpy as np
import time
import re
equation_type = input("Which equation type do you want? (type 'Q' for quadratic or 'L' for linear): ")
if equation_type.upper() == 'Q':
    import matplotlib_quadratic
elif equation_type.upper() == 'L':
    import matplotlib_linear
else:
    print('Invalid Input')
    quit()