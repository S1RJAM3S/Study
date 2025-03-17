from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad, unpad
import random
import os


FLAG = b'siuuuuuuuuuuuuuuuuuuu'

def encAES(msg, key, iv, mode):
    if(mode == AES.MODE_ECB):
        cipher = AES.new(key, mode)
    elif(mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]):
        cipher = AES.new(key, mode, iv=iv)
    elif(mode in [AES.MODE_EAX, AES.MODE_GCM, AES.MODE_SIV]):
        cipher = AES.new(key, mode, nonce=iv)
    else:
        cipher = AES.new(key, AES.MODE_CTR, nonce=iv[:8])
    enc = cipher.encrypt(msg)

    return enc

def decAES(enc, key, iv, mode):
    if(mode == AES.MODE_ECB):
        cipher = AES.new(key, mode)
    elif(mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]):
        cipher = AES.new(key, mode, iv=iv)
    elif(mode in [AES.MODE_EAX, AES.MODE_GCM]):
        cipher = AES.new(key, mode, nonce=iv)
    else:
        cipher = AES.new(key, AES.MODE_CTR, nonce=iv[:8])

    msg = cipher.decrypt(enc)
    return msg

def encTripleAES(msg: bytes, key, mode: list, iv: bytes):
    enc = encAES(pad(msg, 16), key, iv, mode[0])
    enc = encAES(enc, key, iv, mode[1])
    enc = decAES(enc, key, iv, mode[2])
    return enc



def challenge():
    key = os.urandom(16)
    all_mode_options = [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_CTR, AES.MODE_EAX, AES.MODE_ECB, AES.MODE_GCM, AES.MODE_OFB]

    print('I have learned 3DES and AES, let\'t combine it into 3AES-ish!\nYou can encrypt message here or get my encrypted super secret...')
    while(True):
        print('Choose your option:\n> 1. Encrypt message\n> 2.Get secret\n> 3.Quit')

        try:
            option = int(input())
            if(option == 1):
                print('Choose 3 modes to encrypt s.t. mode2 != mode3. Ex: 1 2 3:')
                print('> 1. CBC\n> 2. CFB\n> 3. CTR\n> 4. EAX\n> 5. ECB\n> 6. GCM\n> 7. OFB')

                options = [int(i) if (int(i) > 0 and int(i) <= 7) else -1 for i in input().split()]
                if(-1 in options or len(options) != 3):
                    print('Invalid option.')
                    continue

                mode = [all_mode_options[i-1] for i in options]
                print('Enter your iv (hex) or None: ')
                iv = input().strip()
                if(iv == 'None'):
                    iv = os.urandom(16)
                else:
                    iv = bytes.fromhex(iv)
                print('Enter your text (hex): ')
                
                hex_msg = input()
                msg = bytes.fromhex(hex_msg)
                enc = encTripleAES(msg, key, mode, iv)
                print(f'> iv = {iv.hex()}')
                print(f'> enc = {enc.hex()}')
                print(f'> mode = {options}')

            elif(option == 2):
                iv = os.urandom(16)
                options = random.sample(range(1,8), 3) 
                mode = [all_mode_options[i-1] for i in options]

                flag_enc = encTripleAES(FLAG, key, mode, iv)
                print(f'> hex_enc = {flag_enc.hex()}')
                print(f'> iv = {iv.hex()}')
                print(f'> mode = {options}')

            elif(option == 3):
                print('Bye bye!')
                return
            
            else:
                print('Invalid option.')
        except:

            print('Hmm... 500 - Internal Server Error')

challenge()
exit(0)