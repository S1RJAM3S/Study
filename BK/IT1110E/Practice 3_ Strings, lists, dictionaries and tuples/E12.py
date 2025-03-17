from collections import Counter

def merge_dict(d1, d2):
    return dict(Counter(d1) + Counter(d2))