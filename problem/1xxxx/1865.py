import sys
input = sys.stdin.readline

def solve():
    n, m, w = map(int, input().split())
    graph = {}
    for i in range(m):
        s, e, t = map(int, input().split())
        if s not in graph:
            graph[s] = {}
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], t)
    for i in range(w):
        s, e, t = map(int, input().split())
        if s not in graph:
            graph[s] = {}
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], -1 * t)
    
    def be_fo(start, n):
        data = [1e9] * (n + 1)
        data[start] = 0

        for i in range(n - 1):
            for u in graph:
                for v in graph[u]:
                    if data[u] + graph[u][v] < data[v]:
                        data[v] = data[u] + graph[u][v]
        for u in graph:
            for v in graph[u]:
                if data[u] + graph[u][v] < data[v]:
                    return True
        return False
    for u in graph:
        if be_fo(u, n):
            print("YES")
            return
    print("NO")


t = int(input())
for _ in range(t):
    solve()


# 아직 안품