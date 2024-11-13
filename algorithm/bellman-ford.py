def bellman_ford(graph, vertices, src):
    # 최단 거리 배열을 무한대로 초기화, 시작 정점의 거리는 0
    dist = [float('inf')] * vertices
    dist[src] = 0

    # V-1번 반복하여 최단 거리 업데이트
    for _ in range(vertices - 1):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in graph:
        for v, w in graph[u]:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("음의 사이클 존재")
                return None  

    return dist

graph = {
    0: [(1, -1), (2, 4)],
    1: [(2, 3), (3, 2), (4, 2)],
    3: [(2, 5), (1, 1)],
    4: [(3, -3)]
}
vertices = 5  
src = 0       

distances = bellman_ford(graph, vertices, src)
if distances is not None:
    print("각 정점까지의 최단 거리:", distances)
