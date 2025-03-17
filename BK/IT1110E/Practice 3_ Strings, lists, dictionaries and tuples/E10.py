tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])
print('\n'.join(list(map(lambda x: ' '.join(x), [[str(i*n + j + 1) for j in range(n)] for i in range(m)]))))