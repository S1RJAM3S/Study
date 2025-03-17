import math
import numpy as np

def vector_distance(v1, v2, **kwargs):
  v1 = np.array(v1)
  v2 = np.array(v2)
  norm = kwargs['norm']
  if (norm == 'manhattan'): return np.sum(np.abs(v1 - v2))
  elif (norm == 'cosine'): return round(1 - (np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))), 9)
  else: return round(np.linalg.norm(v1 - v2), 9)
print(vector_distance([1, 2], [4, 6], norm='manhattan'))