from sympy.ntheory.modular import crt
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes
from itertools import combinations
import os

PATH = os.path.dirname(os.path.abspath(__file__))
n_list = []
c_list = []
e = 3
with open(PATH + "\\" + "output_0ef6d6343784e59e2f44f61d2d29896f.txt", 'r') as f:
    for line in f.readlines():
        if 'n' in line:
            n_list.append(int(line[4:]))
        if 'c' in line:
            c_list.append(int(line[4:]))

for (n_1, c_1), (n_2, c_2), (n_3, c_3) in combinations(zip(n_list, c_list), 3):
    try:
        ct = crt([n_1, n_2, n_3], [c_1, c_2, c_3])[0]
        pt = iroot(ct, e)[0]
        print(long_to_bytes(pt).decode())
    except:
        continue