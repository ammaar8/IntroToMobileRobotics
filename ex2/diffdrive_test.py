import numpy as np
import matplotlib.pyplot as plt
from diff_drive import diffdrive, diffdrive_naive

# (v_l, v_r, t)
commands = [(0.3, 0.3, 3), (0.1, -0.1, 1), (0.2, 0, 2)]

# Initial Pose DiffDrive
x, y, theta = 1.5, 2, np.pi/2

plt.subplot(1, 2, 1)

plt.title("DiffDrive")
plt.scatter(x, y)
plt.quiver(x, y, np.cos(theta), np.sin(theta))

for v_l, v_r, t in commands:

    x, y, theta = diffdrive(x, y, theta, v_l, v_r, t)
    plt.scatter(x, y)
    plt.quiver(x, y, np.cos(theta), np.sin(theta))

plt.gca().set_aspect('equal')
plt.xlim([0.5, 2.5])
plt.ylim([1.5, 3.5])

# Initial Pose DiffDrive Naive

x, y, theta = 1.5, 2, np.pi/2

plt.subplot(1, 2, 2)

plt.title("DiffDrive Naive")
plt.scatter(x, y)
plt.quiver(x, y, np.cos(theta), np.sin(theta))

for v_l, v_r, t in commands:

    x, y, theta = diffdrive_naive(x, y, theta, v_l, v_r, t)
    plt.scatter(x, y)
    plt.quiver(x, y, np.cos(theta), np.sin(theta))

plt.gca().set_aspect('equal')
plt.xlim([0.5, 2.5])
plt.ylim([1.5, 3.5])

plt.show()
