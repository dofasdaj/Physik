import numpy as np

def normalize(a):
    a = np.array(a)
    return a/np.linalg.norm(a)