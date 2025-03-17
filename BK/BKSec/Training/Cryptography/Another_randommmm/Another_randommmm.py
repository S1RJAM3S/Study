from Crypto.Util.number import long_to_bytes
from hashlib import sha256
from randcrack import RandCrack

# Load the leaked values from leak.txt
with open('D:\\Study\\BK\\BKSec\\Training\\Cryptography\\Another_randommmm\\leak.txt', 'r') as f:
    leak = eval(f.readline().strip())

# Initialize RandCrack
rc = RandCrack()

# Feed the leaked values into RandCrack
bits_submitted = 0
for value in leak:
    # Split the 1024-bit value into 32-bit chunks
    for _ in range(32):
        if bits_submitted >= 624:
            break  # Stop after submitting 624 bits
        rc.submit(value & 0xFFFFFFFF)  # Submit the lowest 32 bits
        value >>= 32  # Shift right by 32 bits to process the next chunk
        bits_submitted += 1

# Debug: Print the number of bits submitted
print("Bits submitted:", bits_submitted)

# Predict the next random number (used for the flag)
predicted_random = rc.predict_getrandbits(1024)

# Debug: Print the predicted random number
print("Predicted random number:", predicted_random)

# Compute the flag
flag_hash = sha256(long_to_bytes(predicted_random)).hexdigest()
flag = f'BKSEC{{{flag_hash}}}'

# Output the flag
print("Recovered flag:", flag)