n = int(input())

def fibo(n: int) -> int:
    if(n == 1 or n == 2): return 1
    return fibo(n - 1) + fibo(n - 2)

mem = [1, 1]
def fibo_mem(n: int) -> int:
    if(n <= len(mem)): return mem[n-1]
    else:
        f = fibo_mem(n - 1) + fibo_mem(n - 2)
        mem.append(f)
        return f
    
print(fibo(n))
print(fibo_mem(n))