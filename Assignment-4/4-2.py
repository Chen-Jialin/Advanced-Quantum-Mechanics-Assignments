import numpy as np
import matplotlib.pyplot as plt

x_1 = np.linspace(-10, -1, 1000)
psi_1 = 2 / (-10 * x_1 + 16)**0.25 * np.cos(0.4 * x_1**2)
plt.plot(x_1, psi_1, 'k')
x_2 = np.linspace(1, 10, 1000)
psi_2 = np.exp(-x_2)
plt.plot(x_2, psi_2, 'k')
plt.plot()
plt.show()