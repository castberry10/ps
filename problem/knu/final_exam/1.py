#최소 공통 부모 문제
# from collections import deque # 덱을 사용 선언
# n = int(input()) # n 입력
# graph = {} #그래프
# parent = [0] * (n + 1) # 부모
# depth = [0] * (n + 1) # 깊이 배열
# for i in range(n-1): # 간선 입력수
#     u, v = map(int, input().split())
#     if u not in graph:
#         graph[u] = []
#     graph[u].append(v) # 자식을 가르키는 그래프 
#     parent[v] = u # 부모 부서를 가르킴 
# m = int(input())

# def bfs():
#     print("bfs")
#     start = 1
#     q = deque()
#     q.append(start)
#     while q:
#         current = q.pop()
#         if current in graph:
#             for v in graph[current]:
#                 depth[v] = depth[current] + 1
#                 q.append(v)
    
# bfs()   # bfs를 진행하여 깊이를 계산 
# for j in range(m):
#     a, b = map(int, input().split())
    
#     if depth[a] == depth[b]: 
#         pass
#     elif depth[a] > depth[b]: #깊이가 다르다면 교체합니다. 
#         a, b = b, a
        
#     # 여기서부터는 depth가 b가 무조건 큼 (차이가 있다면) 
#     while depth[a] != depth[b]:
#         depth[b] -= 1
#         b = parent[b]
    
#     while True:
#         if a == b:
#             print(b)
#             break
#         else:
#             a = parent[a]
#             b = parent[b]
# 위 코드는 부모가 하나임을 가정한 코드입니다. 
# 아래 코드는 u부서가 v부서의 부모가 아닐경우의 코드입니다. 
from collections import deque

n = int(input())
graph = {}
parent = [0] * (n + 1)
depth = [0] * (n + 1) 

for i in range(n-1):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[v].append(u)
    graph[u].append(v) 
    
m = int(input())
visit = set()

def bfs():
    start = 1
    q = deque()
    visit.add(start)
    q.append(start)
    while q:
        current = q.pop()
        if current in graph:
            for v in graph[current]:
                if v not in visit:
                    depth[v] = depth[current] + 1
                    parent[v] = current
                    visit.add(v)
                    q.append(v)
bfs()   
for j in range(m):
    a, b = map(int, input().split())
    if depth[a] == depth[b]:
        pass
    elif depth[a] > depth[b]:
        a, b = b, a
        
    # 여기서부터는 depth가 b가 무조건 큼 (차이가 있다면) 
    while depth[a] != depth[b]:
        depth[b] -= 1
        b = parent[b]
    
    while True:
        if parent[a] == 0:
            print(1)
            break
        if a == b:
            print(b)
            break
        else:
            a = parent[a]
            b = parent[b]
            
# 13
# 1 2
# 1 3
# 2 4
# 2 5
# 5 6
# 5 7
# 6 10 
# 6 11
# 7 12
# 7 13
# 3 8
# 3 9
# 1
# 11 12