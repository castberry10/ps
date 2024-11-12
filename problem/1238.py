# from collections import deque
import heapq
# 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 
# 파티를 벌이기로 했다. 
# 이 마을 사이에는 총 M개의 단방향 도로들이 있고 
# i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.
n, m, x = map(int, input().split())
graph = {}
for i in range(m):
    start, end, time = map(int, input().split())
    if start not in graph:
        graph[start] = []
    graph[start].append((end, time))

def dijkstra(start):
    queue = []
    timelist = [1e9] * (n + 1)
    heapq.heappush(queue, (0, start))
    timelist[start] = 0

    while queue:
        time, current_node = heapq.heappop(queue)

        if timelist[current_node] < time:
            continue
        if current_node in graph:
            for node, node_time in graph[current_node]:
                cost = time+ node_time
                if timelist[node] > cost:
                    timelist[node] = cost
                    heapq.heappush(queue, (cost, node))
    return timelist
answer = 0
for i in range(n):
    a = dijkstra(i + 1)
    b = dijkstra(x)
    answer = max(answer, a[x] + b[i + 1])
print(answer)