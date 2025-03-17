from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from sympy.ntheory.residue_ntheory import discrete_log
from sympy.ntheory.modular import crt
from hashlib import sha256
import os

FLAG = "TEST_TIME".encode()

g = 5
p = getStrongPrime(1024)

class Server:
    def __init__(self):
        self.p = p
        self.secret = bytes_to_long(os.urandom(128)) 
        self.A = pow(g, self.secret, self.p)

    def dh_hex(self, B, p = None):
        if p != None:
            self.p = p
        shared_secret = pow(B, self.secret, self.p)
        self.shared_key = sha256(str(shared_secret).encode()).digest()[:16]

    def send_msg(self, pt):
        iv = os.urandom(16)
        cipher = AES.new(self.shared_key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(pad(pt,16))

client_secret_key = bytes_to_long(os.urandom(128))
cpk = pow(g, client_secret_key, p)
s = Server()
s.dh_hex(cpk)
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
    
spk = s.A
flag_enc = str(s.send_msg(FLAG).hex())
sp = smooth_p()
spk_list = []
test_list = []
gen_list = []
for x in div_list:
    s.dh_hex(pow(g,(sp-1)//x, sp), sp)
    test_list.append(s.send_msg(b"Shynt_is_my_son_").hex())

print("done")    
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
print(decrypt_text(int(flag_enc, 16), shared).decode())