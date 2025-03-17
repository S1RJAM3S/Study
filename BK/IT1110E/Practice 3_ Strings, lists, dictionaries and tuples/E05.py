from itertools import zip_longest

def remove_duplicates(l):
  return [curr for curr, next in zip_longest(l, l[1:]) if curr != next]