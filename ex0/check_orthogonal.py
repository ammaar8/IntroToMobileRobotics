import numpy as np
import math


def check_orthogonal(M):
    if (len(M.shape) != 2):
        print("Not a Matrix")
        return False

    if (M.shape[0] != M.shape[1]):
        print("Not a square matrix")
        return False
    A = np.dot(M, M.T)
    if np.allclose(A, np.identity(M.shape[0])):
        return True
    else:
        return False


D = 1./3.*np.array([[2, 2, -1],[2, -1, 2],[-1, 2, 2]])  
print(check_orthogonal(D))