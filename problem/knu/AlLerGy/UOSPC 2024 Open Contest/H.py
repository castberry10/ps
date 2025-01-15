from collections import deque
n, m, a, b, c = map(int, input().split())
graph = {a: (b, -c)}

for i in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append((v, 1))
q = deque()

q.append()