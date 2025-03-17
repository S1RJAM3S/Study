n, m = [int(x) for x in input().split()]
matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    matrix[u-1][v-1] += 1
    matrix[v-1][u-1] += 1

def is_bipartite(u: int) -> bool:
    Q = []
    colour[u] = 0
    Q.append(u)
    while(len(Q) != 0):
        x = Q.pop(0)
        for v in range(n):
            if (matrix[x][v] != 0 ):
                if (x == v): 
                    return False
                elif (colour[v] == -1):
                    colour[v] = 1 - colour[x]
                    Q.append(v)
                elif(colour[x] == colour[v]): return False
    return True

colour = [-1 for _ in range(n)]
print(int(is_bipartite(0)))