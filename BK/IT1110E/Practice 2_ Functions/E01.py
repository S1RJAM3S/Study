import math

def is_perfect(n: int):
    sum = 0
    for i in range(1, math.ceil(n/2) + 1):
        if (n % i == 0):
            sum += i
    return True if (sum == n and not n <= 1 and not float(n) != n) else False