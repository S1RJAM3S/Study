import numpy as np

def system_solver(a):
    return np.linalg.solve(a[:, :-1], a[:, -1])