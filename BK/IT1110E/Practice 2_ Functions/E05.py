n = int(input())

fibo_series = [1, 1]

def fibo(n: int):
    if (n <= len(fibo_series)): return fibo_series[n - 1]
    else:
        temp_fibo = fibo(n-1) + fibo(n-2)
        fibo_series.append(temp_fibo)
        return temp_fibo
        
if(n == 0): print('0')
else: print(fibo(n))