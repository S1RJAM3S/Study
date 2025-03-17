from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
from hashlib import sha256


flag = 'BKSEC{REDACTED}'
deg = 512

def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])

coeffs = [random.getrandbits(64) for _ in range(deg + 1)]

shares = []
for _ in range(5):
    x = random.getrandbits(16)
    shares.append((x,polyeval(coeffs,x)))

secret = polyeval(coeffs,0x31104)
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)

c = cipher.encrypt(pad(flag.encode(),16)).hex()

with open("output.txt", "w") as f:
    f.write(f"shares = {shares}\n")
    f.write(f"c = \"{c}\"\n")



