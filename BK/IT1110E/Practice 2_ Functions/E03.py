import math

def print_prime(n: int):
    def is_prime(n: int) -> bool:
        if (n == 2): return True
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if (n % i == 0):
                return False
        return True
    for i in range(2, n):
        if (is_prime(i)):
            print(i, end=" ")
