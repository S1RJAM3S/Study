import math

pi = math.pi

def exp_m(x):
    res = 0
    n = 0
    while True:
        curr = (x**n) / math.factorial(n)
        res += curr
        if abs(curr) < 1e-9:
            break
        n += 1
    return round(res, ndigits=6)

def sin_m(x):
    x = x % (2*pi)
    res = 0
    n = 0
    while True:
        curr = ((-1)**n) * (x**(2*n+1)) / math.factorial(2*n+1)
        res += curr
        if abs(curr) < 1e-9:
            break
        n += 1
    return round(res, ndigits=6)

def cos_m(x):
    x = x % (2*pi)
    res = 0
    n = 0
    while True:
        curr = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
        res += curr
        if abs(curr) < 1e-9:
            break
        n += 1
    return round(res, ndigits=6)