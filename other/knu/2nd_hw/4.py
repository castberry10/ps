import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
# 그래프 표현 - 
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

city_list = list(map(int, input().split()))

# BFS 
# 특정 지점에서 모든 지점으로의 시간 측정
# 시간 복잡도 : 인접 리스트이기에 O(nm)
def bfs(start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    q = deque()
    q.append(start)
    while q:
        current = q.popleft()
        for i in graph[current]:
            if dist[i] > dist[current] + 1:
                dist[i] = dist[current] + 1
                q.append(i)
    return dist

# 필수 방문 도시 BFS
# 시간 복잡도 O(k x (N + M))
distance = {city: bfs(city) for city in city_list}

# 백트래킹
# 브루트포스 시간복잡도는 O(N!)
def bt(current_city, visited, total_time):
    if len(visited) == k:  # 모든 필수 도시를 방문했으면 종료
        return total_time

    min_time = float('inf') 
    for next_city in city_list: # 순회 
        if next_city not in visited: # 방문 안하면 
            time = distance[current_city][next_city]
            if time < float('inf'):  # 경로가 존재할 때만 진행
                if visited:
                    min_time = min(min_time, bt(next_city, visited | {next_city}, total_time + time))

    return min_time

answer = float('inf')

for city in city_list:
    answer = min(answer, bt(city, {city}, 0))

if answer == float('inf'):
    print(-1)
else:
    print(answer)