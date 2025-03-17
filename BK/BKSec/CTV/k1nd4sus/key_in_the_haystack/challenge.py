from Crypto.Util import number
from base64 import b64encode

prime = lambda: number.getPrime(512)
def b64enc(x):
	h = hex(x)[2:]
	if len(h) % 2:
		h = '0' + h
	return b64encode(bytes.fromhex(h)).decode()


p = prime()
q = prime()
with open("flag.txt") as f:
	flag = f.readline().strip()

n = p * q
m = int(flag.encode().hex(), 16)
c = pow(m, 65537, n)

print("ciphertext:", hex(c)[2:])

bale = [p, q]
bale.extend(prime() for _ in range(1<<6))

def add_hay(stack, straw):
	x = stack[0]
	for i in range(1, len(stack)):
		y = stack[i]
		stack[i] = y + (straw * x)
		x = y
	stack.append(straw * x)

stack = [1]
add_hay(stack, p)
add_hay(stack, q)
for straw in bale:
	add_hay(stack, straw)

print("size:", len(stack))
for x in stack:
	print(b64enc(x))
