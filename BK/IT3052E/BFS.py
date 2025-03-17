n, m = [int(x) for x in input().split()]
matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    matrix[u-1][v-1] += 1
    matrix[v-1][u-1] += 1

def BFS(u: int):
    Q = []
    print(u+1, end=' ')
    visited[u] = True
    Q.append(u)
    while(len(Q) != 0):
        x = Q.pop(0)
        for v in range(n):
            if(not visited[v] and matrix[x][v] != 0):
                print(v+1, end=' ')
                visited[v] = True
                Q.append(v)
            

visited = [False for _ in range(n)]
for i in range(n):
    if (not visited[i]):
        BFS(i)