import numpy as np

def convert(a):
    return a / a.sum(axis = 1, keepdims = True)