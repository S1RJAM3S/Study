temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])

a = []
b = []
for i in range(m):
  a.append(input().split(' '))
for i in range(m):
  b.append(input().split(' '))

result =  [[0 for i in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        result[i][j] = str(int(a[i][j]) + int(b[i][j]))
print('\n'.join(list(map(lambda x: ' '.join(x), result))))