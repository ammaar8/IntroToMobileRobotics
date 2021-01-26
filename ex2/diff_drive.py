import numpy as np


def diffdrive_naive(x, y, theta, v_l, v_r, t, l=0.5):
    v = (v_r + v_l) / 2
    omega = (v_r - v_l) / l

    x_n = x + v * np.cos(theta) * t
    y_n = y + v * np.sin(theta) * t
    theta_n = theta + omega * t
    return x_n, y_n, theta_n 


def diffdrive(x, y, theta, v_l, v_r, t, l=0.5):

    # Linear
    if (v_l == v_r):
        theta_n = theta
        x_n = x + v_l * np.cos(theta) * t
        y_n = y + v_l * np.sin(theta) * t
    # Curved
    else:
        # R - Radius of Curvature / Turning Radius
        # Ixx - Instantaneous Center of Rotation X coordinate
        # Iyy - Instantaneous Center of Rotation Y coordinate
        R = l / 2 * ((v_r + v_l) / (v_r - v_l)) 
        Ixx = x - R * np.sin(theta)
        Iyy = y + R * np.cos(theta)
        omega = (v_r - v_l) / l
        
        x_n = (x - Ixx) * np.cos(omega * t) - (y - Iyy) * np.sin(omega * t) + Ixx
        y_n = (x - Ixx) * np.sin(omega * t) + (y - Iyy) * np.cos(omega * t) + Iyy
        theta_n = theta + omega * t

    return x_n, y_n, theta_n

