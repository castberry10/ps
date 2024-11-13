import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
grape = {}
for i in range(E):
    u, v, w = map(int, input().split())
    if u not in grape:
        grape[u] = []
    grape[u].append((v, w))

def dijkstra(start):
    q = []
    distance_list =[1e9 for i in range(V + 1)]
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
datalist = dijkstra(k)
for i in range(V):
    temp = datalist[i + 1]
    if temp == 1e9:
        print("INF")
    else:
        print(temp)

