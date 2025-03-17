from Crypto.Util.number import *
from hashlib import sha256
import os 
import signal
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

FLAG = os.environ.get("FLAG", "BKSEC{???????}").encode()

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
    



if __name__ == '__main__':
    client_secret_key = bytes_to_long(os.urandom(128))
    client_public_key = pow(g, client_secret_key, p)
    s = Server()
    s.dh_hex(client_public_key)
    print(
        f"Eavesdropping...\n"
        f"client initiating key agreement:\n"
        f'Public key: {hex(p)}\n'
        f"client->server: {hex(client_public_key)}\n"
        f"server->client: {hex(s.A)}\n"
        f"server->client: {s.send_msg(FLAG).hex()}"
    )

    signal.alarm(100)
    while True:
        print(
            "Your illegal choices:\n"
            "1. New DH\n"
            "2. Test connectiong\n"
            "3. Exit\n"
            ">", end=" "
        )

        choice = int(input())
        if choice == 1:
            B = int(input(),16)
            new_p = int(input(),16)
            s.dh_hex(B, new_p)
        elif choice == 2:
            print(s.send_msg(b"Shynt_is_my_son_").hex())
        else:
            break
