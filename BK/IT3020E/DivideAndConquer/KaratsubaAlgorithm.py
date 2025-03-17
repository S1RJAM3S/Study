# a * b = a1*b1 * (10**(2*sp)) + ((a1 + a2)*(b1 + b2) - a1*b1 - a2*b2) * (10**(sp)) + a2*b2

a = input()
b = input()

def make_equal_len(s: str, n: int) -> str:
    for i in range(n-len(s)):
        s = '0' + s
    return s

def KA(a: str, b: str) -> int:
    n = max(len(a), len(b))
    if (len(a) < len(b)):
        a = make_equal_len(a, n)
    if (len(b) < len(a)):
        b = make_equal_len(b, n)
        
    if n == 0: return 0
    if n == 1: return int(a[0])*int(b[0])
    
    fp = n // 2
    sp = n - fp
    
    a1 = a[:fp]
    a2 = a[fp:]
    b1 = b[:fp]
    b2 = b[fp:]
    
    a1b1 = KA(a1, b1)
    a2b2 = KA(a2, b2)
    m = KA(str(int(a1) + int(a2)), str(int(b1) + int(b2)))
    
    return a1b1 * (10**(2*sp)) + (m - a1b1 - a2b2) * (10**sp) + a2b2

print(KA(a, b)) 