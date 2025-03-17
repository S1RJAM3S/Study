from Crypto.Util.number import *

flag = b'BKSEC{REDACTED}'

p = getPrime(512)
q = getPrime(512)
hint = (p + 1)*getPrime(512)
n = p * q
e = 65537

c = pow(bytes_to_long(flag),e,n)

print('c =',c)
print('n =',n)
print('hint = ',hint)