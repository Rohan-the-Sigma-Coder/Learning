import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([x for x in range(10)])
ypoints = np.array([x for x in range(10)])
plt.pie(xpoints)
plt.show()