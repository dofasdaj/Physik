import numpy as np

def normalize(a):
    a = np.array(a)
    return a/np.linalg.norm(a)

def add_vectors(a,b):
    c = (a[0]+b[0], a[1]+b[1])
    return c
