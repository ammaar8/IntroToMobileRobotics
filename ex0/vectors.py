import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng


rng = default_rng(1000)

def myFunction(x):
    return math.cos(x) * math.exp(x)

x = np.linspace(- 2 * np.pi, 2 * np.pi, 50, True)
y = list(map(myFunction, x))

sd_vector = rng.normal(5.0, 2.0, (100000))
uniform_vector = rng.integers(0, 10, (100000))

plt.hist(sd_vector, bins=101)
plt.show()