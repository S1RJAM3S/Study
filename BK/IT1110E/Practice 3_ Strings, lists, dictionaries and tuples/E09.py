def transform(l):
  return list(map(lambda x: -x if x%2 else 2*x, l))