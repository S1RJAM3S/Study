n, m = [int(x) for x in input().split()]
matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    matrix[u-1][v-1] += 1
    matrix[v-1][u-1] += 1

def DFS(u: int):
    for i in range(n):
        if (not visited[i] and matrix[u][i] != 0):
            print(i+1, end=' ')
            visited[i] = True
            DFS(i)

visited = [False for _ in range(n)]
for i in range(n):
    if (not visited[i]):
        print(i+1, end=' ')
        visited[i] = True
        DFS(i)