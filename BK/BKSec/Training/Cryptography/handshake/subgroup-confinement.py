from pwn import *
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from sympy.ntheory.residue_ntheory import discrete_log
from sympy.ntheory.modular import crt
from hashlib import sha256

r = remote('15.235.162.115', 9999)

div_list = []
def smooth_p():
    mul = 1
    i = 2
    while True:
        if isPrime(i):
            mul *= i
            div_list.append(i)
        if ((mul + 1).bit_length() >= p.bit_length() and isPrime(mul + 1)):
            return mul + 1
        i += 1

def decrypt_text(ct_hex, shared_key):
    ct = long_to_bytes(ct_hex)
    iv = ct[:16]
    ct = ct[16:]
    cipher = AES.new(shared_key, AES.MODE_CBC, iv)
    try:
        return unpad(cipher.decrypt(ct), 16)
    except:
        return None

r.recvuntil("Public key: 0x")
p = int(r.recvline(keepends=False), 16)
r.recvuntil("client->server: 0x")
cpk = int(r.recvline(keepends=False), 16)
r.recvuntil("server->client: 0x")
spk = int(r.recvline(keepends=False), 16)
r.recvuntil("server->client: ")
flag_enc = int(r.recvline(keepends=False), 16)
print(flag_enc)

sp = smooth_p()
spk_list = []
test_list = []
gen_list = []
g = getPrime(12)
for x in div_list:
    r.recvuntil("> ")
    r.sendline("1")
    r.sendline(str(hex(pow(g,(sp-1)//x, sp))))
    r.sendline(str(hex(sp)))
    r.recvuntil("> ")
    r.send("2\n")
    print(x)
    test_list.append(r.recvline(keepends=False))
print("ran")
for i in range(len(div_list)):
    x = div_list[i]
    test = test_list[i]
    gen = pow(g, ((sp - 1)//div_list[i]), sp)
    a = 1
    while True:
        S1 = pow(gen, a, sp)
        shared_key = sha256(str(S1).encode()).digest()[:16]
        pt = decrypt_text(int(test, 16), shared_key)
        if pt and b"Shynt_is_my_son_" in pt:
            print(pt.decode())
            spk_list.append(a) 
            break
        a += 1

c = crt(div_list, spk_list)[0]
print(pow(5, c, p) - spk)
shared = sha256(str(pow(cpk, c, p)).encode()).digest()[:16]
print(decrypt_text(flag_enc, shared).decode())
