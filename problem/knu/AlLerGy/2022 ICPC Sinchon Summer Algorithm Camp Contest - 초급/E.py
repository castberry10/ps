import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = input().rstrip()  
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

visit = [False] * (n + 1)
queue = deque()
queue.append((0, 0))  
visit[0] = True

depth = {}

temp = 0 
while queue:
    node, d = queue.popleft()
    if d not in depth:
        depth[d] = data[node]
    else:
        # print(data[node-1], graph[d-1])
        if node in graph[d-1] or d == 0:
            depth[d] = max(depth[d], data[node])
        # depth[d] = max(depth[d], data[node - 1])
    
    for j in graph[node]:
        if not visit[j]:
            visit[j] = True
            queue.append((j, d + 1))
# print(g)
print(depth)
temp = max(depth.keys())
result = ''.join(depth[d] for d in range(temp+1))
print(result)

# 10
# aaaacddeba
# 1 2
# 1 3
# 1 4
# 2 5
# 3 6
# 4 7
# 5 8
# 6 9
# 7 10

# answer:
# aadb
# import sys
# from collections import deque

# input = sys.stdin.readline

# n = int(input())
# data = input().rstrip()
# graph = [[] for _ in range(n)]

# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     graph[u - 1].append(v - 1)
#     graph[v - 1].append(u - 1)

# visit = [False] * n
# queue = deque()
# queue.append((0, 0))  # (노드, 깊이)
# visit[0] = True

# depth = {}

# while queue:
#     node, d = queue.popleft()
    
#     if d not in depth:
#         depth[d] = data[node]
#     else:
#         depth[d] = max(depth[d], data[node])
    
#     for neighbor in graph[node]:
#         if not visit[neighbor]:
#             visit[neighbor] = True
#             queue.append((neighbor, d + 1))

# max_depth = max(depth.keys())
# result = ''.join(depth[d] for d in range(max_depth + 1))
# print(result)
