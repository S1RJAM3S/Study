from pwn import *

# Correct LCG parameters for Bash's RANDOM
MULTIPLIER = 1103515245
INCREMENT = 12345
MODULUS = 2**31  # Corrected modulus to 2^31

def simulate_flips(seed, num_flips):
    current_seed = seed
    flips = []
    for _ in range(num_flips):
        current_seed = (current_seed * MULTIPLIER + INCREMENT) % MODULUS
        random_value = (current_seed >> 16) & 0x7FFF
        flip = 1 if (random_value % 3 == 1) else 0
        flips.append(flip)
    return flips

def brute_force_seed(observed):
    # Iterate over all possible 15-bit seeds (0-32767)
    for seed in range(0, 32768):
        flips = simulate_flips(seed, len(observed))
        if flips == observed:
            return seed
    return None

def main():
    while True:
        # Connect to the server
        r = remote('challs.watctf.org', 5156)  # Replace with actual server details

        # Collect initial outcomes (bet on first N rounds)
        observed = []
        money = 5
        N = 30  # Adjust based on needed accuracy

        for _ in range(N):
            r.recvuntil('#? ')
            r.sendline('1')  # Bet "Yes"
            result = r.recvline()
            print(result)
            if b'won!' in result:
                observed.append(1)
                money += 1
            else:
                observed.append(0)
                money -= 1
            if money <= 0:
                print("Ran out of money during initial bets!")
                r.close()
                break
        if (money <= 0):
            continue
        break

    # Brute-force the seed
    seed = brute_force_seed(observed)
    if seed is None:
        print("Failed to find seed!")
        return

    # Predict future flips and bet only on wins
    current_seed = seed
    flips_generated = simulate_flips(seed, N)  # Already used N flips
    remaining_flips = simulate_flips(current_seed, 1000)  # Generate enough

    for flip in remaining_flips:
        if money > 1000:
            break
        r.recvuntil('Do you want to bet')
        if flip == 1:
            r.sendline('1')  # Bet "Yes"
            money += 1
        else:
            r.sendline('2')  # Bet "No"

    # Print the flag
    r.recvuntil('CONGRATS!!!!')
    print(r.recvline().decode())

if __name__ == '__main__':
    main()