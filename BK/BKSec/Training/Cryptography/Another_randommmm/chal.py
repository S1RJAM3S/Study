from Crypto.Util.number import long_to_bytes
import random
from hashlib import sha256

rng = random.Random()
FLAG = 'BKSEC{' + sha256(long_to_bytes(rng.getrandbits(1024))).hexdigest() + '}'
leak = [rng.getrandbits(1024) for i in range(20)]

with open('leak.txt', 'w') as f:
    f.write(str(leak) + '\n')

