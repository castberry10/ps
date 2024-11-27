import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
## Floyd-Warshall
# 시간은 O(N^3) 
# 각 노드와 노드의 최소시간 조회는 O(1)
for k in range(1, n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

visit = set()
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] >= 1e9:
            print('INF', end=" ")
        else:
            print(graph[i][j], end = ' ')
    print()