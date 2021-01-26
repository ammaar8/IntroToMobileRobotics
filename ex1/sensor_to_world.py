import numpy as np
import matplotlib.pyplot as plt
import math
pi = math.pi
scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-pi/2, pi/2, np.shape(scan)[0], endpoint=True)



def transform_matrix(tx, ty, angle):
    T = np.array([
        [np.cos(angle), -np.sin(angle), tx],
        [np.sin(angle), np.cos(angle), ty],
        [0, 0, 1],
    ])
    return T

x = scan * np.cos(angle)
y = scan * np.sin(angle)
ones = np.ones(np.shape(angle)[0])

T_global_robot = transform_matrix(1, 0.5, math.pi/4)
T_robot_laser = transform_matrix(0.2, 0, 0)
T_global_laser = np.dot(T_global_robot, T_robot_laser)

scan_laser = np.array([x, y, ones])
scan_global = np.dot(T_global_laser, scan_laser)

plt.figure()

plt.plot(scan_global[0], scan_global[1], '.k', markersize=3)
plt.plot(T_global_robot[0,2], T_global_robot[1, 2], "+r")
plt.plot(T_global_laser[0,2], T_global_laser[1, 2], "+g")
plt.gca().set_aspect('equal')
plt.savefig('scan2.pdf')
plt.show()
