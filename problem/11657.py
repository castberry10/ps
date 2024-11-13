import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grape = {}
for i in range(m):
    a, b, c = map(int, input().split())
    if a not in grape:
        grape[a] = []
    grape[a].append((b, c))
# def bellman_ford(graph, vertices, src):
#     # 최단 거리 배열을 무한대로 초기화, 시작 정점의 거리는 0
#     dist = [float('inf')] * vertices
#     dist[src] = 0

#     # V-1번 반복하여 최단 거리 업데이트
#     for _ in range(vertices - 1):
#         for u in graph:
#             for v, w in graph[u]:
#                 if dist[u] != float('inf') and dist[u] + w < dist[v]:
#                     dist[v] = dist[u] + w

#     for u in graph:
#         for v, w in graph[u]:
#             if dist[u] != float('inf') and dist[u] + w < dist[v]:
#                 print("음의 사이클 존재")
#                 return None  

#     return dist
def bellman_ford(start):
    distance_list = [1e9] * (n + 1)
    distance_list[start] = 0
    
    for i in range(n - 1):
        for u in grape:
            for v, w in grape[u]:
                if distance_list[u] != 1e9 and distance_list[u] + w < distance_list[v]:
                    distance_list[v] = distance_list[u] + w
    for u in grape:
        for v, w in grape[u]:
            if distance_list[u] != 1e9 and distance_list[u] + w < distance_list[v]:
                return None
    return distance_list
data = bellman_ford(1)
if data == None:
    print(-1)
else:
    for i in range(n-1):
        if data[i + 2] >= 1e9:
            print(-1)
        else:
            print(data[i + 2])
