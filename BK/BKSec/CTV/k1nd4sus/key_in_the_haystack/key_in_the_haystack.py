from Crypto.Util import number
from base64 import b64decode
from sympy import symbols, Poly, real_roots

# Decode base64 to integer
def b64dec(s):
    return int.from_bytes(b64decode(s), byteorder='big')

# Given stack (replace with actual base64 values from the output)
stack_b64 = []
with open("D:\\Study\\BK\\BKSec\\CTV\\k1nd4sus\\key_in_the_haystack\\output.txt", 'r') as f:
    for line in f.readlines():
        stack_b64.append(line.strip())

# Decode the stack
stack = [b64dec(x) for x in stack_b64]

x = symbols('x')
coefficients = stack[::-1]  # Coefficients are already in ascending order
poly = Poly(coefficients, x)

# Find the real roots of the polynomial
roots = real_roots(poly)

# The roots are p, q, r1, r2, ..., r64
# Since p and q are 512-bit primes, they will be the largest roots.

# Sort the roots and select the two largest (p and q)
roots_sorted = sorted(roots, reverse=True)
p = roots_sorted[0]
q = roots_sorted[1]

# Verify p and q
# Check if p and q are primes (using a probabilistic primality test)
if number.isPrime(p) and number.isPrime(q):
    print("p:", p)
    print("q:", q)
else:
    print("Failed to find valid primes. Try a more precise root-finding method.")