# 개선된 LCA
#pypy로 통과 가능
import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
depth = [0] * (n + 1)
parent_depth = 0

temp = 1
while temp <= n:
    temp *= 2
    parent_depth += 1

parent = [[0 for _ in range(n + 1)] for _ in range(parent_depth + 1)]

graph = {}
visit = set()

for i in range(n - 1):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visit.add(1)

## BFS ## 
while q:
    current_node = q.popleft()
    if current_node in graph:
        for i in graph[current_node]:
            if i not in visit:
                parent[0][i] = current_node
                depth[i] = depth[current_node] + 1
                q.append(i)
                visit.add(i)

## BFS end ## 

for i in range(1, parent_depth + 1):
    for j in range(1, n + 1):
        parent[i][j] = parent[i - 1][parent[i - 1][j]]


m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a

    for k in range(parent_depth, -1, -1):
        if 2 ** k <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]
    
    for k in range(parent_depth, -1, -1):
        if a == b: 
            break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    if a != b:
        a = parent[0][a]
    print(a)
    