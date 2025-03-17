from Crypto.Util.number import *
from sage.all import *
import os

proof.arithmetic(False)  # to make sage faster

flag = b"BKSEC{REDACTED}"

p = getPrime(1024)
q = getPrime(512)
n = p * q
e = 65537
E = EllipticCurve(Zmod(n), [p, q])

while True:
    x = ZZ(bytes_to_long(flag + os.urandom(192 - len(flag))))
    try:
        yp = ZZ(E.change_ring(GF(p)).lift_x(x).xy()[1])
        yq = ZZ(E.change_ring(GF(q)).lift_x(x).xy()[1])
        y = crt([yp, yq], [p, q])
        break
    except:
        pass

C = e * E(x, y)
with open('output.txt','w') as f:
    f.write(f'n = {n}\n')
    f.write(f'C = {C.xy()}\n')
