import sys
input = sys.stdin.readline

n, start, end, m = map(int, input().split())
graph = {}
for i in range(m):
    a, b, c = map(int, input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append((b, c))
money_list = list(map(int, input().split()))

def trans_bellman_ford(start):
    distance_list = [-1e9] * (n + 1)
    distance_list[start] = money_list[start]

    for i in range(n + 100):
        for u in graph:
            for v, w in graph[u]:
                if distance_list[u] == -1e9:
                    continue
                elif distance_list[u] >= 1e9:
                    distance_list[v] = 1e9
                elif distance_list[v] < distance_list[u] + money_list[v] - w:
                    distance_list[v] = distance_list[u] + money_list[v] - w
                    if i >= n - 1:
                        distance_list[v] = 1e9
    return distance_list
data = trans_bellman_ford(start)
if data[end] <=-1e9:
    print("gg")
elif data[end] >= 1e9:
    print("Gee")
else:
    print(data[end])