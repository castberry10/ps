import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
depth = [0] * (n + 1)
parent = [0] * (n + 1)
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
while q:
    current_node = q.popleft()
    if current_node in graph:
        for i in graph[current_node]:
            if i not in visit:
                parent[i] = current_node
                depth[i] = depth[current_node] + 1
                q.append(i)
                visit.add(i)
    
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    if depth[a] < depth[b]:
        a, b = b, a
    while depth[a] > depth[b]:
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)
    