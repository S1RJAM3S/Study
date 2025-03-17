import random
from typing import List

FLAG = "BKSEC{fl4g_neeee}"

FLAG = (FLAG[len(FLAG) // 2:] + FLAG[:len(FLAG) // 2])[::-1]


def random_gen(bits: List[int]) -> List[int]:

    shuffled_indices = list(range(len(bits)))
    random.shuffle(shuffled_indices)

    half_size = len(shuffled_indices) // 2
    indices_keep = shuffled_indices[:half_size]
    indices_flip = shuffled_indices[half_size:]

    modified_bits = bits.copy()
    
    for idx in indices_keep:
        modified_bits[idx] = modified_bits[idx]
    for idx in indices_flip:
        modified_bits[idx] = 1 - modified_bits[idx]
    
    return modified_bits

def bit_to_hex(bits: List[int]) -> str:
    bit_string = ''.join(map(str, bits))
    return hex(int(bit_string, 2))[2:].zfill(len(bits) // 4)

def string_to_bits(s: str) -> List[int]:
    return [int(bit) for char in s for bit in bin(ord(char))[2:].zfill(8)]

flag_bits = string_to_bits(FLAG)


def generate_data_file(filename: str, num_lines: int = 1_000_000):
    with open(filename, "w") as file:
        for _ in range(num_lines):
            modified_bits = random_gen(flag_bits)
            file.write(bit_to_hex(modified_bits) + "\n")

generate_data_file("data.txt")
