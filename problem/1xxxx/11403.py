# 11403
import sys
input = sys.stdin.readline
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def fw():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
fw()
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()