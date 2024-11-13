def floyd_warshall(graph, vertices):
    # 최단 거리 행렬 초기화
    dist = [[float('inf')] * vertices for _ in range(vertices)]
    
    # 자기 자신으로의 거리는 0으로 설정
    for v in range(vertices):
        dist[v][v] = 0
    
    # 주어진 간선에 따라 거리 초기화
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = w

    # 플로이드-워셜 알고리즘 적용
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 음의 사이클 존재 확인
    for v in range(vertices):
        if dist[v][v] < 0:
            print("그래프에 음의 사이클이 존재합니다.")
            return None  # 음의 사이클이 있으면 None 반환

    # 최단 거리 행렬 반환
    return dist

# 예제 사용법
graph = {
    0: [(1, 3), (2, 8), (4, -4)],
    1: [(3, 1), (4, 7)],
    2: [(1, 4)],
    3: [(0, 2), (2, -5)],
    4: [(3, 6)]
}
vertices = 5  # 정점의 수

distances = floyd_warshall(graph, vertices)
if distances is not None:
    print("모든 정점 쌍 간의 최단 거리:")
    for row in distances:
        print(row)
