import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[1e11 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    graph[i + 1][i + 1] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] < 1e11 and graph[k][j] < 1e11:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(n):
    for j in range(n):
        if graph[i + 1][j + 1] >= 1e11:
            print(0, end = " ")
        else:
            print(graph[i+1][j+1] , end = " ")
    if i != n - 1:
        print()

################# 수정 해야함 ###################