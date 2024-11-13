import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
grape = {}
for i in range(E):
    u, v, w = map(int, input().split())
    if u not in grape:
        grape[u] = []
    grape[u].append((v, w))
    if v not in grape:
        grape[v] = []
    grape[v].append((u, w))
v1, v2 = map(int, input().split())
def dijkstra(start):
    q = []
    distance_list =[1e11 for i in range(V + 1)]
    heapq.heappush(q, (0, start))
    distance_list[start] = 0

    while q:
        current_distance, current_node = heapq.heappop(q)
        if current_distance > distance_list[current_node]:
            continue

        if current_node in grape:
            for neighbor, weight in grape[current_node]:
                distance = current_distance + weight
                if distance < distance_list[neighbor]:
                    distance_list[neighbor] = distance
                    heapq.heappush(q, (distance, neighbor))
    return distance_list
v1_list = dijkstra(v1)
v2_list = dijkstra(v2)
list_start = dijkstra(1)

v1v2 = list_start[v1] + v1_list[v2] + v2_list[V]
v2v1 = list_start[v2] + v2_list[v1] + v1_list[V]

# DEBUG
# print(v1v2, v2v1)
# print(list_start)
# print(v1_list)
# print(v2_list)

if v1v2 >= 1e11 and v2v1 >= 1e11:
    print(-1)
else:
    print(min(v1v2, v2v1))
