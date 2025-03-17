from Crypto.Util.number import long_to_bytes

e = 65537
n = 3367854845750390371489
c = 2542377158923381875170

p = 49450786403
q = 68105182763
PHI = (p - 1) * (q - 1)
d = pow(e, -1, PHI)
print(long_to_bytes(pow(c, d, n)).decode())