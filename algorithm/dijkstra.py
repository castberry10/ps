import heapq
############
grape = {}
V, E = 5, 4
##########
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
##############